#include<iostream>
#include<vector>
using namespace std;

main()
{
      int tc, number=1;
      scanf("%d",&tc);
      
      while(tc--)
      {
                int l,t,n,c;
                int i,j,sum=0;
                scanf("%d %d %d %d",&l,&t,&n,&c);
                vector<int> v(n,0);
                for(i=0;i<c;i++)
                {
                                scanf("%d",&v[i]);
                }
                for(i;i<n;i++)
                {
                              v[i]=v[i%c];
                }
                
                for(i=0;i<n;i++)
                {
                                sum+=v[i];
                }
                sum*=2;
                vector<bool>mark(n,false);
                for(i=0;i<l;i++)
                {
                                int max=0,maxi=-1,ti=0;
                                for(j=0;j<n;j++)
                                {

                                          if(ti>=t&&max<v[j]&&!mark[j])
                                          {
                                                                max=v[j];
                                                                maxi=j;
                                          }
                                          if(ti<t&&ti+v[j]*2>t&&max<v[j]-(t-ti)/2&&!mark[j])
                                          {
                                                                                      max=v[j]-(t-ti)/2;
                                                                                      maxi=j;
                                          }
                                                if(mark[j])
                                                ti+=v[j];
                                                else
                                                ti+=2*v[j];
                                }
                                //cout<<"boost"<<max<<" "<<maxi<<endl;
                                sum-=max;
                                mark[maxi]=true;
                }
                printf("Case #%d: ",number++);
                cout<<sum<<endl;
}
}
                
                
