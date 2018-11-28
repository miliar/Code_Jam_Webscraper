#include<cstdio>
#include<algorithm>

using namespace std;

int n;

char s[45];

int t[45];

void alg(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++){
		scanf("%s",s+1);
		int a = 0;
		for(int j=1;j<=n;j++){
			if(s[j] == '1') a = j;
		}
		t[i] = a;
	}
	int w = 0;
	for(int i=1;i<=n;i++){
		for(int k=i;k<=n;k++){
			if(t[k] <= i){
				while(k != i){
					++w;
					swap(t[k],t[k-1]);
					--k;
				}
				break;
			}
		}
	}
	printf("%d\n",w);
}

int main(){
	int d;
	scanf("%d",&d);
	for(int i=1;i<=d;i++){
		printf("Case #%d: ",i);
		alg();
	}
}
