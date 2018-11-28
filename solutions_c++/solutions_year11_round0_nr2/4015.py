// a.cpp : Defines the entry point for the console application.
//

#include <iostream>

using namespace std;

char buf[1000];
char res[1000];
char combine[200][200];
bool oppose[200][200];
int m;

void checking() {

	if (m < 2)
		return;

	bool flag = false;
	while (m >= 2) {
	
		char com = combine[res[m-1]][res[m-2]];
		if (com != 0) {
			m -=2;
			res[m++] = com;
			res[m] = 0;
			flag = true;
		} 
		else
			break;
	}
	
	if (flag == false) {
		int i = 0;
		for (i = 0; i < m - 1; i++) {
			if (oppose[res[m-1]][res[i]]) {
				break;
			}
		}

		if (i < m - 1) {
			m = 0;
			res[m] = 0;
		}
	}
}

int main()
{
#ifdef _DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		printf("Case #%d: [", i+1);
		int nc;
		scanf("%d", &nc);
		memset(buf, 0, sizeof(buf));
		memset(oppose, 0, sizeof(oppose));
		memset(combine, 0, sizeof(combine));

		for (int i = 0; i < nc; i++) {
			scanf("%s", buf);
			combine[buf[0]][buf[1]] = buf[2];
			combine[buf[1]][buf[0]] = buf[2];
		}

		int nd;
		scanf("%d", &nd);

		for (int i = 0; i < nd; i++) {
			scanf("%s", buf);
			oppose[buf[0]][buf[1]] = true;
			oppose[buf[1]][buf[0]] = true;
		}

		int nn;
		scanf("%d", &nn);
		scanf("%s", buf);
		m = 0;

		for (int i = 0; i < nn; i++) {
			res[m++] = buf[i];
			res[m] = 0;
			checking();
		}

		for (int i =0 ; i < m; i++) {
			if (i)
				printf(", ");
			printf("%c", res[i]);
		}

		printf("]\n");
	}
	return 0;
}

