#include<iostream>
#include<vector>
#include<list>
#include<string>
#include<algorithm>
#include <sstream>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>

using namespace std;
int main()
{
    int N,C,i,j,k,flag;
    long long A,B,P,count,x,h,c,grp,d,grp2,w;
    cin>>C;
    for(i=0;i<C;i++)
    {
        cin>>A>>B>>P;
        count=B-A+1;
        
        vector<long long>prime;
        vector<int>group;
        c=0;
        for(x=P;x<B;x++)
        {
                   for(h=2;h*h<=x;h++)
                   {
                                     if(x%h==0)
                                               break;
                   }
                   if(h*h>x)
                   {
                            prime.push_back(x);
                            c++;
                   }
        }
        for(h=A;h<=B;h++)
        {
                         group.push_back(h-A);
        }
        //cout<<"here";
        for(x=0;x<c;x++)
        {
                        flag=0;
                        for(h=A;h<=B;h++)
                        {
                                         if(h%prime[x]==0)
                                         {
                                                  if(flag==0)
                                                  {
                                                             flag=1;
                                                             grp=group[h-A];
                                                             //cout<<"g"<<grp;
                                                  }
                                                  else
                                                  {
                                                             grp2=group[h-A];
                                                             for(w=A;w<=B;w++)
                                                                              if(group[w-A]==grp2)
                                                                              group[w-A]=grp;
                                                  } 
                                         }
                        }
        }
        c=0;
        sort(group.begin(),group.end());
        for(h=A;h<=B;h++)
        {
                        //cout<<group[h-A]<<" ";
                         if(group[h-A]!=group[h-A+1])
                                                 c++;
        }
        cout<<"Case #"<<i+1<<": "<<c<<"\n";
    }
    //system("PAUSE");
    return 0;
}
