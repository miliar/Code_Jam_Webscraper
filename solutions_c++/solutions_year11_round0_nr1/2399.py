# include <iostream>
# include <vector>

using namespace std;

int main()
{
    int t,cnt = 1;
    cin>>t;
    while(t--)
    {
              int n,tm[200],po=1,pb=1,ans=0,i,tme[200],tmp,j;
              //vector <int> to(100,-1),tb(100,-1);
              char bt[200];
              cin>>n;
              for(i=0;i<n;i++)
              {
                  cin>>bt[i]>>tm[i];
              }
              if(bt[0] == 'O')
              {
                 tme[0] = abs(tm[0]-po) + 1;
                 po = tm[0];
              }
              if(bt[0] == 'B')
              {
                 tme[0] = abs(tm[0]-pb) + 1;
                 pb = tm[0];
              }
              for(i=1;i<n;i++)
              {
                  if(bt[i]==bt[i-1])
                  {
                        if(bt[i] == 'O')
                        {
                                 tme[i] = abs(tm[i]-po) + 1;
                                 po = tm[i];
                        }
                        if(bt[i] == 'B')
                        {
                                 tme[i] = abs(tm[i]-pb) + 1;
                                 pb = tm[i];
                        }               
                  }
                  else
                  {
                        if(bt[i] == 'B')
                        {
                            tmp = tme[i-1];
                            for(j=i-2;j>=0;j--)
                            {
                                if(bt[j]==bt[j+1])
                                {
                                     tmp += tme[j];                  
                                }
                                else
                                   break;                    
                            }
                            tme[i] = abs(tm[i]-pb) + 1;
                            pb = tm[i];
                            if(tme[i] > tmp)
                               tme[i] -= tmp;
                            else
                                tme[i] = 1;
                        }
                        if(bt[i] == 'O')
                        {
                            tmp = tme[i-1];
                            for(j=i-2;j>=0;j--)
                            {
                                if(bt[j]==bt[j+1])
                                {
                                     tmp += tme[j];                  
                                }
                                else
                                   break;                    
                            }
                            tme[i] = abs(tm[i]-po) + 1;
                            po = tm[i];
                            if(tme[i] > tmp)
                               tme[i] -= tmp;
                            else
                                tme[i] = 1;
                        }
                  }                
              }
    for(i=0;i<n;i++)
       ans += tme[i];
    cout<<"Case #"<<cnt++<<": "<<ans<<endl;
    }
}
