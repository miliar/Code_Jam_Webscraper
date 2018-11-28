#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
using namespace std;

int n;

char finalnum[40][20] = {
"001",
"005",
"027",
"143",
"751",
"935",
"607",
"903",
"991",
"335",
"047",
"943",
"471",
"055",
"447",
"463",
"991",
"095",
"607",
"263",
"151",
"855",
"527",
"743",
"351",
"135",
"407",
"903",
"791",
"135",
"647"
};

int main()
{
	int i, j, k;
	int t;
	int nowt;

	freopen("C-small-attempt0.in.txt", "r", stdin);
//	freopen("C-small-attempt0.out.txt", "w", stdout);

	scanf("%d", &t);
	nowt = 0;

	while (t--) {
		nowt ++;

		scanf("%d", &n);
		printf("Case #%d: %s\n", nowt, finalnum[n]);
	}

	return 0;
}



