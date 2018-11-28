#include <string.h>
#include <fstream>
#include <queue>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>
using namespace std;
#define S(n) 		scanf("%d",&n)
#define SL(n) 		scanf("%lld",&n)
#define FORALL(i,a,b) 	for(int i=a;i<b;i++)
#define ALL(a)   	a.begin(), a.end()
#define IN(a,b) 	((b).find(a) != (b).end())
#define SZ(a) 		((int)(a.size()))
#define MP            	make_pair
#define VI 		vector<int>
#define VPI 		vector<pair<int,int> >
#define DREP(a)      	sort(all(a)); a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) 	(lower_bound(all(arr),ind)-arr.begin())
#define LL 		long long
vector<vector<int> > v;
vector<vector<int> > r;
map<char,int> m;
void preSet()
{
	m['X']=1;
	m['O']=2;
	m['T']=7;
	m['.']=0;
}
void debug(vector<vector<int> > v)
{
	for(int i=0;i<v.size();i++)
	{
		for(int j=0;j<v[i].size();j++)
		{
			cout<<v[i][j]<<" ";
		}
		cout<<endl;
	}
}
int main()
{
	ifstream ifs("file.in");
	preSet();
	int t;
	ifs>>t;
	//cout<<t<<endl;
	int index=0;
	while(t--)
	{
		bool dotFound=false;
		v.clear();
		v.resize(4);
		r.resize(4);
		for(int i=0;i<4;i++)
		{
			v[i].resize(4);
			r[i].resize(4);
		}
		for(int i=0;i<4;i++)
		{
			string in;
			ifs>>in;
		//	cout<<in<<endl;
			for(int j=0;j<4;j++)
			{
				char a;
				a=in[j];
				if(a=='.') dotFound=true;
				v[i][j]=m[a];
				r[i][j]=11;
			}
		}
		//string t;
		//ifs>>t;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				r[i][0] &= v[i][j];
			}
		}
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				r[i][1] &= v[j][i];
			}

		}
		for(int i=0;i<4;i++)
		{
			r[0][2] &= v[i][i];
		}
		for(int i=3,j=0;i>=0;i--,++j)
		{
			r[0][3] &= v[j][i];
		}
		bool ansFound=false;
		cout<<"Case #"<<++index<<": ";
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<2;j++)
			{
				if(r[i][j]==1)
				{
					cout<<"X won\n";
					ansFound=true;
					break;
				}
				else if(r[i][j]==2)
				{
					cout<<"O won\n";
					ansFound=true;
					break;
				}
			}
			if(ansFound) break;
		}
		if(!ansFound)
		{
		if(r[0][2]==1 || r[0][3]==1)
		{
			cout<<"X won\n";
			ansFound=true;
		}
		else if(r[0][2]==2 || r[0][3]==2)
		{
			cout<<"O won\n";
			ansFound=true;
		}
		}
		if(!ansFound)
		{
			if(dotFound)
			{
				cout<<"Game has not completed\n";
			}
			else
			{
				cout<<"Draw\n";
			}
		}
	}
	return 0;
}
