#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

char combine[300][300];
bool oppose[300][300];

int main()
{
//	freopen("-small-attempt2.in", "rt", stdin);
//	freopen("output.txt", "wt", stdout);
	int test, i;
//	scanf("%d", &test);
	fin >> test;
	for (int t=1; t<=test; ++t) {
		int com, opp;
		char a, b, c;
		memset(combine, 0, sizeof combine);
		memset(oppose, 0, sizeof oppose);
		//scanf("%d", &com);
		fin >> com;
		for (i=0; i<com; ++i) {
			//scanf("%c%c%c", &a, &b, &c);
			fin >> a >> b >> c;
			combine[a][b] = combine[b][a] = c;
		}
//		scanf("%d", &opp);
		fin >> opp;
		for (i=0; i<opp; ++i) {
			//scanf("%c%c", &a, &b);
			fin >> a >> b;
			oppose[a][b] = oppose[b][a] = true;
		}
		int len;
//		scanf("%d", &len);
		fin >> len;
		string ans = "";
	//	scanf("%c", &a);
	//	scanf("%c", &a);
		fin >> a;
		ans += a;
		for (i=1; i<len; ++i) {
			//scanf("%c", &a);
			fin >> a;
			if (combine[a][ans[ans.size() - 1]]) {
				ans[ans.size() - 1] = combine[a][ans[ans.size() - 1]];
			} else {
				bool opp = false;
				int sz = ans.size();
				for (int l=0; l<sz; ++l) {
					if (oppose[ans[l]][a]) {
						opp = true;
						break;
					}
				}
				if (opp) {
					ans = "";
				} else ans += a;
			}
		}
		if (ans.size()) {
//			printf("Case #%d: [%c", t, ans[0]);
			fout << "Case #" << t << ": [" << ans[0];
			for (int k=1; k<ans.size(); ++k) 
				fout << ", " << ans[k];
				//	printf(", %c", ans[k]);
//			printf("]\n");
			fout << "]" << endl;
		} else {
//			printf("Case #%d: []\n", t);
			fout << "Case #" << t << ": []" << endl;
		}
	}
	
	return 0;
}