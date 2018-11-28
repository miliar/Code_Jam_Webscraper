#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

#define VAR(i,v) __typeof(v)i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin()); i!=(v).end(); i++)

static vector< vector<int> > where;

int main() {
	const char *text = "welcome to code jam";
	{
		where.resize(256);
		for(int i=0; text[i]; i++) {
			where[text[i]].push_back(i);
		}
	}

	char line[1000];
	line[sizeof(line)-1] = 0;
	fgets(line, sizeof(line)-1, stdin);

	int T; sscanf(line, "%d", &T);
	for(int t=0; t<T; t++) {
		vector<int> num;
		num.resize(strlen(text)+1);
		num[0] = 1;

		fgets(line, sizeof(line)-1, stdin);

		const char *z = line;
		while(*z) {
			const vector<int> &pos = where[*z];
			z++;

			FOREACH(w, pos) {
				num[*w + 1] += num[*w];
				num[*w + 1] %= 10000;
			}
		}

		printf("Case #%d: %04d\n", t+1, num[strlen(text)]);
	}
}

