#include<cstdio>
#include<set>
#include<string>
#include<vector>
using namespace std;
char s[200];
int main() {
	int ntc;
	scanf("%d", &ntc);
	for(int TC=1, N, M; TC <= ntc; TC++) {
		scanf("%d %d", &N, &M);
		set<string> st;
		st.insert("/");
		for(int i=0; i<N; i++) {
			scanf("%s", s);
			string ss = s, sk = "";
			ss = ss + "/";
			for(int k=0, to=ss.length(); k<to; k++) {
				sk.push_back(ss[k]);
				if ( ss[k] == '/' ) st.insert( sk );
			}
		}
		string sss[M+3];
		
		for(int i=0; i<M; i++) {
			scanf("%s", s);
			sss[i] = s;
		}
		sort(sss, sss+M);
		int ans = 0;
		for(int i=0; i<M; i++) {
			string ss = sss[i], sk = "";
			ss = ss + "/";
			for(int k=0, to=ss.length(); k<to; k++) {
				sk.push_back(ss[k]);
				if ( ss[k] == '/' ) {
					if ( st.find( sk ) == st.end() ) {
						ans++;
						st.insert(sk);
					}
				}
			}
		}
		printf("Case #%d: %d\n", TC, ans);
	}
	return 0;
}
