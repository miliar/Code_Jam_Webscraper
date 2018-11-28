#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;

char str[120];
int main(){
	int T;
	scanf("%d",&T);
	int testcase = 0;
	while(T--> 0 ){
		++testcase;
		scanf("%s",str);
		long long mustset = 0;
		long long mustclear = 0;
		long long cur = 1;
		for(int i = strlen(str)-1;i >= 0;i --){
			if(str[i] == '0'){
				mustclear |= cur;
			}else if(str[i] == '1'){
				mustset |= cur;
			}
			cur <<= 1;
		}
		long long ans;
		for(long long i = 1; i < (1LL<<31); i++){
			long long t = i*(long long)i;
			if((t & mustset) != mustset) continue;
			if(((~t) & mustclear) != mustclear) continue;
			ans = t;
			break;
		}
		printf("Case #%d: ",testcase);
		string strv;
		while(ans){
			if(ans%2 == 0){
				strv.push_back('0');
			}else{
				strv.push_back('1');
			}
			ans >>= 1;
		}
		reverse(strv.begin(),strv.end());
		printf("%s\n",strv.c_str());
	}
	return 0;
}
