#include <string>
#include <vector>
using namespace std;
bool pattern[16][32];

int main() {
	FILE *fi = fopen("a.in", "r");
	FILE *fo = fopen("a.out", "w");
	int L, D, N;
	fscanf(fi, "%d%d%d", &L, &D, &N);

	char word[1024];
	fgets(word, 1024, fi);
	vector<string> dict;
	for (int i=0; i<D; i++) {
		fgets(word, 1024, fi);
		dict.push_back(string(word));
	}

	for (int testCase=0; testCase<N; testCase++) {
		for (int i=0; i<16; i++)
			for (int j=0; j<32; j++)
				pattern[i][j] = false;
		fgets(word, 1024, fi);
		int j = 0;
		for (int i=0; i<L; i++) {
			if (word[j]=='(') {
				while (word[++j]!=')')
					pattern[i][word[j]-'a'] = true;
			} else
				pattern[i][word[j]-'a'] = true;
			j++;
		}

		int counter = 0;
		for (int wi=0; wi<D; wi++) {
			bool ok = true;
			for (int i=0; i<L && ok; i++)
				if (!pattern[i][dict[wi][i]-'a'])
					ok = false;
			if (ok)
				counter++;
		}
		fprintf(fo, "Case #%d: %d\n", testCase+1, counter);
	}

	fclose(fo);
	fclose(fi);
	return 0;
}
