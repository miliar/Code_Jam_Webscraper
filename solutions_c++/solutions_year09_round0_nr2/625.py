#include<iostream>
#include<string>
#include<vector>
using namespace std;

#define MAX 101

int alt[MAX][MAX];
int drain[MAX][MAX];
int maxi=0;
int T,W,H;

void set_drain(int a,int b)
{
int end=false;
vector<int> Vx,Vy;
int na,nb;
//cout<<"New Drain ..."<<endl;

while(end==false)
	{

end=true;
Vx.push_back(a);
Vy.push_back(b);
//cout<<a<<","<<b<<endl;
//NORTH	
if(a>0) 
	{
	if(alt[a-1][b]<alt[a][b]) { end=false; na=a-1; nb=b; }
	}
//WEST	
if(b>0)
	 {
	 if(alt[a][b-1]<alt[a][b])
	 		{
	 		if(end) { na=a; nb=b-1; end=false; }
			else {
			     if(alt[a][b-1]<alt[na][nb]) { na=a;nb=b-1; }
			     }
			}
	 }
//EAST
if(b<(W-1))
	 {
	 if(alt[a][b+1]<alt[a][b])
	 		{
	 		if(end) { na=a; nb=b+1; end=false; }
			else {
			     if(alt[a][b+1]<alt[na][nb]) { na=a; nb=b+1; }
			     }
			}
	 }
//SOUTH
if(a<(H-1))
	 {
	 if(alt[a+1][b]<alt[a][b])
	 		{
	 		if(end) { na=a+1; nb=b; end=false; }
			else {
			     if(alt[a+1][b]<alt[na][nb]) { na=a+1;nb=b; }
			     }
			}
	 }
	 
	if(end==false) 
			{
			a=na; b=nb;
			if(drain[a][b]>=0) end=true;
			}
	}
	
//cout<<"Terminated at "<<a<<","<<b<<endl;

int val;
if(drain[a][b]==-1) { val=maxi; maxi++; } 
else val=drain[a][b];

int z=Vx.size();
for(int i=0;i<z;i++) drain[Vx[i]][Vy[i]]=val;

return;
}

int main()
{
cin>>T;
for(int i=0;i<T;i++)
	{
	cin>>H>>W;
	for(int a=0;a<H;a++)
		for(int b=0;b<W;b++)
			{
		cin>>alt[a][b];	
		drain[a][b]=-1;
			}
	maxi=0;
	
	for(int a=0;a<H;a++)
		for(int b=0;b<W;b++)
			{
			if(drain[a][b]==-1) set_drain(a,b);
			}
	
	cout<<"Case #"<<i+1<<":"<<endl;
	
	for(int a=0;a<H;a++)
		{
		for(int b=0;b<W;b++)
			cout<<char('a'+drain[a][b])<<" ";	
		cout<<endl;
		}
	}
	
return 0;
}
