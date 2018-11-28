#include <cctype>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	
	char A[] = "yhesocvxduiglbkrztnwjpfmaq";
	char B[] = "abcdefghijklmnopqrstuvwxyz";
	char C[200];
	
	int T;
	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++) {
		gets(C);
		int N = strlen(C);
		
		printf("Case #%d: ", t);
		for (int i = 0; i < N; i++) {
			printf("%c", isalpha(C[i]) ? A[int(C[i] - 'a')] : C[i]);
		}
		printf("\n");
	}
	return 0;
}
