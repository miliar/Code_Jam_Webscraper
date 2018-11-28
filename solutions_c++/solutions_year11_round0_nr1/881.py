#include <iostream>
#include <cstdio>
#include <memory>
#include <utility>
#include <algorithm>

using namespace std;

#define rep(x,y,z) for (int x=(y),e##x=(z);x<e##x;x++)

typedef pair<int,int> pii;

void test(int a)
{
	int n;
	cin>>n;
	pii A[101];
	rep(i,0,n)
		scanf(" %c %d",&A[i].first,&A[i].second);
	int O=1,P=1;
	int res=0;
	int lastO=0,lastP=0;
	int dvi;
	rep(i,0,n)
	{
		if (A[i].first=='O') 
		{
			dvi=res-lastO;
			res+=max(0,abs(O-A[i].second)-dvi)+1;
			O=A[i].second;
			lastO=res;
		}
		else 
		{
			dvi=res-lastP;
			res+=max(0,abs(P-A[i].second)-dvi)+1;
			P=A[i].second;
			lastP=res;
		}
		//res++;
	}
	printf("Case #%d: %d\n",a,res);
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	cin>>t;
	rep(i,0,t) test(i+1);
	return 0;
}