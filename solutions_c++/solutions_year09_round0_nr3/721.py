#include <stdio.h>
#include <string.h>

const char s[]="welcome to code jam";

void add(int &x,int y){
	x+=y;
	if(x>=10000) x-=10000;
}

int main(){
	const int size=19;
	int N;
	char t[1000];
	scanf("%d",&N);
	fgets(t,1000,stdin);
	for(int cs=1; cs<=N; cs++){
		int a[size];
		for(int i=0; i<size; i++)
			a[i]=0;
		fgets(t,1000,stdin);
		for(int i=0; t[i]; i++){
			for(int j=size-1; j>0; j--)
				if(t[i]==s[j])
					add(a[j],a[j-1]);
			if(t[i]==s[0])
				add(a[0],1);
		}
		printf("Case #%d: %04d\n",cs,a[size-1]);
	}
	return 0;
}
