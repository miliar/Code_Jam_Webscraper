#include <iostream>
#include <cstring>
using namespace std;

int main() {

int L, D, N, i, j, k, l, R;
char d[8192][16], p[512];
bool pos[32], v[8192];

cin >> L;
cin >> D;
cin >> N;

for (i=0; i<D; i++) {
   cin >> d[i];
}

for (l=1; l<=N; l++) {

cin >> p;

memset(v, true, sizeof(v)); j = 0;
for (i=0; i<L; i++) {
   memset(pos, false, sizeof(pos));
   if (p[j] != '(') {pos[p[j]-'a'] = true; j++;}
	else {
		j++;
	   while (p[j] != ')') {
		   pos[p[j]-'a'] = true;
			j++;
		}
		j++;
	}
	for (k=0; k<D; k++) {
	   if (pos[d[k][i]-'a'] == false) v[k] = false;
	}
}

R = 0;
for (k=0; k<D; k++) R += v[k];
cout << "Case #" << l << ": " << R << endl;

}

return 0;
}
