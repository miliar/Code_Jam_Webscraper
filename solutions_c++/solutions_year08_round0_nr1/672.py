#include <iostream>
#include <string>
#include <vector>
using namespace std;

int memo[1000];

int func(int cur, vector <string> &search, vector <string> &query) {
	if (memo[cur]!=-1) return memo[cur];
	int r=INT_MAX,flag;
	for (int i=0;i<search.size();i++) {
		if (search[i]!=query[cur]) {
			flag = 0;
			for (int j=1;cur+j<query.size();j++) {
				if (query[cur+j] == search[i]) {
					r = min(r,func(cur+j,search,query));
					flag = 1;
					break;
				}
			}
			if (!flag) return memo[cur] = 0;
		}
	}
	return memo[cur] = r+1;
}

int main(void) {
	int N,S,Q;
	string tmp;
	getline(cin,tmp);
	N = atoi(tmp.c_str());
	for (int testcase=0;testcase<N;testcase++) {
		vector <string> search, query;
		getline(cin,tmp);
		S = atoi(tmp.c_str());
		for (int sss=0;sss<S;sss++) {
			getline(cin,tmp);
			search.push_back(tmp);
		}
		getline(cin,tmp);
		Q = atoi(tmp.c_str());
		for (int qqq=0;qqq<Q;qqq++) {
			getline(cin,tmp);
			query.push_back(tmp);
			memo[qqq]=-1;
		}
		cout << "Case #" << testcase+1 << ": " << func(0,search,query) << endl;
	}
}
