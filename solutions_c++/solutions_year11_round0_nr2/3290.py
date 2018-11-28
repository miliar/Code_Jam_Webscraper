#include <cstdio>
#include <cmath>
const int MAX_A = 30;
const int MAX_L = 111;
const int A = 'A' - 1;
using namespace std;
int N;
//A = 1, B = 2, C = 3 ....
char combine[MAX_A][MAX_A];	//combine[a][b] = the letter that is formed when a and b combine
bool opposed[MAX_A][MAX_A];	//opposed[a][b] = are a and b opposed?
int C, D, L;

int ind;
char final[MAX_L];

void printMagic() {
	printf("[");
	if(ind > 0) {
		for(int i = 1; i < ind; i++) {
			printf("%c, ", final[i]);
		}
		printf("%c", final[ind]);
	}
	printf("]\n");
}

void solve(int caseNum) {
	printf("Case #%d: ", caseNum);

	//Input combinations
	scanf("%d ", &C);
	for(int i = 1; i <= C; i++) {
		char a, b, c;
		scanf("%c%c%c ", &a, &b, &c);
		combine[a - A][b - A] = combine[b - A][a - A] = c;
	}

	//Input oppositions
	scanf("%d ", &D);
	for(int i = 1; i <= D; i++) {
		char a, b;
		scanf("%c%c ", &a, &b);
		opposed[a - A][b - A] = opposed[b - A][a - A] = true;
	}

	//Input element string
	scanf("%d ", &L);
	ind = 0;	//ind is the length of our answer
	for(int i = 1; i <= L; i++) {
		ind++;
		scanf("%c", &final[ind]);
		if(combine[final[ind] - A][final[ind - 1] - A] != 0) {
			final[ind - 1] = combine[final[ind] - A][final[ind - 1] - A];
			ind--;
		} else {
			for(int j = 1; j < ind; j++) {
				if(opposed[final[j] - A][final[ind] - A]) {
					ind = 0;
					break;
				}
			}
		}
	}

	printMagic();
	for(int i = 1; i <= 27; i++) for(int j = 1; j <= 27; j++) combine[i][j] = opposed[i][j] = 0;
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
