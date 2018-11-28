#include <stdio.h>
#include <map>
#include <vector>
using namespace std;
#define LENGTH 19

char *wel = "welcome to code jam";
vector<int> count[LENGTH + 1];
multimap<char, int> letter;
char line[501];

int main() {
	int casa;
	scanf("%d", &casa);
	for(int i = 0; wel[i] != '\0'; i++) {
		letter.insert(make_pair(wel[i], i + 1));
	}
	gets(line);
	for(int ncasa = 1; ncasa <= casa; ncasa++) {
		// count[0] for '\0'
		for(int i = 0; i < LENGTH + 1; i++) {
			count[i].clear();
			count[i].push_back(0);
		}
		gets(line);
		for(int i = 0; line[i] != '\0'; i++) {
			for(multimap<char, int>::iterator it = letter.lower_bound(line[i]);
				it != letter.upper_bound(line[i]); ++it) {
				count[it->second][0] ++;
				count[it->second].push_back(count[it->second - 1][0]);
			}
		}
		
		for(int i = 1; i < count[1].size(); i++) {
			count[1][i] = i;
		}
		for(int i = 2; i < LENGTH + 1; i++) {
			for(int j = 1; j < count[i].size(); j++) {
				if(count[i][j] > 0) {
					count[i][j] = count[i - 1][count[i][j]];
				}
			}
			for(int j = 2; j < count[i].size(); j++) {
				count[i][j] += count[i][j - 1];
				if(count[i][j] >= 10000) {
					count[i][j] -= 10000;
				}
			}
		}
		
		printf("Case #%d: %04d\n", ncasa, count[19].back());
	}
}


