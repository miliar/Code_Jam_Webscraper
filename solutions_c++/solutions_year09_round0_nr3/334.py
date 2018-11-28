#include<iostream>
using namespace std;

const int s[19] = { 'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m' };
int n,l,a;
int f[20];

int main()
{
    freopen("c1.in","r",stdin);
    freopen("c1.out","w",stdout);
    scanf("%d",&n);
    getchar();
    for (int i=1; i<=n; i++ )
    {
        printf("Case #%d: ",i);
        l=0;
        memset(f,0,sizeof(f)); f[0]=1;
        while (1)
        {
              a=getchar();
              if (a==10) break;
              for (int j=19; j>0; j-- ) 
                 if (a==s[j-1]) 
                 {
                    f[j]+=f[j-1];
                    if (f[j]>=10000) f[j]-=10000;
                 }
        }
        
        printf("%04d\n",f[19]);
    }
    fclose(stdin);
    fclose(stdout);
}
