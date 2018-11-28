#include <iostream>
#include <string>
using namespace std;
string o;
char s[501];
int N,Cn,i,j,k,len,tot,tmp;
int t[500];
int main()
{
    freopen("C-large.in.txt","r",stdin);
    freopen("C-large.out.txt","w",stdout);
    o="welcome to code jam";
    scanf("%d",&N);
    gets(s);
    for (Cn=1;Cn<=N;Cn++)
    {
        memset(t,0,sizeof(t));
        gets(s);
        len=strlen(s);
        for (i=len-1;i>=0;i--)
            if (s[i]==o[o.size()-1])
               t[i]=1;
        for (i=o.size()-2;i>=0;i--)
        {
            k=0;
            for (j=len-1;j>=0;j--)
            {
                tmp=t[j];
                if (o[i]==s[j])
                    t[j]=k;
                else
                    t[j]=0;
                k=(k+tmp) % 10000;
            }
        }
        tot=0;
        for (i=0;i<len;i++)
            tot=(tot+t[i]) % 10000;
        printf("Case #%d: ",Cn);
        if (tot<1000)
           printf("0");
        if (tot<100)
           printf("0");
        if (tot<10)
           printf("0");
        printf("%d\n",tot);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
