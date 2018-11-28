#include <iostream>
#include <string>

using namespace std;

string zod, ns;
int budas[20], used[20], best, k;

void bandyk() {
//	for (int j= 0 ; j < k; j++)
//		cout << budas[j] << " ";
//	cout << endl;
	int stab = -k;
	ns = "";
	for (int j = 0; j < zod.size(); j++) {
		if (j % k == 0) stab += k;
		int kel = j % k;
		ns = ns + zod[stab + budas[kel]];
//		cout << zod[stab+ budas[kel]]  << " ";
	}
//	cout << endl;
	int keic = 0;
	for (int r = 1; r < ns.size(); r++)
		if (ns[r] != ns[r - 1]) keic++;
	best = min(best, keic);
//	cout << "keic: " << keic << endl;
}

void perrink(int vt) {
	if (vt == k) bandyk();
		else for (int i = 0; i < k; i++) 
			if (!used[i]) {
				used[i] = true;
				budas[vt] = i;
				perrink(vt + 1);
				used[i] = false;
			}
}	
		 

int main() {
	freopen("dsmall.in", "r", stdin);
	freopen("dsmall.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &k);
		char buf[10000];
		best = 100000000;
		scanf(" %s", &buf);
		zod = buf;
//		cout << zod << " : " << endl;
		perrink(0);
		printf("Case #%d: %d\n", i + 1, best + 1);
	}	
	return 0;
}
