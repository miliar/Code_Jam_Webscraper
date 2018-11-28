#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <functional>
#include <map>
#include <set>
#include <cassert>
#include <list>
#include <deque>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <queue>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b)) 
#define SETF(x) memset(x,0xff,sizeof(x))
#define SET0(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB(x) push_back(x)
#define VI vector <int> 
#define VVI vector < vector <int> > 
#define VS vector <string>
 
using namespace std;

vector <string> V;
int N;
map <int, int> M;
struct node
{
	int perm;
	int cost;
};
vector <string> getstring(int perm)
{
	vector <string> T;
	string S;
	int i;
	while(perm)
	{
		T.push_back(V[(perm%10)-1]);
		perm/=10;
	}
	return T;
}
bool chk(vector <string> grid)
{
	int i,j;
	for(i=0;i<N;i++)
		for(j=0;j<N;j++)
			if(grid[i][j]=='1' && j>i)
				return false;
	return true;
}
int getnewperm(int perm, int n, int m)
{
	char buff[100];
	sprintf(buff,"%d",perm);
	char temp;
	temp=buff[n];
	buff[n]=buff[m];
	buff[m]=temp;
	int ret;
	sscanf(buff,"%d",&ret);
	return ret;
}
int solve(int perm)
{
	queue <node> Q;
	node temp;
	temp.perm=perm;
	temp.cost=0;
	Q.push(temp);
	M[perm]=1;
	while(!Q.empty())
	{
		temp=Q.front();
		Q.pop();
		vector <string> grid=getstring(temp.perm);
		int per=temp.perm;
		int cost=temp.cost;
		//cout<<per<<" "<<cost<<endl;
		if(chk(grid))
			return cost; 
		int i,j;
		for(i=0;i+1<N;i++)
		{
			int nperm=getnewperm(per,i,i+1);
			if(M.find(nperm)==M.end())
			{
				node neww;
				neww.perm=nperm;
				neww.cost=cost+1;
				M[nperm]=1;
				Q.push(neww);
			}
		}
	}
}
int main()
{
	int _ncases;
	cin>>_ncases;
	for(int ncases=1;ncases<=_ncases;ncases++)
	{
		int i;
		string t;
		M.clear();
		V.clear();
		cin>>N;
		for(i=0;i<N;i++)
		{
			cin>>t;
			V.push_back(t);
		}
		int n=N;
		int sum=0;
		while(n)
		{
			sum=sum*10+n;
			n--;
		}
		//cout<<sum<<endl;
		int ans=solve(sum);
		cout<<"Case #"<<ncases<<": "<<ans<<endl;
	}
	return 0;
}
