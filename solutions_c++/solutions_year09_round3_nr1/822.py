#include <iostream>
#include <fstream>
#include <cstdio>
#include <string>

using namespace std;

int pow(int n,int p) {
	if (p == 1) return n;
	if (p == 0) return 1;
	if (p % 2 == 0) {
		int res = pow(n,p/2);
		return res * res;
	} else return n * pow(n,p-1);
}

int main() {
	
	//freopen("test.in","r",stdin);
	
	int T,t,i,j,base,d;
	
	scanf("%d",&T);
	
	char s[80];
	int nums[80];
	int used[36];
	
	for (t = 1; t <= T; ++ t) {
		memset(s,0,sizeof(s));
		memset(nums,-1,sizeof(nums));
		memset(used,0,sizeof(used));
		scanf("%s\n",&s);
		
		//printf("%s\n",s);
		
		nums[0] = 1;
		used[1] = 1;
		for (i=0;i<strlen(s);++i) {
			if (s[i] == s[0]) nums[i] = 1;
		}
		
		for (i=1;i<strlen(s);++i) {
			if (nums[i] != -1) continue;
			
			for (j=0;j<36;++j) if (used[j] == 0) {
				d = j;
				break;
			}
			
			used[d] = 1;
			nums[i] = d;
			for (j=i;j<strlen(s);++j) {
				if (s[j] == s[i]) nums[j] = nums[i];
			}
		}
		
		base = 2;
		for (i=0;i<strlen(s);++i) 
			if (nums[i]+1 > base) base = nums[i]+1;
			
		long res = 0;
			
		for (i=0;i<strlen(s);++i) {
			res += nums[i] * pow(base,strlen(s) - i - 1);
		}
		
		printf("Case #%d: %d\n",t,res);
	}
	
	return 0;
}