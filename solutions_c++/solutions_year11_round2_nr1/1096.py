#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>
#include<math.h>
#include<queue>
#include<stack>

using namespace std;

FILE *fin;
FILE *fout;

int T,n;
char a[1000][1000];
int table[1000][1000];


double winpoint(int x,int y)
{
    double wp = 0;
    double win = 0,games = 0;
    for(int i = 1;i <= n;++i)
    {
        if(i == y)
            continue;
        if(table[x][i] == 1)
            ++win; 
        if(table[x][i] != -1)
            ++games;
    }
    wp = win / games;
    return wp;
}

double owinpoint(int x)
{
    double games = 0;
    double points = 0;
    for(int i = 1;i <= n;++i)
        if(table[x][i] != -1)
        {
            ++games;    
            points += winpoint(i,x);
        }
    return points / games;
}

double oowinpoint(int x)
{
    double games = 0;
    double points = 0;   
    for(int i = 1;i <= n;++i)
        if(table[x][i] != -1)
        {
            ++games;    
            points += owinpoint(i);
        }
    return points / games;
}

double calc(int x)
{
    return winpoint(x,0) * 0.25 + owinpoint(x) * 0.5 + oowinpoint(x) * 0.25;
}

int main()
{
    fin = fopen("testin.txt","r");
    fout = fopen("testout.txt","w");
    fscanf(fin,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        fscanf(fin,"%d",&n);
        for(int i = 1;i <= n;++i)
            fscanf(fin,"%s",a[i]);
        for(int i = 1;i <= n;++i)
            for(int j = 0;j < n;++j)
            {
                if(a[i][j] == '.')
                    table[i][j + 1] = -1;
                if(a[i][j] == '1')
                    table[i][j + 1] = 1;
                if(a[i][j] == '0')
                    table[i][j + 1] = 0;
            }
        fprintf(fout,"Case #%d:\n",i);
        for(int i = 1;i <= n;++i)
            fprintf(fout,"%.12lf\n",calc(i));
    }
    fclose(fin);
    fclose(fout);
    return 0;    
}
