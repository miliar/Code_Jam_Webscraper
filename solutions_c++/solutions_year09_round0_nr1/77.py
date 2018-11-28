#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

#define MAXN 5500

int m;
string words[MAXN];

int calc(string& pattern){
	int ret = 0;
	int i,j;
	int p;
	
	for(i=0;i<m;i++){
		p = 0;
		for(j=0;j<words[i].size();j++){
			if(pattern[p] == '('){
				p++;
				bool ok = false;
				while(pattern[p] != ')'){
					if(words[i][j] == pattern[p]){
						ok = true;
					}
					p++;
				}
				if(!ok){
					break;
				}
				p++;
			}
			else{
				if(pattern[p] != words[i][j]){
					break;
				}
				p++;	
			}	
		}
		if(p >= pattern.size()){
			ret++;
		}
	}
	
	return ret;
}

int main(){
    int n;
    int i;
    int t=0;
    int l;
    
    while(scanf("%d %d %d",&l,&m,&n) != EOF){
		for(i=0;i<m;i++){
			cin >> words[i];
		}
		
		for(i=0;i<n;i++){
			string pattern;
			cin >> pattern;
			int ret	= calc(pattern);
			printf("Case #%d: %d\n",++t,ret);
		}
		
	}
    
    return 0;
}
