#include<iostream>
#include<string>

using namespace std;

FILE *fin;
FILE *fout;

int T,n,l,h;
int a[10000];

bool check(int x)
{
    for(int i = 1;i <= n;++i)
        if(x % a[i] != 0 && a[i] % x != 0)
            return false;    
    return true;
}

int main()
{
    fin = fopen("in.txt","r");
    fout = fopen("out.txt","w");
    fscanf(fin,"%d",&T);
    for(int i = 1;i <= T;++i)
    {
        fscanf(fin,"%d%d%d",&n,&l,&h);
        for(int i = 1;i <= n;++i)
            fscanf(fin,"%d",&a[i]);
        int ans = -1000000;
        for(int i = l; i <= h;++i)
            if(check(i))
            {
                ans = i;
                break;
            }
        if(ans < 0)
            fprintf(fout,"Case #%d: NO\n",i);
        else
            fprintf(fout,"Case #%d: %d\n",i,ans);
        
    }
    fclose(fin);
    fclose(fout);
    return 0;    
}
