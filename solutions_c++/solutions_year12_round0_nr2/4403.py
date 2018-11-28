#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
bool vis[2][35][15];
void init()
{
 		 int flag,t;
 	   for(int x=0;x<=10;x++)
		 for(int y=0;y<=10;y++)
		 if(fabs(x-y)<=2)
		 for(int z=0;z<=10;z++)	 
     if(fabs(x-z)<=2&&fabs(y-z)<=2)
     {
		     if(fabs(x-y)==2||fabs(x-z)==2||fabs(z-y)==2)flag=0;
		     else flag=1;
				 t=max(max(x,y),z);
		    // if(x+y+z==21)cout<<x<<" "<<y<<" "<<z<<":"<<flag<<endl;
		     for(int i=t;i>=0;i--)vis[flag][x+y+z][i]=true;
     }
}
int main()
{
      freopen("a.in","r",stdin);
      freopen("a.out","w",stdout);
      init();
      int T,n,m,p,x,ans;
      scanf("%d",&T);
      for(int cas=1;cas<=T;cas++)
      {
			    scanf("%d%d%d",&n,&m,&p);
					int c=0,t1,t2,t3,t4;
					t1=t2=t3=t4=0;
					for(int i=1;i<=n;i++)
					{
  			      scanf("%d",&x);
  			      //cout<<x<<" "<<vis[0][x][p]<<" "<<vis[1][x][p]<<endl;
	 				   	if(vis[0][x][p]&&vis[1][x][p])t1++;
							else if(vis[0][x][p])t2++;
							else if(vis[1][x][p])t3++;	
							else t4++;
				  }
				  if(m<=t1+t2)ans=min(m,t2)+t3+t1;
				  else if(m<=t1+t2+t4)ans=t1+t2+t3;
				  else ans=t3-(m-t1-t2-t4);
				  printf("Case #%d: %d\n",cas,ans);
				 // cout<<ans<<endl;
			  				 
      }

      return 0;
}
