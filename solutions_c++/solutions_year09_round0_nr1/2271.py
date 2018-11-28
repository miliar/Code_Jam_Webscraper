#include <stdio.h>

char buf[1024];

int main() {
	int L,D,N;

	gets(buf);
	sscanf(buf,"%d %d %d",&L,&D,&N);
	
	for (int i = 0; i < D ; ++i){
		gets(buf);
		}
	for (int i = 0; i < N; ++i) {
		gets(buf);
		printf("%s\n",buf);
	}

	return 0;
}
