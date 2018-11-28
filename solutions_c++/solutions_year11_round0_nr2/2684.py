//#include <cstdlib>
//#include <cctype>
//#include <cstring>
//#include <cstdio>
//#include <cmath>
//#include <algorithm>
//#include <vector>
//#include <string>
//#include <iostream>
//#include <sstream>
//#include <map>
//#include <set>
//#include <queue>
//#include <stack>
//#include <fstream>
//#include <numeric>
//#include <iomanip>
//#include <bitset>
//#include <list>
//#include <stdexcept>
//#include <functional>
//#include <utility>
//#include <ctime>
//using namespace std;
//
//int T, CT=1, L, P, C;
//int main() {
//	//freopen("B-small-attempt0.in","r",stdin);
//    //freopen("B-small-attempt0.out","w",stdout);
//	//scanf("%d", &T);
//	cin>>T;
//	while(T--) {
//		scanf("%d %d %d", &L, &P, &C);
//
//		int ans = 0;
//		int TT = C;
//		while(L * C < P) {
//			L *= TT;
//			TT *= C;
//			++ans;
//		}
//		printf("Case #%d: %d\n", CT++, ans);
//
//	}
//	return 0;
//}


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

struct node
{
	char ch;
	int pos;
};
int work[28][28],aga[26];
void init()
{
		for(int i=0;i<28;i++)
			for(int j=0;j<28;j++)
				work[i][j] = -1;
		for(int i=0;i<26;i++)
			aga[i] = -1;
}
int main()
{
	freopen("B-small-attempt2.in","r",stdin);
    freopen("B-small-attempt2.out","w",stdout);
	int t;
	//scanf("%d",&t);
	cin >> t;
	for(int cases=1;cases<=t;cases++)
	{
		int c,d,n;
		char com[80][6],op[80][6];
		init();
		cin >>c;
		for(int i=0;i<c;i++)
		{
			cin >> com[i];
			work[com[i][0]-'A'][com[i][1]-'A'] = com[i][2] - 'A';
			work[com[i][1]-'A'][com[i][0]-'A'] = com[i][2] - 'A';
		}
		cin >> d;
		for(int i=0;i<d;i++)
		{
			cin >> op[i];
			aga[op[i][0]-'A'] = op[i][1] - 'A';
			aga[op[i][1]-'A'] = op[i][0] - 'A';
		}
		cin >> n;
		char ch;
		char v[1000];int cnt = 0;
		for(int i=0;i<n;i++)
		{
			cin >> ch;
			bool changed = true;
			v[cnt++] = ch;
			while(changed)
			{
				changed = false;
				if(cnt-2>=0 && work[v[cnt-1]-'A'][v[cnt-2]-'A']!=-1)
				{
					v[cnt-2] = work[v[cnt-1]-'A'][v[cnt-2]-'A'] + 'A';
					cnt = cnt -1;
					changed = true;
				}
				else
				{
				    bool find = false;
					for(int j=cnt-2;j>=0;j--)
					{
						if(aga[v[cnt-1]-'A'] == (v[j]-'A'))
						{
							find = true;
							cnt = 0;
							break;
						}
					}
				}
				if(changed==false)
					break;
			}
		}
		v[cnt] = '\0';
		int len = strlen(v);
		printf("Case #%d: [",cases);
		for(int i=0;i<len-1;i++)
			printf("%c, ",v[i]);
		if(len>=1)
			printf("%c",v[len-1]);
		printf("]\n");
	}
	return 0;
}
