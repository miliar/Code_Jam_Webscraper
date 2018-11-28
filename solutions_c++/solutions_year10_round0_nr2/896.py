#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <stdio.h>
using namespace std;

#define rep(i,m) for( i=0;i<m;i++)
#define rep2(i,x,m) for(i=x;i<m;i++)
#define C_Max  100
int GCD(int a,int b);

int main ()
{
int i,j,k,m,counter;//counters
long time[3],diff[2],GCD_Tot[1],GCD_final,slarboseconds;
int N[C_Max];
      
                 freopen("B-small-attempt0.in","rt",stdin);    
                 freopen("B-small-attempt0.out","wt",stdout);    
      
                 int C;//test cases number    
                 cin>>C;    
    
                     rep(i,C)    
                     {  cin>>N[i];  
					    rep(j,N[i])
						cin>>time[j];
						sort(time,time+N[i]);

						rep2(k,1,N[i])
							diff[k-1]=time[k]-time[k-1];
						
						GCD_Tot[0]=diff[0];

						if(N[i]>2)
						{  rep2(m,1,N[i]-1)
								GCD_Tot[m]=GCD(GCD_Tot[m-1],diff[m]);


						    GCD_final=GCD_Tot[N[i]-2];
						}
						else
							GCD_final=diff[0];


						slarboseconds=-100;
						counter=1;
						while(slarboseconds <0)
						{slarboseconds =GCD_final*counter-time[0];
						counter++;}


						cout<<"Case #"<<i+1<<": "<<slarboseconds <<endl;
						//cout<<"   "<<GCD_final<<" "<<counter<<"  "<<diff[0]<<"  "<<diff[1];
						//cout<<"  "<<GCD_Tot[0]<<"  "<<GCD_Tot[1]<<endl;
						//cout<<time[0]<<"  "<<time[1]<<"   "<<time[2]<<endl;

						}
    
 
  return 0;    
}    
    




int GCD(int a,int b)
{
 if(b==0) return a;
 return GCD(b,a%b);
}

