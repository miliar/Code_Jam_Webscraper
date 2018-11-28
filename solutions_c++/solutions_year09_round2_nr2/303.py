#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;

#define min(a,b) (((a)<(b))?(a):(b))
#define max(a,b) (((a)>(b))?(a):(b))
#define rep(i,n) for(i=0;i<(n);i++)

int main() {
	int T,kase=1;
	int i;
	char tmp[30];
	string num,res;
	scanf("%d",&T);
	while(T--) {
		scanf(" %s",tmp);
		num = tmp;
		if(next_permutation(num.begin(),num.end()) ) {
			res = num;
		}
		else {
			sort(num.begin(),num.end());
			num = "0" + num;
			for(i = 0; i < num.size(); i++) {
				if(num[i] != '0') {
					res = num[i] + num.substr(0,i) + num.substr(i+1);
					break;
				}
			}
		}

		printf("Case #%d: %s\n",kase++,res.c_str());
	}
	return 0;
}