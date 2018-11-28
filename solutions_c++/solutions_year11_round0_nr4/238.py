#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
#include<cstring>
#include<string>
#include<sstream>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<ctime>
#include<cstdlib>
#include<cmath>
#include<cassert>
using namespace std;

typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef pair<int,int> pii;
typedef long long ll;

#define I ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i = a ; i <= b ; i++)
#define REV(i,a,b) for(int i = a ; i >= b ; i--)
#define REP(i,n) for(int i = 0 ; i < n ; i++)

#define INF 1000000000

int main()
{
	int t;
	cin>>t;
	int cas=0;
	while(t--)
	{
		cas++;
		int n;
		cin>>n;
		int ans = 0;
		FOR(i,1,n)
		{
			int temp;
			cin>>temp;
			if(temp != i)
				ans++;
		}
		cout<<"Case #"<<cas<<": "<<ans<<endl;
	}
	return 0;
}
