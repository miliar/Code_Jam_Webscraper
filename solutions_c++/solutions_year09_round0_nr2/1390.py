#include <iostream>
#include <algorithm>
using namespace std;

char basin[105][105];
int alt[105][105];
char curchar = 'a';
int H,W;
char go(int a, int b)
{
	//cerr<<endl<<"trace: "<<a<<" "<<b<<endl;
	if(basin[a][b]>='a' && basin[a][b]<='z') return basin[a][b];
	int north, west, east, south;
	north = west = east = south = 90000000;
	if(a>0) north = alt[a-1][b];
	if(a<H-1) south = alt[a+1][b];
	if(b>0) west = alt[a][b-1];
	if(b<W-1) east = alt[a][b+1];
	int next = min(min(north,south),min(west,east));
	if(next>=alt[a][b])
	{
		basin[a][b]=curchar;
		
		return curchar++;
	}
	char result;
	if(next == north) result = go(a-1,b);
	else if(next == west) result = go(a,b-1);
	else if(next == east) result = go(a,b+1);
	else if(next == south) result = go(a+1,b);
	basin[a][b]=result;
	return basin[a][b];
}


int main()
{
	int V;
	cin>>V;
	for(int v=0;v<V;v++)
	{
		cin>>H>>W;
		for(int i=0;i<105;i++)
		for(int j=0;j<105;j++)
		{alt[i][j]=900000;basin[i][j]=(char)0;}
		
		for(int i=0;i<H;i++)
		for(int j=0;j<W;j++)
		cin>>alt[i][j];
		curchar = 'a';
		cout<<"Case #"<<v+1<<":"<<endl;
		for(int i=0;i<H;i++)
		{for(int j=0;j<W;j++)
		if(j==W-1)cout<<go(i,j);else cout<<go(i,j)<<" ";cout<<endl;}
	}
	
}