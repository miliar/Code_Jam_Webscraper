#include<iostream>
#include<string>

using namespace std;

FILE *fin;
FILE *fout;

int T,R,C;
char t;
char a[100][100];
bool solved[100][100];

bool solve(int i,int j)
{
    /*if(solved[x][y])
        return;
    if(x < 1 || y < 1 || x > R || y > C)
        return;*/
    if(a[i + 1][j] == '#' && a[i + 1][j + 1] == '#' && a[i][j + 1] == '#')
    {
        a[i][j] = '/';
        a[i + 1][j] = '\\';
        a[i][j + 1] = '\\';
        a[i + 1][j + 1] = '/';
        return true;
    }
    return false;    
}

int main()
{
    fin = fopen("in.txt","r");
    fout = fopen("out.txt","w");
    fscanf(fin,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        memset(a,0,sizeof(a));
        memset(solved,false,sizeof(solved));
        bool flag = true;
        fscanf(fin,"%d%d",&R,&C);
        fscanf(fin,"%c",&t);
        for(int i = 1;i <= R;++i)
            fscanf(fin,"%s",a[i] + 1);
        for(int i = 1;i <= R && flag;++i)
            for(int j = 1;j <= C && flag;++j)
            {
                if(a[i][j] == '#')
                    flag = solve(i,j);    
            }
        fprintf(fout,"Case #%d:\n",i);
        if(!flag)
            fprintf(fout,"Impossible\n");
        else
        {
            for(int i = 1;i <= R;++i)
                fprintf(fout,"%s\n",a[i] + 1);
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;    
}
