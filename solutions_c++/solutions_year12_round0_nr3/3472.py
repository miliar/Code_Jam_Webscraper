#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
using namespace std;

int len(int n)
{
    int l = 0;
    while (n != 0) {
          n /= 10;
          l += 1;     
    }
    return l;
}

int main () {
    ofstream fout ("test.out");
    ifstream fin ("C-small-attempt0.in");
    
	int T, t, A, B, i, j, k, l, ans;
	int r[200010], n[200010];

	for (i = 1; i <= 200010; i++)
		r[i] = 0;

	for (i = 1; i <= 200010; i++) 
		if (r[i] == 0) {
			r[i] = i;
			l = len(i); k = i;
			for (j = 1; j < l; j++) {
				k = k / 10 + (k % 10) * ((int)(pow(10.0, l - 1)));
				if (len(k) == l && k <= 200010)
					r[k] = i;
			}
		}
    fin >> T;
	for (t = 1; t <= T; t++) {
		for (i = 1; i <= 200000; i++)
			n[i] = 0;
		fin >> A >> B;
		for (i = A; i <= B; i++)
			n[r[i]] += 1;
		ans = 0;
		for (i = 1; i <= B; i++) {
			if (n[i] > 1)
               ans += n[i] * (n[i] - 1) / 2;
        }
		fout << "Case #" << t << ": " <<ans << endl;
	}
    
    return 0;
}
