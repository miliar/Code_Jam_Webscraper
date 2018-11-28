#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

long min(long a, long b) {
	if (a < b)
		return a;
	return b;
}

int main() {
  long n, s, q;

  scanf("%ld\n", &n);

  for (long i = 0; i < n; i++) {
    scanf("%ld\n", &s);
	string st1[s];
    for (long j = 0; j < s; j++) {
		getline(cin, st1[j]);
    }

    scanf("%ld\n", &q);
	string st2[q];
	for (long j = 0; j < q; j++) {
		getline(cin, st2[j]);
	}
	
	
	long map[q][s];
	for (long j = 0; j < q; j++)
		for (long k = 0; k < s; k++)
			map[j][k] = 0;
	
	for (long k = 0; k < s; k++)
		if (st2[0].compare(st1[k]) == 0)
			map[0][k] = 1;
		else
			map[0][k] = 0;
			
	for (long j = 1; j < q; j++)
		for (long k = 0; k < s; k++) {
			if (st2[j].compare(st1[k]) == 0)
				map[j][k] = q+1;
			else
				map[j][k] = map[j-1][k];
				
			for (long l = 0; l < s; l++) {
				if (l == k)
					continue;
				map[j][k] = min(map[j-1][l] + 1, map[j][k]);
			}
		}

	long ans = q+1;
	for (long k = 0; k < s; k++)
		ans = min(ans, map[q-1][k]);
	if (q == 0)
		ans = 0;
	
	cout << "Case #" << i+1 << ": " << ans << endl; 
  }

  return 0;
}
