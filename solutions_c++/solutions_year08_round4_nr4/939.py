#include <stdio.h>
#include <string>
#include <algorithm>
using namespace std;

int n;
char s[1001];
char v[1001];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int C;
    scanf("%d",&C);
    int cont;
    int fin=1<<20;
    for(int I=0;I<C;I++)
    {
        fin=1<<20;   
        scanf("%d%s",&n,s);
        int ma[]={0,1,2,3,4,5};
        do
        {
            for(int i=0;i<strlen(s);i+=n)
            {
                for(int k=0;k<n;k++)
                {
                    v[i+k]=s[i+ma[k]];
                }
            }
            cont=1;
            char a=v[0];
            for(int i=1;i<strlen(s);i++)
            {
                if(a!=v[i])
                {
                    cont++;
                    a=v[i];
                }
            }
            fin=min(fin,cont);
        }while(next_permutation(ma,ma+n));
        printf("Case #%d: %d\n",I+1,fin);
    }
}
