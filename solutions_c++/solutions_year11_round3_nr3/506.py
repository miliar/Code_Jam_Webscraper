#include <cstdio>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <complex>
#include <string>
#include <cstring>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <functional>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef long double ld;
typedef pair<int,int> pii;
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)

const double PI=acos(-1.0);

template<class T> inline T SQR(T a){return a*a;}

#define __small
//#define __large

void test(int T)
{
	
	int n,L,H;
	cin>>n>>L>>H;
	int ans=0;
	int A[101];
	rep(i,0,n)
	{
		scanf("%d",A+i);
	}
	rep(j,L,H+1)
	{
		bool ok=true;
		rep(i,0,n)
			if (A[i]%j!=0 && j%A[i]!=0) ok=false;
		if (ok)
		{
			ans=j;
			break;
		}
	}
	printf("Case #%d: ",T);
	if (ans==0) puts("NO");
	else printf("%d\n",ans);

	
}

int main()
{
#ifdef __small
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-out.txt","w",stdout);
#endif
#ifdef __large
	freopen("C-large.in","r",stdin);
	freopen("C-large-out.txt","w",stdout);
#endif

	int t;
	cin>>t;
	rep(i,0,t)
		test(i+1);
	return 0;	
}
/*

1
4 1
2
4


2
4 1
2
4
8 3
1 1 4
3 7 7
*/