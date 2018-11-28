#include <algorithm>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iostream>
#include <limits.h>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define SQ(a) ((a)*(a))
#define EPS 1e-10

set<string> strings;

int T; 
int N,M;

int main(){
	char tmp[200];
	scanf("%d\n",&T); 
	for(int t=1;t<=T;++t){
		scanf("%d %d\n",&N,&M);
		strings.clear();
		strings.insert("/");
		for(int i=0;i<N;++i){
			scanf("%s\n",tmp);
			string s(tmp);
			strings.insert(s);
			//cout << "in: " << s << endl;
			int index = 1;
			for(;;){
				index = s.find("/", index);
				if(index == string::npos) break;
				string s2 = s.substr(0, index);
				++index;
				//cout << s2 << endl;
				strings.insert(s2);
			}
		}
		long long cnt = 0;
		for(int i=0;i<M;++i){
			scanf("%s\n",tmp);
			string s(tmp);
			//cout << "\ttest for:" << s << endl;
			s = s + "/";
			int index = 1;
			for(;;){
				index = s.find("/", index);
				if(index == string::npos) break;
				string s2 = s.substr(0, index);
				++index;
				//cout << "test:" << s2 << endl;
				if(strings.find(s2) == strings.end()){
					++cnt;
					strings.insert(s2);
				}
				//strings.insert(s2);
			}
		}
		
		printf("Case #%d: %lld\n", t, cnt);
		
	}
}
