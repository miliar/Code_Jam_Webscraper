#include <iostream>
#include <string>
#include <stdio.h>

using namespace std;



int main(int argc,char *argv[])
{
int t,h,w,crt;
string s;
cin>>t;

for(int i=0;i<t;i++)
{
crt=0;
cout<<"Case #"<<i+1<<":\n";
cin>>h>>w;
int sink[h][w],map[h][w];
for(int j=0;j<h;j++)
	for(int k=0;k<w;k++)
		sink[j][k]=-1;
for(int j=0;j<h;j++)
	for(int k=0;k<w;k++)
	  cin>>map[j][k];
for(int j=0;j<h;j++)
{	for(int k=0;k<w;k++)
	{
	 int x=j,y=k;
	 while(1)
	 {
	 int minx=x,miny=y;
	 if((x+1)<h && (y+1>=w || map[x+1][y]<map[x][y+1]) && ((y-1)<0 || map[x+1][y]<map[x][y-1]) && (x-1<0 || map[x+1][y]<map[x-1][y]))
		minx++;
	 else  if((y+1)<w && (y-1<0 || map[x][y+1]<map[x][y-1]) && ((x-1)<0 || map[x][y+1]<map[x-1][y]))
	   miny++;
	 else if((y-1)>=0 && (x-1<0 || map[x][y-1]<map[x-1][y]))
	  miny--;
	  else
		minx--;
		
	if(map[minx][miny]<map[x][y])
	  {x=minx;y=miny;}
	else 
	   break;
	   
	 }
	 
	 if(sink[x][y]>=0 )
	  {printf("%c",'a'+sink[x][y]);}
	 else
	 {
	 sink[x][y]=crt;
	  printf("%c",'a'+crt);
	  //cout<<"("<<crt<<")";
	  crt++;
	 }
	 
	if(k!=w-1)
	cout<<" ";
	
	}

cout<<endl;
}

}


return 0;
}