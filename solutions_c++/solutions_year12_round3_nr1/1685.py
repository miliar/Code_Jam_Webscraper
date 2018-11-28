/* MUKESH GUPTA */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;
#define INF 1000000
typedef long long int LL;
#define FF(i,m,n)    for(int i=m;i<n;i++)
#define F(i,n)    FF(i,0,n)
typedef vector<int> vi;
typedef vector<vi> vvi;

vvi temp;
map<pair<int,int>,int> mp;
vvi GetnextthPower(vvi matrix,int size)
{
	int i,j,k,sum;
	vvi ret(size,vi(size,0));
 for (i=0; i<size; i++)
 {
   for (j=0; j<size; j++)
     {
     // ret[i][j] =0;
     for (k=0; k<size; k++)
       ret[i][j] = ret[i][j] + matrix[i][k]*temp[k][j];
     }
    
 }
temp=ret;	
 return ret;
}

bool isdiamond(map<pair<int,int>,int> mp,int N)
{
FF(i,0,N)
	FF(j,0,N)
{
if(mp[make_pair(i,j)]>1 &&i!=j)return true;
}
return false;
}
void solve()
{

	int N;
	cin>>N;
	vvi matrix(N,vi(N,0));
	mp.clear();
	FF(i,0,N)
	{
		int Mi;
		cin>>Mi;
		FF(j,0,Mi)
		{
		int p;
		cin>>p;
		
		matrix[i][p-1]=1;
		}
	}
	temp.clear();
	temp = matrix;
	bool f=false;
	FF(p,0,N)
		FF(q,0,N)
		{
		if(matrix[p][q]==1 && p!=q)
		mp[make_pair(p,q)]++;
	}
	FF(i,0,N)
	{
	vvi t(N,vi(N));
	t=GetnextthPower(matrix,N);
	FF(p,0,N)
		FF(q,0,N)
		{
		if(t[p][q]>=1 && p!=q)
		mp[make_pair(p,q)]+=t[p][q];
	}
	}
	
	
	if(isdiamond(mp,N))
		{
			cout<<" Yes\n";		
	}
	else
		cout<<" No\n";
	
	
	

}
int main()
{
	int T;
	cin>>T;
	int Kase=1;
	while(T--)
	{
		cout<<"Case #"<<Kase++<<":";
		solve();
	}
}