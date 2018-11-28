#define _CRT_SECURE_NO_WARNINGS
#include <ctime>
#include <cfloat>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
#define pb push_back
#define L(s) (int)(s).size()5
#define rp(i,n) for(int (i)=0;(i)<(n);++(i))
#define fr(i,st,fn) for(int (i)=(st);(i)<=(fn);++(i))
#define VI vector<int>
#define inf 1000000000
#define ll long long
#define C(a) memset((a),0,sizeof((a)))
#define all(s) (s).begin(),s.end()
#define pi 3.1415926535897932384626433832795
#define pii pair<int,int>
#define mp make_pair
//#define x first
//#define y second
int n,k;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int ts;
	scanf("%d",&ts);
	for(int test=1;test<=ts;++test)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",test);
		if ((k+1)%(1<<n)==0)
			printf("ON\n");
		else
			printf("OFF\n");
	}
}