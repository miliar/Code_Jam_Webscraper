#include <iostream>
#include<string>
using namespace std;

char a[5001][16];

int main()
{
   int m,n,i,j,k,r,s,sum,t;
    char b[1000];

   int c[17][2];
   freopen("A-large.in","r",stdin);
   freopen("ans.out","w",stdout);
   scanf("%d %d %d",&m,&n,&t);
   for(i=0;i<n;i++)
   {
       scanf("%s",a[i]);
   }
   int q=1;

   while(t--)
   {
   scanf("%s",b);
    j=0;
   sum=0;
   int size=strlen(b);

   for(i=0;i<size;i++)
   {
       if(b[i]=='(')
        {
           c[j][0]=i;
        }
        if(b[i]==')')
        {
            c[j++][1]=i;
        }

   }
   for(j=0;j<n;j++)
   {
       k=0;
       s=0;
    for(i=0;i<m;i++)
    {

        if(b[k]=='(')
            {
                for(r=k+1;r<c[s][1];r++)
                {
                       if(a[j][i]==b[r])
                        {
                            break;
                        }

                }
                if(r<c[s][1])
                    {
                        k=c[s][1]+1;
                        s++;
                    }
                    else
                    break;
            }
            else
            {
                if(a[j][i]==b[k])
                    k++;
                    else
                    break;
            }
    }
    if(i==m)
     sum++;
   }
    cout<<"Case #"<<q<<": "<<sum<<endl;
    q++;
   }
    return 0;
}
