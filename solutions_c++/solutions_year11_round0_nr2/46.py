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


int main()
{
	//freopen("B.in","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
	//freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	for (int case_id=1;case_id<=testcase;case_id++)
	{
		char C[256][256];
		bool D[256][256];
		memset(C,255,sizeof(C));
		memset(D,false,sizeof(D));
		int nC,nD,n,L;
		char r[1024],s[1024];
		for (scanf("%d",&nC);nC>0;nC--)
		{
			scanf("%s",s);
			C[s[0]][s[1]]=s[2];
			C[s[1]][s[0]]=s[2];
		}
		for (scanf("%d",&nD);nD>0;nD--)
		{
			scanf("%s",s);
			D[s[0]][s[1]]=true;
			D[s[1]][s[0]]=true;
		}
		scanf("%d%s",&n,s);
		L=0;
		for (int i=0;i<n;i++)
		{
			r[L++]=s[i];
			for (;L>=2 && C[r[L-2]][r[L-1]]>=0;L--)
				r[L-2]=C[r[L-2]][r[L-1]];
			bool op=false;
			for (int a=0;a<L;a++) for (int b=a+1;b<L;b++)
				if (D[r[a]][r[b]])
					op=true;
			if (op)
				L=0;
		}
		printf("Case #%d: ",case_id);
		printf("[");
		for (int i=0;i<L;i++)
		{
			if (i>0)
				printf(", ");
			printf("%c",r[i]);
		}
		printf("]\n");
	}
	return 0;
}
