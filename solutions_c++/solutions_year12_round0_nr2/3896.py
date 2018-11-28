#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    // freopen("B-large.in","r",stdin);
 //   freopen("B-large.out","w",stdout);
    int t,s,p,n,N[101],count=0,test,gap,bonus,base;
    cin>>t;
    for(int j=0;j<t;j++)
    {
        count=0;
        cin>>n>>s>>p;
        for(int i=0;i<n;i++)
        {
            cin>>test;
            base=test/3;
            bonus=test%3;
            gap=p-base;

             if(test==0)
             {
                 if(p==0)
                 {count++; continue;}
                 else
                 continue;
             }
            if(gap<=0)
            {
                count++;
              //  cout<<"a";
                continue;
            }
            else if(gap==1)
            {
                if(bonus>=1)
                {
                    count++;
                 //   cout<<"b";
                    continue;
                }
                else if(s>0)
                {
                    count++; s--;
                    //cout<<"c";
                    continue;
                }
                //else cout<<"d";
            }
            else if(gap==2)
            {
                if((bonus==2) && (s>0))
                {
                    count++; s--;
                   // cout<<"e";
                    continue;
                }


            }



        }
        printf("Case #%d: %d\n",j+1,count);

    }

    return 0;
}
