#include <cstdio>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int AlianLanguage(vector <string> words, string pattern)
{
	vector <string> p;
	int ptr = 0;
	for (int i = 0; i < words[0].size(); i++) {
		if (pattern[ptr] == '(') {
			int next = pattern.find(')', ptr);
			p.push_back(pattern.substr(ptr + 1, next - ptr - 1));
			ptr = next + 1;
		} else {
			p.push_back(pattern.substr(ptr, 1));
			ptr++;
		}
	}
	//printf("%s %s %s\n", p[0].c_str(), p[1].c_str(), p[2].c_str());

	int ret = 0;
	for (int i = 0; i < words.size(); i++) {
		int j;
		for (j = 0; j < words[0].size(); j++) {
			//printf("%c-%s : ", words[i][j], p[j].c_str());
			if (p[j].find(words[i][j]) == string::npos) {
				break;
			}
		}
		if (j == words[0].size()) {
			ret++;
		}
	}
	return ret;
}


int main()
{
	char inp[999];

	int L, D, N;
	gets(inp); sscanf(inp, "%d%d%d", &L, &D, &N);

	vector <string> words(D);
	for (int i = 0; i < D; i++) {
		gets(inp); stringstream ss(inp); ss >> words[i];
	}

	for (int caseno = 1; caseno <= N; caseno++) {
		string pattern;
		gets(inp); stringstream ss(inp); ss >> pattern;
		printf("Case #%d: %d\n", caseno, AlianLanguage(words, pattern));
	}

	return 0;
}

