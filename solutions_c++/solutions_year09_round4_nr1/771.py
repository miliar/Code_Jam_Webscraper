#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int leftones(const string & st){
    for (int i = st.size()-1; i >= 0; i --)
	if (st[i] == '1')
	    return i + 1;
    return 0;
}

int main(){

    int numcases;
    scanf("%d", &numcases);

    for (int casno = 1; casno <= numcases; casno ++){
	int n;
	scanf("%d", &n);

	char str[1000];
	vector<string> vst;
	for (int i = 0; i < n; i ++){
	    scanf("%s", str);
	    vst.push_back(str);
	}
	
	int ans = 0;
	for (int i = 0; i < n; i ++){
	    //row i; at most (i+1) zeroes
	    if (leftones(vst[i]) > i+1){
		for (int j = i+1; j < n; j ++){
		    if (leftones(vst[j]) <= i+1){
			for (int k = j; k > i; k --){
			    swap(vst[k], vst[k-1]);
			    ans ++;
			}
			break;
		    }
		}
	    }
	}
	printf("Case #%d: %d\n", casno, ans);
    }
    return 0;
}
	
	
    
