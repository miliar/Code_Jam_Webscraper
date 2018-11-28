#include <stdio.h>
#include <vector>
#include <string.h>

using namespace std;
char seq[103];
int comb[256][256];
int opp[256][256];

int main(){
	int testcase = 0;
	int T;
	scanf("%d",&T);
	for(int testcase = 1; testcase <= T; testcase ++) {
		memset(comb,0,sizeof(comb));
		memset(opp,0,sizeof(opp));
		int c,d,n;
		char str[10];
		scanf("%d",&c);
		for(int i = 0;i < c;i ++){
			scanf("%s",str);
			comb[str[0]][str[1]] = str[2];
			comb[str[1]][str[0]] = str[2];
		}
		scanf("%d",&d);
		for(int i = 0;i <d ;i++) {
			scanf("%s",str);
			opp[str[0]][str[1]] = 1;
			opp[str[1]][str[0]] = 1;
		}
		scanf("%d",&n);
		scanf("%s",seq);
		vector<char> myset;

		for(int i = 0;i < n; i++){
			myset.push_back(seq[i]);
			if(myset.size() >= 2){
				if(comb[*myset.rbegin()][*++myset.rbegin()] != 0){
					char toadd = comb[*myset.rbegin()][*++myset.rbegin()];
					myset.pop_back();
					myset.pop_back();
					myset.push_back(toadd);
					continue;
				}
			}
			for(int j = 0;j + 1 < myset.size();j ++){
				if(opp[myset[j]][seq[i]]) {
					myset.clear();
				}
			}
		}

		printf("Case #%d: [",testcase);
		for(int i = 0; i < myset.size();i ++){
			printf("%c",myset[i]);
			if(i + 1 < myset.size() ){
				printf(", ");
			}
		}
		printf("]\n");
	}
	return 0;
}

