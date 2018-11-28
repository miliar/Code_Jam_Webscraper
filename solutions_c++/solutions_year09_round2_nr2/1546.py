#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <sstream>
#include <stack>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int n,tmp,t,res,mul,min;
    char c;
    vector <int> v,v1,v2;
    vector <int>::iterator it;
    scanf("%d%c",&n,&c);
    for(int i=1;i<=n;i++)
    {
        scanf("%d%c",&tmp,&c);
        t=tmp;
        while(t>0)
        {
            v.push_back(t%10);
            t/=10;
        }

        sort(v.begin(),v.end());
         res=0;
            mul=1;
            for(int j=0;j<v.size();j++)
            {
                res+=(v[j]*mul);
                mul*=10;
            }
            v1.push_back(res);
        while(next_permutation(v.begin(),v.end()))
        {
            res=0;
            mul=1;
            for(int j=0;j<v.size();j++)
            {
                res+=(v[j]*mul);
                mul*=10;
            }
            v1.push_back(res);


        }
        sort(v1.begin(),v1.end());
        it=find(v1.begin(),v1.end(),tmp);



        if((it-v1.begin())!=(v1.size()-1)){
            printf("Case #%d: %d\n",i,v1[(it-v1.begin())+1]);

        }

        else
        {
            int ct=0;
            //cout<<v1[0];
            int pp=v1[0];
             v.erase(v.begin(),v.end());
             t=tmp;
             v1.erase(v1.begin(),v1.end());
             while(t>0)
            {
                v.push_back(t%10);
                if(t%10==0)
                    ct++;
                else
                    v1.push_back(t%10);
                t/=10;

            }
           //  cout<<ct;
             if(ct==0)
             {
             t=pp;
             v.erase(v.begin(),v.end());
              v1.erase(v1.begin(),v1.end());
            while(t>0)
            {
                v.push_back(t%10);

                t/=10;

            }
             }
             if(ct==0)
             {
                 res=0;
                mul=1;
                for(int j=0;j<v.size()-1;j++)
                {

                        res+=(v[j]*mul);
                         mul*=10;

                }
                 mul*=10;
                 res+=(v[v.size()-1]*mul);
                printf("Case #%d: %d\n",i,res);
             }
             else
             {

                  res=0;
                mul=1;
                 sort(v1.begin(),v1.end());

                 for(int kk=v1.size()-1;kk>0;kk--)
                 {
                     res+=(v1[kk]*mul);
                         mul*=10;
                 }
                 for(int yy=0;yy<ct;yy++)
                     mul*=10;
                 mul*=10;
                 res+=(v1[0]*mul);
                  printf("Case #%d: %d\n",i,res);
             }

        }
        v.erase(v.begin(),v.end());
        v1.erase(v1.begin(),v1.end());
    }
}