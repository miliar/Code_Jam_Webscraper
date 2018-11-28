#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

static void solve() {
	/* 1 <= x <= 10**20 */
	char text[100]; scanf("%s", text);
	char *Z = text;
	while(*Z == '0') Z++;

	vector<int> digits;
	while(*Z) {
		digits.push_back(*Z - '0');
		Z++;
	}
	/* digits [0] -> najstarsza cyfra */

	bool are_sorted_rev = true;
	for(int i=1; i<(int)digits.size(); i++) {
		are_sorted_rev = are_sorted_rev && (digits[i-1] >= digits[i]);
	}

	if(are_sorted_rev) {
		int smallest = -1;
		for(int i=0; i<(int)digits.size(); i++) {
			if(digits[i] == 0) continue;
			if(smallest == -1 || digits[i] < digits[smallest])
				smallest = i;
		}
		swap(digits[0], digits[smallest]);
		sort(digits.begin()+1, digits.end());
		digits.insert(digits.begin()+1, 0);
	} else {
		int j, maxDig = 0;
		for(j=(int)digits.size()-1; j>=0; j--) {
			maxDig = max(maxDig, digits[j]);
			if(digits[j] < maxDig) {
				break;
			}
		}
		/* okej - j to miejsce zmiany cyfry */
		/* znajdź na co zmienić */
		int swI = -1;
		for(int i=j+1; i<(int)digits.size(); i++) {
			if(digits[i] <= digits[j])
				continue; // za małe
			if(swI != -1 && digits[swI] < digits[i])
				continue; // za duże
			swI = i;
		}
		swap(digits[j], digits[swI]);
		sort(digits.begin() + (j+1), digits.end());
	}

	//printf("%s -> ", text);
	for(int i=0; i<(int)digits.size(); i++) {
		printf("%c", '0' + digits[i]);
	}
	printf("\n");
}

int main() {
	int _Nc; scanf("%d", &_Nc);
	for(int _Ni=1; _Ni<=_Nc; _Ni++) {
		printf("Case #%d: ", _Ni);
		solve();
	}
	return 0;
}
