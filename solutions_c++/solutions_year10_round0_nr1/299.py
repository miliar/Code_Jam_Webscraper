#include <stdio.h>
#include <vector>
#include <string>
#include <list>

int countbits(unsigned long c,int len){
	int r=0;
	while(c!= 0 && len-- >0){
		if(c & 1 != 0){
			r++;
		}
		c >>= 1;
	}
			
	return r;
}

int main(int argc,char** argv){
	FILE* fp = fopen(argv[1],"r");
	char buf[256];
	char* p;
	
	fgets(buf,256,fp);
	int T = atoi(buf);

	int N,K;
	int c = 0;
	while(fscanf(fp,"%d %d",&N,&K) != EOF){
		int res = countbits(K,N);
		printf("Case #%d: ",++c);
		if(N==res){
			printf("ON");
		}else{
			printf("OFF");
		}
		printf("\n");
	}
	fclose(fp);
}

