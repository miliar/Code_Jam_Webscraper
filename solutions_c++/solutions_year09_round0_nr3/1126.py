#include <iostream>
#include <cstdio>
#include <cstdlib>
#define MOD 10000
using namespace std;

char welcome[20] = "welcome to code jam";
char message[512];
int data[512][20];


/*  
long back(int pos,int k) { // Small data set
	int i;
	long ret = 0;
	
	if (k == 18) return 1;
	
	for (i=pos+1;i<strlen(message);++i)
		if (message[i] == welcome[k+1]) {
			ret += back(i,k+1);
			ret %= MOD;
		}
	
	return ret;
} 
*/

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	
	int t,T,i,j,k,p,res;
	
	scanf("%d\n",&T);
	
	for (t=1;t<=T;++t) {
		res = 0;
		char cres[5];
	
		memset(data,0,sizeof(data));
	
		memset(message,0,sizeof(message));
		fgets(message,sizeof(message),stdin);
		
		for (i=strlen(message)-1;i>=0;--i) {
			if (message[i] == 'w') {data[i][0] = 1;p=i;}
		}
		
		for (i=1;i<19;++i) {
			for (j=0;j<strlen(message);++j) {
				if (message[j] == welcome[i]) 
					for (k=j-1;k>=0;--k) {	
						if (message[k] == welcome[i-1]) { 
							data[j][i] += data[k][i-1];
							data[j][i] %= MOD;
						}
					}
			}
			
			if (i == 18) {
				for (j=0;j<strlen(message);++j) {
					if (message[j] == 'm') res += data[j][i] % MOD;
					res %= MOD;
				}
			}
		}
		
		for (i=3;i>=0;--i) {
			cres[i] = '0' + res % 10;
			res /= 10;
		}
		cres[4] = '\0';
		
		printf("Case #%d: %s\n",t,cres);
		
	}
	
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}