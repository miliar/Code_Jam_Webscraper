#include  "iostream" 
#include  "vector"
#include  "string"
#include  "string.h"
#include  "algorithm" 
#include  "sstream"
#include  "set"
#include  "map"
#include  "queue"
#include  "deque"
#include  "stack"
#include "list"
#include  "bitset"
#include  "cstdio"
#include  "assert.h"
#include  "cmath"
#include  "cstdlib"
#include  "ctime"
#include  "cfloat"
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define INF (1<<25)
int cases;
int main()
{
	
	freopen("Achi.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	scanf("%d",&cases);
	long long  n,k;
	for(int i=0;i<cases;i++)
	{
		//scanf("%d %d",&n,&k);
		cin>>n>>k;
		cout<<"Case #"<<i+1<<": ";
		long long num=(1LL<<n);
		if(k==0)
		{
			cout<<"OFF"<<endl;
			continue;
		}
		if((k+1)%num==0)
			cout<<"ON"<<endl;
		else
			cout<<"OFF"<<endl;
	}
	return 0;
}