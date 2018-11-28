#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

char n[30];
int ntc,len,pos;

int main(){
	freopen("input2.txt","r",stdin);
	freopen("output2.txt","w",stdout);
	scanf("%d",&ntc);
	for (int tc=1;tc<=ntc;tc++){
		scanf("%s",n);
		len=strlen(n);
		if (next_permutation(n,n+len)) printf("Case #%d: %s\n",tc,n);
		else{
			printf("Case #%d: ",tc);
			for (int i=0;i<len;i++)
				if (n[i]!='0'){
					pos=i;
					break;
				}
			printf("%c",n[pos]);
			for (int i=0;i<(pos+1);i++) printf("0");
			for (int i=pos+1;i<len;i++) printf("%c",n[i]);
			printf("\n");
		}
	}
	return 0;
}
