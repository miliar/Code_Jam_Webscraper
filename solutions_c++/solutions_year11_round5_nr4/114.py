#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <queue> 
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
using namespace std; 

const int inf = 1000*1000*1000; 
#define CL(x,a) memset(x,a,sizeof(x)); 
#define ALL(v) (v).begin(),(v).end() 
#define PII pair<int,int> 
#define PDI pair<double,int> 
#define MP(a,b) make_pair(a,b) 
#define FOR(i,n) for(int i=0;i<n;i++) 
typedef long long LL; 
typedef vector<int> vi; 
typedef vector< vi > vvi; 
typedef vector< vector<PII > > vvpii; 

char str[1000];
string s;
bool Check(string s)
{
	LL x=0;
	for (int i=0;i<s.size();i++)
	{
		x*=2;
		x+=s[i];
	}
	LL L=0,R=(1ll<<31)+1,m;
	while(R-L > 1)
	{
		m=(R+L)/2;
		if (m*m <= x)
			L=m;
		else
			R=m;
	}
	if (L*L == x)
		return 1;
	return 0;
}
void Solve()
{
	int n;
	scanf("%s",str);
	s=string(str);
	n = s.size();
	vector<int> v;
	for (int i=0;i<s.size();i++)
		s[i]-='0';
	FOR(i,n)
		if (str[i] == '?')
			v.push_back(i);
	string res = s;
	for (int i=0;i<(1<<(int)v.size());i++)
	{
		string t=s;
		for (int j=0;j<v.size();j++)
		{
			if (i & (1 << j))
				t[v[j]]=1;
			else
				t[v[j]]=0;
		}
		if (Check(t))
		{
			res = t;
			break;
		}
	}
	for (int i=0;i<res.size();i++)
		res[i]+='0';
	printf("%s",res.c_str());
}
int main() 
{ 
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++)
	{
		printf("Case #%d: ",test);
		Solve();
		printf("\n");
	}
	return 0; 
}