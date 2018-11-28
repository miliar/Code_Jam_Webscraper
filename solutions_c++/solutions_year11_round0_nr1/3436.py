#include <cstdio>
#include <cmath>
#include <queue>
#define OrangeTurn 0
#define BlueTurn 1
const int MAX_C = 111;
using namespace std;
int N, C;

int indA, indO, indB, maxA, maxO, maxB;
int OrangeC[MAX_C], BlueC[MAX_C];
bool AllC[MAX_C];

void solve(int caseNum) {
	printf("Case #%d: ", caseNum);
	scanf("%d ", &C);
	maxA = maxO = maxB = indA = indO = indB = 1;
	for(int i = 1; i <= C; i++) {
		char a;
		int b;
		scanf("%c %d ", &a, &b);
		if(a == 'O') {
			OrangeC[maxO++] = b;
			AllC[maxA++] = OrangeTurn;
		} else if(a == 'B') {
			BlueC[maxB++] = b;
			AllC[maxA++] = BlueTurn;
		}
	}
	int bPos = 1, oPos = 1, t = 1;
//	printf("At time %d, O is at %d, B is at %d\n", t, oPos, bPos);
	while(1) {
		bool pushed = false;
		if(indB < maxB) {
			if(bPos == BlueC[indB]) {
				if(AllC[indA] == BlueTurn) {
					//Push button
					indA++;
					indB++;
					pushed = true;
//					printf("B push\t");
					if(indA > C) break;	//End of commands
				}
				//Do nothing otherwise
			} else {
				//Move towards next button
				if(bPos < BlueC[indB]) {
					bPos++;
				} else if(bPos > BlueC[indB]) {
					bPos--;
				}
			}
		}
		if(indO < maxO) {
			if(oPos == OrangeC[indO]) {
				if(AllC[indA] == OrangeTurn && !pushed) {
					//Push button
					indA++;
					indO++;
//					printf("O push\t");
					if(indA > C) break;	//End of commands
				}
				//Do nothing otherwise
			} else {
				//Move towards next button
				if(oPos < OrangeC[indO]) {
					oPos++;
				} else if(oPos > OrangeC[indO]) {
					oPos--;
				}
			}
		}
		t++;
//		printf("At time %d, oPos = %d(%d), bPos = %d(%d), (indA = %d, looking on %d side)\n", t, oPos, indO, bPos, indB, indA, AllC[indA]);
	}
	printf("%d\n", t);
	return;
}

int main() {
	freopen("small.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) solve(i);

	freopen("large.txt", "r", stdin);
	freopen("largeout.txt", "w", stdout);
	scanf("%d", &N);
	for(int i = 1; i <= N; i++) solve(i);
	return 0;
}
