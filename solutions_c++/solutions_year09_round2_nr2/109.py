#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(void)
{
	int T,cs=0;
	scanf("%d",&T);
	while(T--){
		char z[35];
		int n;
		scanf("%s",z+1);
		n=strlen(z+1);
		z[0]='0';
		next_permutation(z,z+n+1);
		if(z[0]=='0'){
			printf("Case #%d: %s\n",++cs,z+1);
		}else
			printf("Case #%d: %s\n",++cs,z);
	}
	return 0;
}
