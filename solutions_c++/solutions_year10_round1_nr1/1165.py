#include <stdio.h>
#include <iostream>
#include <map>
#include <list>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

char b[51][51];
int dpr[51][51],dpb[51][51],k,n;
bool red,blue;
int mp[51][51][51][51];


void fill(int r,int c,int x,int y)
{
  if(mp[r][c][x+2][y+2]==1) {
	return;
  }

  dpr[r][c] =  (b[r][c]=='R');
  dpb[r][c] =  (b[r][c]=='B');
 int str=r,stc=c;
 int nr=r+x,nc=c+y;
  while ((nr>=0 && nr<n)&&(nc>=0 && nc<n))
  {
    dpr[nr][nc] = dpr[r][c] + (b[nr][nc]=='R');
    dpb[nr][nc] = dpb[r][c] + (b[nr][nc]=='B');
    r=nr;c=nc;
    nr=r+x;nc=c+y;
 }
 int K = k-1;
 nr = str+x*K;nc=stc + y*K;
 r=str;c=stc;
 
// cout<<"r=="<<r<<' '<<c<<' '<<dpr[r][c]<<endl;
 while ((nr>=0 && nr<n)&&(nc>=0 && nc<n))
  {
	
 	mp[r][c][x+2][y+2]=1;
 	if ((dpr[nr][nc]-dpr[r][c]) + (b[r][c]=='R') ==k)
		{red=true;
		}

 	if ((dpb[nr][nc]-dpb[r][c]+ (b[r][c]=='B')==k)) {
		blue=true;
	
	}
	
        r+=x;c+=y;
	nr=r+x*K;nc=c+y*K;
  }
}




int main()
{
int tc;
cin>>tc;

for(int t=1;t<=tc;++t)
{
  red=blue=false;
  cin>>n>>k;
  for(int i=n-1;i>=0;--i)
	for(int j=0;j<n;++j)
		{cin>>b[j][i];
 		    mp[j][i][1+2][0+2]=mp[j][i][0+2][1+2]=mp[j][i][1+2][-1+2]=mp[j][i][1+2][1+2]=0;			
		}
  
  for(int i=0;i<n;++i)
  {	
	int dest =n-1;
	for(int j=n-1;j>=0;--j) {
			if(b[j][i]!='.') 
				b[dest--][i] = b[j][i]; 
			
	}
	while(dest>=0)
		b[dest--][i]='.';
   }
 
/*for(int i=0;i<n;++i) {
	for(int j=0;j<n;++j)
	   cout<<b[i][j];
  cout<<endl;
}*/


  for(int i=0;i<n;++i) {
	for(int j=0;j<n;++j)
	 {
	    fill(i,j,0,1);         	
	    fill(i,j,1,0);
	    fill(i,j,1,1);
	    fill(i,j,1,-1);
	    
	 }
   	if(red&&blue) break;
     }
     cout<<"Case #"<<t<<": ";
     if(red&&blue) cout<<"Both\n";
     else if(red) cout<<"Red\n";
     else if(blue) cout<<"Blue\n";
     else cout<<"Neither\n";  
  }
  

}

