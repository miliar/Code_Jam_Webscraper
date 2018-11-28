#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int main(void) {
	FILE *in = fopen("B-large.in", "r");
	FILE *out = fopen("out3.out", "w");
	int T;
	fscanf(in, "%d", &T);
	char buf[100];
	fgets(buf, 100, in);
	for (int i = 0; i < T; i++) {
		fprintf(out, "Case #%d: ", i+1);
		fgets(buf, 100, in);
		int n = strlen(buf);
		if (n && buf[n-1] == '\n')
			buf[--n] = 0;
		map<int, int> digits;
		int ok = 0;
		for (int j = n-1; j >= 0; j--) {
			digits[buf[j]]++;
			if ((*(digits.rbegin())).first > buf[j]) {
				int zamena = (*(digits.upper_bound(buf[j]))).first;
				buf[j] = zamena;
				digits[zamena]--;
				for (map<int,int>::iterator it = digits.begin(); it != digits.end(); it++)
					for (int l = 0; l < it->second; l++)
						buf[++j] = it->first;
				fprintf(out, "%s\n", buf);
				ok = 1;
				break;
			}
		}
		if (!ok) {
			int zamena = (*(digits.begin())).first;
			if (zamena == '0') {
				map<int,int>::iterator it = digits.begin();
				it++;
				zamena = it->first;
			}
			int j = 0;
			buf[j] = zamena;
			digits[zamena]--;
			buf[++j] = '0';
			for (map<int,int>::iterator it = digits.begin(); it != digits.end(); it++)
				for (int l = 0; l < it->second; l++)
					buf[++j] = it->first;
			buf[++j] = 0;
			fprintf(out, "%s\n", buf);
		}
	}
	fclose(out);
	fclose(in);
}
