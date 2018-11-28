#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <deque>
#include <algorithm>
#include <cmath>

using namespace std;

struct Word {
	char str[16];
};

int main()
{
	int L, D, N;
	cin>>L;
	cin>>D;
	cin>>N;
	std::vector<Word> words(D);
	for (int i=0;i<D;++i) {
		scanf("%s", words[i].str);
	}

	for (int i = 0;i<N;i++)
	{
		char pattern[1024];
		scanf("%s", pattern);

		std::vector<int> match(D, 0);

		char *p=pattern;
		for (int j=0; j<L && *p != 0; ++j) {
			if (*p == '(') {
				++p;
				while (*p != ')') {
					for (int w=0;w<D;++w) {
						if (match[w] == j && *p == words[w].str[j]) {
							++match[w];
						}
					}

					++p;
				}
			} else {
				for (int w=0;w<D;++w) {
					if (match[w] == j && *p == words[w].str[j]) {
						++match[w];
					}
				}
			}

			++p;
		}

		printf("Case #%d: %d\n", i+1, std::count(match.begin(), match.end(), L));
	}

	return 0;
}
