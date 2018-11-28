#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<vector>
#include<set>
#include<map>
#include<algorithm>

using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define EACH(i,x) REP(i,(x).size())
#define sz	size()
#define all(x) ((x).begin, (x).end)
#define eps	1e-15

typedef long long int lint;

string solve()
{
	int c, d, n;
	scanf("%d",&c);

	map<pair<char, char>, char> combine;

	REP(i,c) {
		char buf[128];
		scanf("%s",buf);
		combine[make_pair(buf[0],buf[1])] = buf[2];
		combine[make_pair(buf[1],buf[0])] = buf[2];
	}

	scanf("%d",&d);

	set<pair<char, char> > opposite;
	REP(i,d) {
		char buf[128];
		scanf("%s",buf);
		opposite.insert(make_pair(buf[0], buf[1]));
		opposite.insert(make_pair(buf[1], buf[0]));
	}
	scanf("%d",&n);
	char buf[256];
	scanf("%s",buf);
	string str = buf;

	string result;
	for(int i=0; i<str.size(); i++) {

		if(result.size() >= 1) {
			char a = result[result.size()-1];
			char b = str[i];
			if(combine.count(make_pair(a,b)) > 0) {
				string temp = result.substr(0,result.size()-1);
				result = temp + combine[make_pair(a,b)];
				continue;
			}
		}
		for(int j=0; j<result.size(); j++){
			if (opposite.find(make_pair(result[j], str[i])) != opposite.end()) {
				result.clear();
				goto maki;
			}
		}
		result += str[i];
maki: ;
	}
	return result;
}

int main(void)
{
	int T;
	scanf("%d",&T);

	REP(i,T) {
		printf("Case #%d: ", i+1);
		string result = solve();
		printf("[");
		for(int i=0; i<result.size(); i++){
			if(i)
				printf(", %c",result[i]);
			else printf("%c",result[i]);
		}

		printf("]\n");
	}

	return 0;
}

