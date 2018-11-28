#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#define n 1001
using namespace std;

map<vector<int>,long long>mp;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    long long T,C,G,test,i,j,S,val,k,add,u,p,sum,kas=1;
    cin>>test;
    while(test--)
    {
       vector<int>aa(n),bb(n);
       vector<int>st(n),mm(n);
       cin>>T>>C>>G;
       aa.clear();
       bb.clear();
       st.clear();
       mm.clear();
       for(i=0;i<G;i++)
       {
         cin>>S;
         aa.push_back(S) ;
       }

       sum=0;
       for(i=k=0;i<T;i++)
       {
            add=0;
            bb.clear();
            st.clear();

            if(mp[aa]==0)
            {
                    mp[aa]=i;
                    for(j=add=0,val=0;j<G;j++)
                    {
                        if(add+aa[j]<=C)
                        {
                            add+=aa[j];
                            bb.push_back(aa[j]);
                        }
                        else
                        {
                            u=j;
                            for(p=u;p<G;p++)
                            st.push_back(aa[p]);

                            for(u=val;u<j;u++)
                            st.push_back(bb[u]);
                            aa=st;
                            break;
                        }

                     }
                     mm.push_back(add);
                     sum+=add;
             }
             else
                break;
       }

       int d=mp[aa];
       int sa=i;
       int diff= i- d;

       int move=T-i;

       int repeat=move/diff;
       int rem=move%diff;

        long long  sum1=0;

        for(i=d;i<sa;i++)
         sum1+=mm[i];
         sum1*=repeat;

         int cnt=0;
         for(i=d;cnt<rem;i++,cnt++)
          sum1+=mm[i];
          sum1+=sum;
          cout<<"Case #"<<kas++<<":"<<" "<<sum1<<endl;
    }
   return 0;
}
