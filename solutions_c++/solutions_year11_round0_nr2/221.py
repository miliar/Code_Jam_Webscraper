#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <deque>
#include <map>

using namespace std;

void solve()
{
	int cn, dn, n;
	char seq[1000];

	std::map<std::pair<char, char>, char> combines;
	std::vector<std::pair<char, char> > opposes;
	std::vector<char> str;

	scanf("%d",&cn);
	for(int i = 0; i < cn; ++i) {
		char buf[100];
		scanf("%s",buf);
		combines[std::make_pair(buf[0],buf[1])] = buf[2];
	}
	scanf("%d",&dn);
	for(int i = 0; i < dn; ++i) {
		char buf[100];
		scanf("%s",buf);
		opposes.push_back(std::make_pair(buf[0],buf[1]));
	}

	
	scanf("%d",&n);	
	scanf("%s",seq);
	for(int i = 0; i < n; ++i) {
		str.push_back(seq[i]);
		if(str.size() < 2) continue;
		char c1 = str[str.size()-1];	
		char c2 = str[str.size()-2];	
		std::pair<char, char> p1 = std::make_pair(c1, c2);
		std::pair<char, char> p2 = std::make_pair(c2, c1);
		if(combines.count(p1)) {
			str.pop_back();
			str.pop_back();
			str.push_back(combines[p1]);
		}
		else if(combines.count(p2)) {
			str.pop_back();
			str.pop_back();
			str.push_back(combines[p2]);
		}
		else {
			int cnt[52] = {0, };	
			for(int i = 0; i < str.size(); ++i) {
				cnt[str[i]-'A'] = 1;
			}
			for(int i = 0; i < opposes.size(); ++i) {
				if(cnt[opposes[i].first-'A'] == 1
						&& cnt[opposes[i].second-'A'] == 1) {
					str.clear();
					break;
				}
			}
		}
	}

	printf("[");
	for(int i = 0; i < str.size(); ++i) {
		if(i) printf(", ");
		printf("%c",str[i]);
	}
	printf("]\n");
}

int main(int argc, char *argv[])
{
	int kase;
	scanf("%d",&kase);
	for(int i = 1; i <= kase; ++i) {
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
