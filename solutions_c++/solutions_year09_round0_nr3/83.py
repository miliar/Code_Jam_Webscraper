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
#define MOD (10000)
 
using namespace std;

char target[]="welcome to code jam";
int limit;
string S;
int dp[20][1001];
int solve(int p1, int p2)
{
	//cout<<p1<<" "<<p2<<endl;
	if(p1==limit)
		return 1;
	if(p2>=S.size())
		return 0;
	int &ret=dp[p1][p2];
	if(ret!=-1)
		return ret;
	ret=0;
	if(target[p1]!=S[p2])
	{
		ret+=solve(p1,p2+1);
		ret%=MOD;
	}
	else
	{
		ret+=solve(p1,p2+1);
		ret%=MOD;
		ret+=solve(p1+1,p2+1);
		ret%=MOD;
	}
	return ret;
}
string display(int N)
{
	string s;
	for(int i=0;i<4;i++)
	{
		s.push_back('0'+N%10);
		N/=10;
	}
	reverse(ALL(s));
	return s;
}
int main()
{
	int N;
	int cas=1;
	limit=19;
	cin>>N;
	char buff[1001];
	fgets(buff,sizeof(buff),stdin);
	while(N--)
	{
		fgets(buff,sizeof(buff),stdin);
		string s(buff);
		S=s;
		SETF(dp);
		int ans=solve(0,0);
		cout<<"Case #"<<cas<<": "<<display(ans)<<endl;
		cas++;
	}
	return 0;
}
