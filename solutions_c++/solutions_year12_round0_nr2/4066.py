
#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("B-large.out","w",stdout);
    int t,s,p,n,N[101],count=0,test,g,b,ba;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        count=0;
        cin>>n>>s>>p;
        for(int i=0;i<n;i++)
        {
            cin>>test;
            ba=test/3;
            b=test%3;
            g=p-ba;

             if(test==0)
             {
                 if(p==0)
                 {count++; continue;}
                 else
                 continue;
             }
            if(g<=0)
            {
                count++;

                continue;
            }
            else if(g==1)
            {
                if(b>=1)
                {
                    count++;

                    continue;
                }
                else if(s>0)
                {
                    count++;
                     s--;

                    continue;
                }

            }
            else if(g==2)
            {
                if((b==2) && (s>0))
                {
                    count++; s--;
                    continue;
                }


            }



        }
        printf("Case #%d: %d\n",j+1,count);

    }

    return 0;
}
