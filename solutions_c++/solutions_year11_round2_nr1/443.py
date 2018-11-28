#include<iostream>
#include<vector>
using namespace std;

main()
{
      int t,number=1;
      scanf("%d",&t);
      while(t--)
      {
                int n;
                scanf("%d",&n);
                vector<vector<int> > v(n, vector<int> (n,0));
                vector<float> wp(n,0);
                vector<float> owp(n,0);
                vector<float> oowp(n,0);
                vector<float> rpi(n,0);
                int i,j,k;
                char c;
                scanf("%c",&c);
                for(i=0;i<n;i++)
                {
                                for(j=0;j<n;j++)
                                {
                                                scanf("%c",&c);
                                                if(c=='1')
                                                v[i][j]=1;
                                                else if(c=='0')
                                                v[i][j]=0;
                                                else
                                                v[i][j]=-1;
                                }
                                scanf("%c",&c);
                }
                              
                for(i=0;i<n;i++)
                {
                                wp[i]=0;
                                int win=0,total=0;
                                for(j=0;j<n;j++)
                                {
                                    if(v[i][j]!=-1)
                                    {
                                                   total++;
                                                   if(v[i][j]==1)
                                                   win++;
                                    }
                                }
                                if(total==0)
                                wp[i]=0;
                                else
                                wp[i]=(double)((double)win/(double)total);
                }            
                
                for(i=0;i<n;i++)
                {
                                int totaln=0;
                                for(j=0;j<n;j++)
                                {
                                                if(v[i][j]!=-1)
                                                {
                                                               totaln++;
                                                               int total=0,win=0;
                                                               for(k=0;k<n;k++)
                                                               {
                                                                               if(k!=i&&v[j][k]!=-1)
                                                                               {
                                                                                                    total++;
                                                                                                    if(v[j][k]==1)
                                                                                                    win++;
                                                                               }
                                                               }
                                                               owp[i]+=(double)((double)win/(double)total);
                                                }
                                }
                                owp[i]=(double)(owp[i]/(double)totaln);
                }
                                
                                
                for(i=0;i<n;i++)
                {
                                int totaln=0;
                                oowp[i]=0;
                                for(j=0;j<n;j++)
                                {
                                                if(v[i][j]!=-1)
                                                {
                                                               oowp[i]+=owp[j];
                                                               totaln++;
                                                }
                                }
                                oowp[i]=(double)(oowp[i]/(double)totaln);
                                rpi[i]=0.25*wp[i] + 0.5*owp[i] + 0.25*oowp[i];
                }
                printf("Case #%d:\n",number++);
                for(i=0;i<n;i++)
                {
                                printf("%lf\n",rpi[i]);
                }
                                                
                
      }
}                
