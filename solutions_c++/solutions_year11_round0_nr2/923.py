#include <cstdio>
#include <string>
#include <map>
#include <vector>
using namespace std;

int pairChar(char c1, char c2) {
	return (((int)c1)&255) | ((((int)c2)&255)<<8);
}

int main() {
	int problemCount;
	scanf("%d", &problemCount);
	for(int problemId=0; problemId<problemCount; ++problemId) {
		int C;
		scanf("%d", &C);
		map<int, char> cSet;
		for(int i=0; i<C; ++i) {
			char buf[256];
			scanf("%s", buf);
			cSet[pairChar(buf[0], buf[1])] = buf[2];
			cSet[pairChar(buf[1], buf[0])] = buf[2];
		}
		int D;
		scanf("%d", &D);
		map<char, vector<char> > oSet;
		for(int i=0; i<D; ++i) {
			char buf[256];
			scanf("%s", buf);
			oSet[buf[0]].push_back(buf[1]);
			oSet[buf[1]].push_back(buf[0]);
		}
		int N;
		scanf("%d", &N);
		char buf[256];
		scanf("%s", buf);
		string result;
		for(int i=0; i<N; ++i) {
			result.push_back(buf[i]);
			if(2 <= result.size()) {
				int s = result.size();
				char c1 = result[s-1];
				char c2 = result[s-2];
				char c3 = cSet[pairChar(c1, c2)];
				if(c3) {
					result.erase(s-2);
					result.push_back(c3);
				}
			}
			if(2 <= result.size()) {
				int s = result.size();
				char c1 = result[s-1];
				result.erase(s-1);
				bool flag = false;
				const vector<char> & list = oSet[c1];
				for(int j=0; j<(int)list.size(); ++j) {
					char c2 = list[j];
					size_t p = result.find(c2, 0);
					if(p!=result.npos) {
						flag = true;
						break;
					}
				}
				result.push_back(c1);
				if(flag) {
					result.clear();
				}
			}
		}
		printf("Case #%d: [", problemId + 1);
		for(int j=0; j<(int)result.size(); ++j) {
			if(j!=0) {
				printf(", ");
			}
			printf("%c", result[j]);
		}
		printf("]\n");
	}
	return 0;
}
