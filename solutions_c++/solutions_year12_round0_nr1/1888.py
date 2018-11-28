#include <iostream>
#include <cstdlib>

using namespace std;



int main () {
	char* decode[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
					  "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
					  "de kr kd eoya kw aej tysr re ujdr lkgc jv"
					 };
	char* encode[] = {"our language is impossible to understand",
					  "there are twenty six factorial possibilities",
					  "so it is okay if you want to just give up"
					 };
	char google_maps[255] = {0};
	char *googles_alpha = "ynficwlbkuomxsevzpdrjgthaq ",
		 *english_alpha = "abcdefghijklmnopqrstuvwxyz ";
	for(int i = 0; i <= 26; ++i) {
		google_maps[googles_alpha[i]] = english_alpha[i];
	}

	int  cases;
	char src[150], dst[150];
	cin.getline(src, sizeof(src));
	cases = atoi(src);
	for (int k = 1;k <= cases; ++k) {
		cin.getline(src, sizeof(src));
		int n = (int)strlen(src);
		dst[n] = '\0';
		for (int i = 0; i < n; ++i) {
			dst[i] = google_maps[src[i]];
		}
		cout << "Case #" << k << ": " << dst << endl;
	}
	return 0;
}