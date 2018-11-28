#include <cstdio>
#include <cstring>
#include <set>
#include <utility>
#include <algorithm>
using namespace std;

typedef pair<int,int> pi;
set<pi> st;

void gen (int i, int l, int r)
{
	char s[200], ns[200];
	itoa(i,s,10);
	int k=strlen(s);
	for (int j=1;j<k;++j)
	{
		for (int ic=j;ic<k;++ic) ns[ic-j]=s[ic];
		for (int ic=0;ic<j;++ic) ns[k-j+ic]=s[ic];
		ns[k]=0;
		int t = atoi(ns);
		if (i<t&&t<=r) st.insert(pi(i,t));
	}
}

int main ()
{
	int l,r,tk;
	scanf("%d",&tk);
	for (int i=1; i<=tk; ++i)
	{
		st.clear();
		scanf("%d%d", &l,&r);
		for (int i=l; i<=r; ++i)
			gen(i,l,r);
		printf("Case #%d: %d\n",i,st.size());
	}
}
