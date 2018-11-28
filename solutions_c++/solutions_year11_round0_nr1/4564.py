
#include <iostream>
using namespace std;

int n;
int an, bn;
int abut[200];
int bbut[200];
int but[400];
bool who[400];

int main()
{
#ifdef _DEBUG
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	char buf[10];

	for (int i = 0; i < t; i++) {
		printf("Case #%d: ", i+1);
		an = bn = 0;

		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			scanf("%s", buf);
			
			scanf("%d", but + i);

			if (buf[0] == 'O') {
				abut[an++] = but[i];
				who[i] = true;
			} else {
				bbut[bn++] = but[i];
				who[i] = false;
			}
		}

		int cura = 1, curb = 1;
		int ai = 0, bi = 0;
		int timer = 0;

		while(ai + bi < n) {
			bool lock = false;
			if (ai < an) {	//a try to move forwad				
				if (cura == abut[ai]) {	//can push
					if (who[ai+bi] == true) {//push the button
						ai++;
						lock = true;
					}	//else stay
				} else if  (cura > abut[ai]) {
					cura--;
				} else {
					cura++;
				}
			}

			if (bi < bn) {	//a try to move forwad				
				if (curb == bbut[bi]) {	//can push
					if (who[ai+bi] == false && lock == false) {//push the button
						bi++;
					}	//else stay
				} else if (curb > bbut[bi]) {
					curb--;
				} else {
					curb++;
				}
			}

			timer ++;
		}

		printf("%d\n", timer);
	}
	return 0;
}

