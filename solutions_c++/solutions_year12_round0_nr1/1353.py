#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

char store[102];
char hash[27]= "yhesocvxduiglbkrztnwjpfmaq";
char t;

int main() {

	int test=0, i=0, count=1, len=0;
	
	scanf("%d",&test);
	scanf("%[\n]",&t);
	while(count <= test) {
		scanf("%[^\n]",store);
		scanf("%[\n]",&t);
		len = strlen(store);
		for(i=0; i< len; ++i) {
			if(store[i]!=' ') {
				store[i] = hash[store[i]-'a'];
			}
		}
		printf("Case #%d: %s\n",count, store);
		store[0]='\0';
		++count;
	}

	return 0;
}
