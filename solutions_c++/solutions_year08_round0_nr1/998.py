#pragma warning(disable:4786)
#include<stdio.h>
#include<string>
#include<map>
using namespace std;

bool used[105];
int usecount;

map<string, int> sindex;
int n;
char str[200];
string sstr;

int main()
{
	int i, j;
	int t, nowt;
	int nq;
	int index;
	int switchcount;

	freopen("A-large.in.txt", "r", stdin);
	freopen("A-large.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t--) {
		nowt ++;

		sindex.clear();

		scanf("%d", &n);
		gets(str);
		for (i = 0; i < n; i ++) {
			gets(str);
//			sstr = str;
			sindex[str] = i;
		}

		for (i = 0; i < n; i ++) {
			used[i] = false;
		}
		usecount = 0;

		switchcount = 0;

		scanf("%d", &nq);
		gets(str);
		for (i = 0; i < nq; i ++) {
			gets(str);
			index = sindex[str];

			if (used[index] == false) {
				used[index] = true;
				usecount ++;
				if (usecount == n) {
					for (j = 0; j < n; j ++) {
						used[j] = false;
					}
					usecount = 0;

					switchcount ++;

					used[index] = true;
					usecount ++;
				}
			}
		}

		printf("Case #%d: %d\n", nowt, switchcount);
	}

	return 0;
}
