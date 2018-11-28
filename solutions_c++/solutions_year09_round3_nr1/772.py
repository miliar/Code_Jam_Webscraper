#include <iostream>
#include <cmath>

using namespace std;

long long ats;
int buvo[200], t;
char buf[200];
int vt ;

int idek(int kur) {
	if (vt == -1) vt = 1;
		else if (vt == 1) vt = 0;
				else if (vt == 0) vt = 2;
						else vt++;
	return vt;
}	

int main() {
	freopen("small.in", "r", stdin);
	freopen("small.out", "w", stdout);
	scanf("%d", &t);
	for (int x = 1; x <= t; x++) {
		fill(buvo, buvo + 150, -1);
		scanf(" %s", &buf);
		vt = -1;
		int ilg = 0;
		for (int g = 0; buf[g] != '\0'; g++) {
			if (buvo[buf[g] - '0'] == -1) buvo[buf[g] - '0'] = idek(buf[g] - '0');
			ilg++;
		}
		ilg--;
		ats = 0;
		int yra, zr = 0;
		if (vt == 0) yra = 2;
			else yra = vt + 1;
		for (; ilg >= 0; ilg--, zr++) 
			ats = ats + pow((double)yra, (double)ilg) * buvo[buf[zr] - '0'];
		printf("Case #%d: %d\n", x, ats);	
	}
	return 0;
}
