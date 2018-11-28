#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#include <algorithm>
#include <vector>
#include <limits.h>

using namespace std;

void init () {
}

int compression_ratio (char *s, vector<int> &numbers, int k) {
	char *str = strdup(s);

	for (int i = 0; i < strlen(s)/k; i++) {
		for (int j = 0; j < k; j++) {
			str[i*k+numbers[j]] = s[i*k+j];
		}
	}
	int count = 0;
	for (int i = 0; i < strlen(s); i++) {
		count ++;
		while (i+1 < strlen(s) && str[i+1] == str[i]) i++;
	}

	free (str);
	return count;

}

void solve (int _nn) {
	char str[1500];
	int k;
	scanf ("%d",&k);
	vector<int> numbers;
	for (int i = 0; i < k; i++)
		numbers.push_back (i);

	scanf ("%s",str);
	int result = INT_MAX;

	do {
		result = min(result, compression_ratio (str, numbers, k));
	} while (next_permutation(numbers.begin(), numbers.end()));
	printf ("Case #%d: %d\n",_nn,result);
}

int main () {
	int cases;

	scanf ("%d",&cases);
	for (int i = 1; i <= cases; i++)
		solve (i);
}
