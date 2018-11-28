#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <set>
#include <map>
#include <string>
#include <vector>

using namespace std;

map <string, int> M[10000];
string S;
char s[256];
   
int main(){	
	freopen("in", "r", stdin);
	freopen("out1", "w", stdout);
	
	int ntest;
	
	scanf("%d", &ntest);
	
	for (int itest=0; itest<ntest; ++itest){
		int n, m;
		int k=0;
		M[0].clear();
		scanf("%d%d\n", &n, &m);
		
		for (int i=0; i<n; ++i){
			scanf("%s", s);
			int v = 0;
			int j = 0;
			int l = strlen(s);
			s[l] = '/';			
			while (j < l){
				++j;
    			S = "";
    			while (s[j] != '/'){
    				S = S + s[j];
    				++j;			
    			}
    			if (M[v].find(S) != M[v].end()){
    				v = (M[v].find(S) -> second);
    			}
    			else{
    				++k;
    				M[k].clear();
    				M[v][S] = k;
    				v = k;			
    			}
    		}		    		
		}
		
		int ans = 0;
		
		for (int i=0; i<m; ++i){
			scanf("%s", s);
			int v = 0;
			int j = 0;
			int l = strlen(s);
			s[l] = '/';			
			while (j < l){
				++j;
    			S = "";
    			while (s[j] != '/'){
    				S = S + s[j];
    				++j;			
    			}
    			if (M[v].find(S) != M[v].end()){
    				v = (M[v].find(S) -> second);
    			}
    			else{
    				++ans;
    				++k;
    				M[k].clear();
    				M[v][S] = k;
    				v = k;			
    			}
    		}		    		
		}
		
		printf("Case #%d: %d\n", itest+1, ans);
	
	}

    return 0;
}

