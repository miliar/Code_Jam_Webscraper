#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
        freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int n,p,ot,bt,te,t,test,ca=0;
    vector<int> o,b;
    vector<pair<int,int> > job;
    char a;
    scanf("%d",&test);
    while(test--)
    {
              job.clear();
              b.clear();
              o.clear();
              t=0;
              ot=bt=1;
              scanf("%d",&n);
              for(int i=0;i<n;i++)
              {
                      cin.get();
                      scanf("%c%d",&a,&te);
                      if(a=='O')
                      {
                       job.push_back(make_pair(0,te));
                       o.push_back(te);
                      }
                      else if(a=='B')
                      {
                       job.push_back(make_pair(1,te));
                       b.push_back(te);
                      }
              }
              for(int i=0;i<job.size();i++)
              {
                    if(job[i].first==0)
                    {
                         if(o.size()>0)
                         {
                           while(ot!=o[0])
                           {
                                if(o.size()>0)
                                {
                                if(ot<o[0])
                                ot++;
                                else if(ot>o[0]  &&o.size()>0) 
                                ot--;
                                }
                                t++;
                               if(b.size()>0)
                               {
                                   if(bt<b[0])
                                        bt++;
                                   else if(bt>b[0])
                                        bt--;
                               }
                           }
                         }
                           t++;
                           if(b.size()>0)
                           {
                           if(bt<b[0])
                                bt++;
                           else if(bt>b[0])
                                bt--;
                           }
                           if(o.size()>0)
                           o.erase(o.begin());
                    }
                    else if(job[i].first==1)
                    {
                         if(b.size()>0)
                         {
                           while(bt!=b[0])
                           {
                                if(o.size()>0)
                                {
                                if(ot<o[0])
                                ot++;
                                else if(ot>o[0]  &&o.size()>0) 
                                ot--;
                                }
                                t++;
                                if(b.size()>0)
                               {
                               if(bt<b[0])
                                    bt++;
                               else if(bt>b[0])
                                    bt--;
                               }
                           }
                         }
                           t++;
                           if(o.size()>0)
                           {
                           if(ot<o[0])
                                ot++;
                           else if(ot>o[0])
                                ot--;
                           }
                           if(b.size()>0)
                           b.erase(b.begin());
                    }
                    
              }
              printf("Case #%d: %d\n",++ca,t);
    }
    return 0;
}
