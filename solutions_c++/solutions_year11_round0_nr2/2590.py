#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#define MAX 105

using namespace std;

char lista[MAX];
int ult;
char form[30][30];
bool dest[30][30];
int N;

int main(){
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
		ult = 0;
		for (int i = 0; i < 30; i++)
			for (int j = 0; j < 30; j++){
				form[i][j] = 30;
				dest[i][j] = false;
			}
		int x;
		scanf ("%d", &x);
		for (int i = 0; i < x; i++){
			char str[10];
			scanf (" %s", str);
			form[str[0]-'A'][str[1]-'A'] = form[str[1]-'A'][str[0]-'A'] = str[2];
		}
		scanf ("%d", &x);
		for (int i = 0; i < x; i++){
			char str[10];
			scanf (" %s", str);
			dest[str[0]-'A'][str[1]-'A'] = dest[str[1]-'A'][str[0]-'A'] = true;
		}
		scanf ("%d", &N);
		for (int i = 0; i < N; i++){
			char c;
			scanf (" %c", &c);
			if (ult > 0 && form[c-'A'][lista[ult-1]-'A'] != 30)
				lista[ult-1] = form[c-'A'][lista[ult-1]-'A'];
			else {
				lista[ult++] = c;
				for (int j = ult-1; j >= 0; j--)
					if (dest[c-'A'][lista[j]-'A']){
						ult = 0;
						break;
					}
			}
		}
		printf ("Case #%d: [", t);
		for (int i = 0; i < ult; i++){
			if (i > 0)
				printf (", ");
			printf ("%c", lista[i]);
		}
		printf ("]\n");
	}
	return 0;
}
