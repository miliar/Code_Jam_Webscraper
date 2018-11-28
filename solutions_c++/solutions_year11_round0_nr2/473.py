#include <cassert>
#include <cmath>
using namespace std;
#include <iostream>
#include <string>
#include <algorithm>
#include <cstring>
#include <stack>
#include <cstdio>
#include <set>
#include <vector>

//By chyx111
#define SZ(a) ((int)(a).size())
#define Rep(i,n) for(int n_ = (n), i = 0; i< n_; ++i)
#define forElem(elem,v) \
for(__typeof__(v.begin()) _it = v.begin(); _it != v.end(); ++_it)\
for(int _once=1, _done=0; _once; (!_done) ? (_it=v.end(), --_it) : _it )\
for(__typeof__(*_it) & elem = * _it; _once && !(_once=0); _done=1) 
#define ALL(a) (a).begin(),(a).end()

char input[32];
int combine[256][256];
vector<char> conflict[256];
int main() {
	int ca;cin>>ca;
	Rep(ica,ca){
		memset(combine,-1,(sizeof combine));
		memset(conflict,0,(sizeof conflict));
		int C, D, n;
		scanf("%d", &C);
		Rep(i, C){
			scanf("%s", input);
			combine[ input[0] ][ input[1] ] = input[2];
			combine[ input[1] ][ input[0] ] = input[2];
		}
		scanf("%d", &D);
		Rep(i, 256) conflict[i].clear();
		Rep(i, D){
			scanf("%s", input);
			if( input[0] == input[1] )assert(0);
			conflict[ input[0] ].push_back( input[1] );
			conflict[ input[1] ].push_back( input[0] );
		}
		scanf("%d", &n);
		scanf("%s", input);
		stack<char> st;
		int cnt[256];
		memset(cnt,0,(sizeof cnt));
		Rep(i, n){
			char curr = input[i];
			while( !st.empty() && combine[st.top()][curr] != -1 ){
				curr = combine[st.top()][curr];
				cnt[st.top()]--;
				st.pop();
			}
			bool ok = true;
			forElem( c, conflict[curr] ){
				if( cnt[c] ){
					ok = false;
				}
			}
			if( !ok ){
				memset(cnt,0,(sizeof cnt));
				while( !st.empty() )st.pop();
			}else{
				st.push(curr);
				cnt[curr]++;
			}
		}
		vector<char> ans;
		while( !st.empty() ){
			ans.push_back( st.top() );
			st.pop();
		}
		reverse( ALL(ans) );

		printf("Case #%d: [", ica+1);
		Rep(i, SZ(ans)){
			if(i)printf(", ");
			printf("%c", ans[i]);
		}
		puts("]");
	}
	return 0;
}

