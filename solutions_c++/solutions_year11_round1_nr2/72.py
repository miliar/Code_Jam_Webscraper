#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

char buffer[100];

pair<int,string> play(const char *l,const vector<string> &dict) {
	
	if (!*l) return make_pair(0,dict[0]);
	if (dict.size() == 1) return make_pair(0,dict[0]);
	int mv = -1;
	vector<string> ret;

	typedef map<vector<size_t>,vector<string> >::iterator iterator;
	map<vector<size_t>,vector<string> > mp;
	for (size_t i=0; i<dict.size(); ++i) {
		vector<size_t> key;
		for (size_t j=0; j<dict[i].size(); ++j) {
			if (dict[i][j] == *l) key.push_back(j);
		}
		iterator it = mp.find(key);
		if (it==mp.end()) {
			mp[key] = vector<string>(1,dict[i]);
		} else {
			it->second.push_back(dict[i]);
		}
	}
	for (iterator it=mp.begin(); it!=mp.end(); ++it) {
		pair<int,string> r = play(l+1,it->second);
		if (it->first.empty()) {
			r.first++;
		}
		if (r.first > mv) {
			mv = r.first;
			ret = vector<string> (1,r.second);
		} else if (r.first == mv) {
			ret.push_back(r.second);
		}
	}

	iterator it = mp.find(vector<size_t>()); 
		if (it != mp.end() && it->second.size() == dict.size()) {
			mv --;
		}
	
/*	if (ret.size() > 1) {
	printf("\nrtest: %d %s %s\n",mv,ret[0].c_str(),ret[1].c_str());
	}
	*/
	if (ret.size() == 1) return make_pair(mv,ret.front());
	for (size_t i=0; i<dict.size(); ++i) {
		for (size_t j=0; j<ret.size(); ++j) {
			if (dict[i] == ret[j]) return make_pair(mv,ret[j]);
		}
	}
	return make_pair(mv+1,"");
}

string playAll(const char *letters,const vector<string> &dict) {
	int mv = -1;
	vector<string> ret;
	for (size_t i=1; i<=10; ++i) {
		vector<string> d;
		for (size_t j=0; j<dict.size(); ++j) {
			if (dict[j].size() == i) {
				d.push_back(dict[j]);
			}
		}
		if (!d.empty()) {
			pair<int,string> r = play(letters,d);
			if (r.first > mv) {
				mv = r.first;
				ret = vector<string> (1,r.second);
			} else if (r.first == mv) {
				ret.push_back(r.second);
			}
		}
	}
//	printf("\ntest: %d %d\n",ret.size(),mv);
	if (ret.size() == 1) return ret.front();
	for (size_t i=0; i<dict.size(); ++i) {
		for (size_t j=0; j<ret.size(); ++j) {
			if (dict[i] == ret[j]) return ret[j];
		}
	}
	return "";
}

int main(void) {
	int t;
	scanf("%d",&t);
	for (int tc=1; tc<=t; ++tc) {
		printf("Case #%d:",tc);
		int n,m;
		scanf("%d%d",&n,&m);
		vector<string> dict;
		for (int i=0; i<n; ++i) {
			scanf("%s",buffer);
			dict.push_back(buffer);
		}
		while (m--) {
			scanf("%s",buffer);
			printf(" %s",playAll(buffer,dict).c_str());
		}
		printf("\n");
	}
	return 0;
}
