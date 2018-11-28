#include<stdio.h>
#include<vector>
#include<bitset>
#include<utility>
#include<string>
#include<string.h>
#include<algorithm>
#include<set>
#include<map>
#include<math.h>
#include<iostream>
#include<conio.h>
using namespace std;

#define max(a,b) (a>=b?a:b)
#define min(a,b) (a<=b?a:b)
#define all(X) (X.begin(),X.end())
#define allr(X) (X.rbegin(),X.rend())
#define mp make_pair
#define pb push_back
#define disp(X) for(int ab=0;ab<N;ab++){printf("%.12g\n",X[ab]);}

int t=1,tests,N,i,j,num;
vector<string> table;
vector<int> total,wins;
vector<double> rpi,wp,owp,oowp;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&tests);
    while(t<=tests)
    {
         scanf("%d",&N);
         table.clear();
         wins.clear();
         total.clear();
         rpi.clear();
         wp.clear();
         owp.clear();
         oowp.clear();
         for(i=0;i<N;i++)
         {
             string temp;
             cin>>temp;
             table.pb(temp);
         }
         //disp(table);
         int win,loss;
         for(i=0;i<N;i++)
         {
             win=loss=0;
             for(j=0;j<N;j++)
             {
                  if(table[i][j]=='1')
                  {win++;}
                  else if(table[i][j]=='0')
                  {loss++;}
             }
             wp.pb((double)win/(win+loss));
             total.pb(win+loss);
             wins.pb(win);
         }
         
         double t_owp;
         for(i=0;i<N;i++)
         {
             t_owp=0;
             num=0;
             for(j=0;j<N;j++)
             {
                  if(table[i][j]!='.')
                  {
                      if(table[j][i]!='.' && total[j]>1)
                      {
                         t_owp+=((double)wins[j]-(table[j][i]-'0'))/(total[j]-1);
                      }
                      else
                      {
                         t_owp+=wp[j];
                      } 
                      num++;
                  }   
             }
             if(num>0)
             {
                owp.pb(t_owp/num);
             }
             else
             {
                owp.pb(0);
             } 
         }      
         
         double t_oowp;               
         for(i=0;i<N;i++)
         {
             t_oowp=0;
             num=0;
             for(j=0;j<N;j++)
             {
                  if(table[i][j]!='.')
                  {
                      t_oowp+=owp[j];
                      num++; 
                  }                    
             }
             if(num>0)
             {
                oowp.pb(t_oowp/num);                
             }
             else
             {
                oowp.pb(0);
             } 
         }   
         //disp(oowp);    
         printf("Case #%d:\n",t);                   
         for(i=0;i<N;i++)
         {
             rpi.push_back(0.25*wp[i]+0.5*owp[i]+0.25*oowp[i]);         
         }       
         disp(rpi);
         
         t++;
    }
    getch();
}
