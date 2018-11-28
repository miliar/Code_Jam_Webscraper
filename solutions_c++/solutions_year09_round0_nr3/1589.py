#include<iostream>
using namespace std;
#define myfor(i,c,d) for(i = (c);i<=(d);++i)
char cst[30] = "welcome to code jam";
const int S_size = 520;
int f[S_size][22];
void work(char *st,int &ans)
{
    memset(f,0,sizeof(f));
    int j,i = 0;
    f[0][0] = 1;
    while(*st)
    {
        ++i;
        myfor(j,0,19)
            f[i][j] = f[i-1][j];
        myfor(j,1,19)
            if( *st == cst[j-1])
            {
                f[i][j]+=f[i-1][j-1];
                f[i][j]%=10000;//be careful
            }
            ++st;
    }
    ans = f[i][19];
}
int main()
{
    int tcase,ans;
    int cc;
    char st[S_size];
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d\n",&tcase);
    myfor(cc,1,tcase)
    {
        gets(st);
        ans = 0;
        work(st,ans);
        printf("Case #%d: ",cc);
        if( ans<1000)putchar('0');
        if(ans<100)putchar('0');
        if(ans<10) putchar('0');
        printf("%d\n",ans);
    }
}