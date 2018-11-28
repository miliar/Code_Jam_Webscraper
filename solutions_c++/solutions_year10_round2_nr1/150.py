
#include <iostream>
#include <string>
#include <set>
#include <cstring>

using namespace std;

int main(){
	
	int T; cin >> T;
	int N, M;
	char buf[1000];
	set<string> s;

	for(int testcase=1; testcase <=T; ++testcase){
		cin >> N >> M;
		int ans = 0;
		s.clear();
		for(int i=0; i<N+M; i++){
			scanf("%s", buf);
			int len=strlen(buf);
			if(i < N){
				for(int j=1; j<len; ++j){
					if(buf[j] == '/'){
						buf[j] = '\0';
						s.insert(string(buf));
						buf[j] = '/';
					}
				}
				s.insert(string(buf));
			}else{
				for(int j=1; j<len; ++j){
					if(buf[j] == '/'){
						buf[j] = '\0';
						if(s.find(string(buf)) == s.end()){
							++ans;
							s.insert(string(buf));
						}
						buf[j] = '/';
					}
				}
				if(s.find(string(buf)) == s.end()){
					++ans;
					s.insert(string(buf));
				}
			}
		}
		printf("Case #%d: %d\n", testcase, ans);
	}
	return 0;
}
