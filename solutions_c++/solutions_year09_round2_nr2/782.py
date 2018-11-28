#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main(){
	int n;
	int d, len;
	scanf("%d", &d);
	n=d;
	char num[50];
	char tmpc;
	int tmpn;
	bool uns;
	while(d--){
		scanf("%s", num);
		len=strlen(num);
		uns=1;
		for(int i=0; i<len-1; i++){
			if(num[i]<num[i+1]){
				uns=0;
				break;
			}
		}
		if(uns){
			sort(num, num+len);
			for(int i=0; i<len; i++) if(num[i]!='0'){
				if(i==0) break;
				num[0]=num[i];
				num[i]='0';
				break;
			}
			printf("Case #%d: %c0%s\n", n-d, num[0], &num[1]);		
			continue;
		}
		for(int i=len-2; i>=0; i--){
			if(num[i]<num[i+1]){
				tmpn=i+1;
				for(int j=i+2; j<len; j++) if(num[j]>num[i] && num[j]<num[tmpn]) tmpn=j;
				tmpc=num[i];
				num[i]=num[tmpn];
				num[tmpn]=tmpc;
				sort(&num[i+1], &num[len]);
				printf("Case #%d: %s\n", n-d, num);		
				break;
			}	
		}
	}
	return 0;
}

