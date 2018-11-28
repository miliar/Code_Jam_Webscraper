#include<stdio.h>
#include<vector>
#include<utility>
using namespace std;

#define MAX(A,B) ((A)>(B)?(A):(B))
#define ABS(A) ((A)>0?(A):(-(A)))

typedef pair<int,int> PII;
vector<PII> B,O;
int ans[200];
char word[10];

int main()
{
	int ks,T,N,i,o,b,szo,szb,a;

//	freopen("A-small-attempt0.in","r",stdin);
//	freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	scanf("%d",&T);
	for(ks=1;ks<=T;ks++)
	{
		scanf("%d",&N);
		B.clear(); O.clear();
		B.push_back(PII(0,1));
		O.push_back(PII(0,1));
		ans[0] = 0;
		for(i=1;i<=N;i++)
		{
			scanf("%s%d",word,&a);
			if(word[0]=='O') O.push_back(PII(i,a));
			else B.push_back(PII(i,a));
		}

		o = b = 1;
		szo = O.size();
		szb = B.size();
		while(o<szo || b<szb)
		{
			if(b!=szb && (o==szo || B[b].first < O[o].first))
			{
				ans[B[b].first] = 1 + MAX(ABS(B[b-1].second-B[b].second) + ans[B[b-1].first], ans[O[o-1].first]);
				b++;
				continue;
			}

			if(o!=szo && (b==szb || B[b].first > O[o].first))
			{
				ans[O[o].first] = 1 + MAX(ABS(O[o-1].second-O[o].second) + ans[O[o-1].first] , ans[B[b-1].first]);
				o++;
				continue;
			}
		}

		printf("Case #%d: %d\n",ks,ans[N]);
	}

	return 0;
}