#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int out[100];
int len, base;

void print(){
	unsigned long long ret=0;
	int pow=1;
	if(base<=1) base=2;
	for(int i=len-1; i>=0; i--){
		ret+=out[i]*pow;
		pow*=base;
	}	
	printf("%llu\n", ret); 
}

int main(){
	int d;
	scanf("%d", &d);
	char num[100];
	int conv[300];
	int fr;
	for(int i=1; i<=d; i++){
		for(int j=0; j<300; j++) conv[j]=-1;
		scanf("%s", num);
		len=strlen(num);
		conv[num[0]]=1;
		out[0]=1;
		base=1;
		fr=0;
		for(int j=1; j<len; j++){
			if(conv[num[j]]==-1){
				conv[num[j]]=fr;
				if(fr==0) fr=1;
				fr++;
				base++;
			}
			out[j]=conv[num[j]];
		}
		printf("Case #%d: ", i);
		print();
	}
	
	return 0;
}

