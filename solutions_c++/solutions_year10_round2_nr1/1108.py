#include <stdio.h>
#include <vector>
#include <list>
#include <string>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

vector<string> split(string str, string delim)
{
	vector<string> result;
	int cutAt;
	while ((cutAt = str.find_first_of(delim)) != str.npos) {
		if (cutAt > 0) {
			result.push_back(str.substr(0, cutAt));
		}
		str = str.substr(cutAt + 1);
	}
	if (str.length() > 0) {
        result.push_back(str);
    }
	return result;
}

struct directory {
	std::map<string, directory> childs;
};

int main(int argc, char* argv[])
{
	FILE* fp = fopen(argv[1], "r");
	if (!fp) return 1;

	int T;
	fscanf(fp, "%d\n", &T);

	std::set<string> input;
	char s[1024];
	for (int line = 1; line <= T; line++) {
		int N, M;
		fscanf(fp, "%d %d\n", &N, &M);

#if 1
		input.clear();
		for (int i = 0; i < N; i++) {
			fgets(s, sizeof(s), fp);
			s[strlen(s) - 1] = '\0';
			input.insert(s);
		}

		directory root;
		for (std::set<string>::const_reverse_iterator in = input.rbegin(); in != input.rend(); ++in) {
			directory* pnext = &root;
			vector<string> v = split(*in, "/");
			for (vector<string>::const_iterator it = v.begin(); it != v.end(); ++it) {
				if (pnext->childs.find(*it) == pnext->childs.end()) {
					pnext->childs[*it] = directory();
				}
				pnext = &pnext->childs[*it];
			}
		}

		input.clear();
		for (int i = 0; i < M; i++) {
			fgets(s, sizeof(s), fp);
			s[strlen(s) - 1] = '\0';
			input.insert(s);
		}

		int result = 0;
		for (std::set<string>::const_reverse_iterator in = input.rbegin(); in != input.rend(); ++in) {
			directory* pnext = &root;
			vector<string> v = split(*in, "/");
			for (vector<string>::const_iterator it = v.begin(); it != v.end(); ++it) {
				if (pnext->childs.find(*it) == pnext->childs.end()) {
					pnext->childs[*it] = directory();
					result++;
				}
				pnext = &pnext->childs[*it];
			}
		}
#else
		directory root;
		for (int i = 0; i < N; i++) {
			directory* pnext = &root;
			fgets(s, sizeof(s), fp);
			s[strlen(s) - 1] = '\0';
			vector<string> v = split(s, "/");
			for (vector<string>::const_iterator it = v.begin(); it != v.end(); ++it) {
				if (pnext->childs.find(*it) == pnext->childs.end()) {
					pnext->childs[*it] = directory();
				}
				pnext = &pnext->childs[*it];
			}
		}

		int result = 0;
		for (int i = 0; i < M; i++) {
			directory* pnext = &root;
			fgets(s, sizeof(s), fp);
			s[strlen(s) - 1] = '\0';
			vector<string> v = split(s, "/");
			for (vector<string>::const_iterator it = v.begin(); it != v.end(); ++it) {
				if (pnext->childs.find(*it) == pnext->childs.end()) {
					pnext->childs[*it] = directory();
					result++;
				}
				pnext = &pnext->childs[*it];
			}
		}
#endif

		printf("Case #%d: %d\n", line, result);
	}

	fclose(fp);
}
