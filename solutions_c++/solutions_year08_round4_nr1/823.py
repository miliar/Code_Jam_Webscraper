#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include<cmath>
#include<iomanip>
#include<fstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
const ll Mod=1000000007;
ll A[600000];
//ll Ans[600000][600000];
ll Ans[10010][2];
int  value[10010];
int gate[10010];
int change[10010];
int lev;
int M,V;
ll infi=1000000000;
ll Cal(int node, int val,int gate)
{
	if(node>M||node<1)
		return 0;
	int c1=node*2;
	int c2=c1+1;
	switch(gate)
	{
	case 0:
		{
			if(val==0)
			{
				return Ans[c1][0]+Ans[c2][0];
			}
			else
			{
				return min(Ans[c1][0]+Ans[c2][1],min(Ans[c1][1]+Ans[c2][0],Ans[c1][1]+Ans[c2][1]));
			}
		}
	case 1:
		{
			if(val==1)
			{
				return Ans[c1][1]+Ans[c2][1];
				
			}
			else
			{
				return min(Ans[c1][0]+Ans[c2][1],min(Ans[c1][1]+Ans[c2][0],Ans[c1][0]+Ans[c2][0]));
			}
		}
	}
	if(node>lev)//р╤вс
	{
		if(value[node]!=val)
			return infi;
		else
			return 0;
	}
	else//╫А╣Ц
	{
		
		if(c1<=M&&c2<=M)
		{
			
		}
		else
			return infi;
	}
}
int  main(){
	string filein;
	//filein="A-small.in";
	//filein="A-large.in";
	//filein="A-small(3).in";
	//filein="A-small-attempt0.in";
	filein="C-small.in";
	filein="A-large.in";
	string fileout;
	//fileout="Anslarge.txt";
	fileout="Anstest.txt";
	//fileout="Anssmall.txt";
	freopen(filein.c_str(), "r", stdin);
	freopen(fileout.c_str(), "w", stdout);
	int  Case;
	cin>>Case;
	for(int  i=1;i<=Case;i++)
	{
		printf("Case #%d: ",i);
		
		cin>>M>>V;
		lev=(M-1)/2;
		for(int j=1;j<=(M-1)/2;j++)
		{
			int G,C;
			cin>>gate[j]>>change[j];			
		}
		for(int j=(M-1)/2+1;j<=M;j++)
		{
			cin>>value[j];
		}
		for(int j=M;j>lev;j--)
		{
			for(int k=0;k<2;k++)
			{
				if(value[j]!=k)
				{
					Ans[j][k]=infi;
				}
				else
				{
					Ans[j][k]=0;
				}
			}
		}
		for(int j=(M-1)/2;j>=1;j--)
		{
			int c1=j*2;
			int c2=c1+1;
			ll tmp;
			for(int k=0;k<2;k++)
			{
				tmp=Cal(j,k,gate[j]);
				if(change[j])
				{
					tmp=min(tmp,1+Cal(j,k,1-gate[j]));
				}
				tmp=min(tmp,infi);
				Ans[j][k]=tmp;
			}
		}
		if(Ans[1][V]==infi)
		{
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
			cout<<Ans[1][V]<<endl;



		
	}

	return 0;
}