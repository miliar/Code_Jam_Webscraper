#pragma warning(disable:4786)
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<functional>
#include<string>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<utility>
#include<fstream>
#include<sstream>
#include<cmath>
#include<stack>
#include<cstdio>
#include <iomanip>


using namespace std;

#define MEM(a,b) memset(a,(b),sizeof(a))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b)  ((a) < (b) ? (a) : (b))
#define istr(S) istringstream sin(S)
#define MP make_pair
#define pb push_back
#define inf 1000000000

typedef pair<int,int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<pi> vpi;

#define inf 1000000000
//typedef long long LL;
//typedef __int64 LL;

int main()
{
	int i,j,k,tests,cs=0,n;
	
	freopen("D:\\gcj\\A-large.in","r",stdin);
	freopen("D:\\gcj\\Alarge.out","w",stdout);

	scanf("%d",&tests);
	while(tests--)
	{
		scanf("%d%d",&n,&k);

		int ans=0;
		j=n-1;

		int ok=1;

		for(i=0;i<n;i++)
			if(!(k&(1<<i))) ok=0;

		printf("Case #%d: ",++cs);
		if(ok)
			puts("ON");
		else
			puts("OFF");



	}
	//printf("Case #%d: ",++cs);

	return 0;
} 


