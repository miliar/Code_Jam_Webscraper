#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(A,B) make_pair(A,B)
typedef pair<int,int> ipair;

int main()
{
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		multiset<int> Q[2];
		vector<ipair> W;
		int nA,nB,T;
		char s1[20],s2[20];
		scanf("%d%d%d",&T,&nA,&nB);
		for (int i=0;i<nA;i++)
		{
			scanf("%s%s",s1,s2);
			s1[2]=s2[2]=' ';
			int h1,m1,h2,m2;
			sscanf(s1,"%d%d",&h1,&m1);
			sscanf(s2,"%d%d",&h2,&m2);
			int t1=h1*60+m1;
			int t2=h2*60+m2;
			W.push_back(MP(t1,t2*2+0));
		}
		for (int i=0;i<nB;i++)
		{
			scanf("%s%s",s1,s2);
			s1[2]=s2[2]=' ';
			int h1,m1,h2,m2;
			sscanf(s1,"%d%d",&h1,&m1);
			sscanf(s2,"%d%d",&h2,&m2);
			int t1=h1*60+m1;
			int t2=h2*60+m2;
			W.push_back(MP(t1,t2*2+1));
		}
		sort(W.begin(),W.end());
		int R[2];
		R[0]=R[1]=0;
		for (int k=0;k<SIZE(W);k++)
		{
			int t1=W[k].first;
			int t2=W[k].second/2;
			int id=W[k].second%2;
			if (SIZE(Q[id])==0 || *Q[id].begin()>t1) R[id]++,Q[id].insert(t1);
			Q[id].erase(Q[id].begin());
			Q[1-id].insert(t2+T);
		}
		printf("Case #%d: %d %d\n",caseId,R[0],R[1]);
	}
	return 0;
}