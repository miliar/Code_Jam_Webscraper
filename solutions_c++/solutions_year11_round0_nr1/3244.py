#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

#define LEN 1000

int T,N;
char str[LEN];
char letters[100];
int nummers[100];
int blauw,oranje;
int btijd,otijd;

void update(char l, int t, int pos) {
	if (l == 'O') {
		otijd = t;
		oranje = pos;
	}
	else {
		btijd = t;
		blauw = pos;
	}
}

int nummer(char l) {
	if (l == 'O')
		return oranje;
	return blauw;
}

int vorigetijd(char l) {
	if (l == 'O')
		return otijd;
	return btijd;
}

int abs(int a) {
	if (a < 0)
		return (-a);
	return a;
}

void solve(int num) {
	blauw = 1;
	oranje = 1;
	int tijd = 0;
	btijd = 0;
	otijd = 0;
	char last = '\0';
	for (int i = 0; i < N; i++) {
		if (letters[i] == last) {
			tijd += abs(nummers[i] - nummer(letters[i])) + 1;
		}
		else {
			int a = abs(nummers[i] - nummer(letters[i]));
			int b = tijd - vorigetijd(letters[i]);
			//printf("  (a,b) = (%d,%d)\n", a,b);
			if (a <= b)
				tijd++;
			else
				tijd += (a-b) + 1;
		}
		update(letters[i],tijd,nummers[i]);
		last = letters[i];
		//printf("Tussenstand (%d): %d\n", i, tijd);
	}
	printf("Case #%d: %d\n", num, tijd);
}

int main() {
	fgets(str,LEN - 2,stdin);
	sscanf(str,"%d",&T);
	for (int i = 0; i < T; i++) {
		char* tmp;
		fgets(str,LEN - 2,stdin);
		tmp = strtok(str," ");
		sscanf(tmp,"%d",&N);
		for (int j = 0; j < N; j++) {
			char l;
			int k;
			tmp = strtok(NULL," ");
			sscanf(tmp,"%c",&l);
			tmp = strtok(NULL," ");
			sscanf(tmp,"%d",&k);
			letters[j] = l;
			nummers[j] = k;
		}
		solve(i + 1);
	}
	return 0;
}
