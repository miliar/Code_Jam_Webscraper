#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(){
	char a[100];
	int N,c,i,j;
	scanf("%d",&N);
	for(int cs=1; cs<=N; cs++){
		scanf("%s",&a);
		c=strlen(a);
		for(i=c-1; i>0; i--)
			if(a[i-1]<a[i]) break;
		printf("Case #%d: ",cs);
		if(i==0){
			sort(a,a+c);
			for(i=0; a[i]=='0'; i++);
			if(i>0) swap(a[0],a[i]);
			printf("%c0%s\n",a[0],a+1); 
		}else{
			sort(a+i,a+c);
			for(j=i; a[j]<=a[i-1]; j++);
			swap(a[i-1],a[j]);
			sort(a+i,a+c);
			printf("%s\n",a);
		}
	}
	return 0;
}
