#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <math.h>

#define pb push_back

using namespace std;

int T,CC,DD,N;

vector<char> A;

char base[] = {'Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'};

char C[100][100];
char D[100][100];

char P[100];
char input[110];

void solve(int test) {
	int i,j;
	
	A.clear();	
	memset(P,0,100*sizeof(char));

	for (i=0; i<N; i++) {
		
		if (A.size() == 0) {
			A.pb(input[i]);
			P[input[i]]++;
			continue;
		}
		
		if (C[A[A.size()-1]][input[i]]) {
			char rem = A[A.size()-1];
			A.pop_back();
			P[rem] --;

			A.pb(C[rem][input[i]]);
			continue;
		}
		
		int ok = 0;
		for (j = 0; j < 8; j++) {
			if (D[base[j]][input[i]] == 1 && P[base[j]] > 0) {
				A.clear();
				memset(P,0,100*sizeof(char));
				ok = 1;
			}
		}
		
		if (ok) {
			continue;
		}
		
		A.pb(input[i]);
		P[input[i]]++;
	}
	
	printf("Case #%d: [", test+1);
	
	if (A.size())
		printf("%c", A[0]);
	
	for (i = 1; i< A.size(); i++) {
		printf(", %c", A[i]);
	}

	printf("]\n");
}

int main () {
	
	int i,j,val;
	char buf[10];
	
	scanf ("%d",&T);
	
	for (i =0; i < T; i++) {
		memset(C, 0, 100 * 100 * sizeof(char));
		memset(D, 0, 100 * 100 * sizeof(char));
		
		scanf("%d", &CC);
		
		for (j=0; j<CC; j++) {
			memset(buf, 0, 10);
			
			scanf("%s", buf);
			C[buf[0]][buf[1]] = buf[2]; 
			C[buf[1]][buf[0]] = buf[2]; 
		}
		
		scanf("%d", &DD);
		
		for (j=0; j<DD; j++) {
			memset(buf, 0, 10);
			
			scanf("%s", buf);
			D[buf[0]][buf[1]] = 1; 
			D[buf[1]][buf[0]] = 1; 
		}
		
		scanf("%d", &N);
		
		memset(input, 0, 110);
			
		scanf("%s", input);
		solve(i);
	}
	
}