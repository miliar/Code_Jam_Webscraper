#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>

#define MP make_pair
#define ST first
#define ND second
#define PB push_back
#define LL long long
#define VII vector<int>
#define PII pair<int, int>

#define MAXN 105

using namespace std;

int t, c, d, n;

char comb[40][5];
char neg[30][5];
char str[120];
char res[120];

bool nega(char a, char b){
    for(int i = 0; i < d; i++){
	if(a == neg[i][0] && b == neg[i][1]) return true;
	if(b == neg[i][0] && a == neg[i][1]) return true;
    }
    return false;
}

char combine(char a, char b){
    for(int i = 0; i < c; i++){
	if(a == comb[i][0] && b == comb[i][1]) return comb[i][2];
	if(b == comb[i][0] && a == comb[i][1]) return comb[i][2];
    }
    return '\0';
}

int main(){
    scanf("%d", &t);
    for(int testcase = 0; testcase < t; testcase++){
	scanf("%d", &c);
	for(int i = 0; i < c; i++) scanf("%s", comb[i]);

	scanf("%d", &d);
	for(int i = 0; i < d; i++) scanf("%s", neg[i]);

	scanf("%d %s", &n, str);

	int res_len = 0;
	for(int i = 0; i < n; i++){
	    res[res_len] = str[i];
	    if(res_len > 0){
		char cmb = combine(res[res_len], res[res_len - 1]);
		if(cmb != '\0'){
		    res[res_len - 1] = cmb;
		}
		else{
		    for(int j = 0; j < res_len; j++){
			if(nega(res[res_len], res[j])){
			    res_len = 0;
			    break;
			}
		    }
		    if(res_len > 0) res_len++;
		}
	    }
	    else{
		res_len++;
	    }
	}

	printf("Case #%d: [", testcase+1);
	for(int i = 0; i < res_len; i++){
	    printf("%c", res[i]);
	    if(i != res_len - 1) printf(", ");
	}
	printf("]\n");
    }
    return 0;
}