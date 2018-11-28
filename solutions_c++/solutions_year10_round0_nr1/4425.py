#include <stdio.h>
#include "common.h"
#include <stdlib.h>
#include <string.h>

struct snapper
{
	bool on;
//	bool power;
};

int main(int argc,char *argv[])
{
	checkargc<2>(argc);
	FILE *fpin = fileopen(argv[1],"rb");
	FILE *fpout = fileopen("result","wb");
	char buf[256];
	int ncase = 0;
	myfgets(buf,256,fpin);
	getheadnum(buf,ncase,0);

	for(int i=0;i<ncase;i++){
		myfgets(buf,256,fpin);
		const char *p = buf;
		int ns = 0,times=0;
		p = getheadnum(p,ns,' ');
		getheadnum(p,times,0);
//		printf("%d %d\n",ns,times);
		bool *os = (bool*)malloc(sizeof(bool)*ns);
		memset(os,0,sizeof(bool)*ns);

		int arrpos = 0;
		for(int j=0;j<times;j++){
			for(int k=0;k<=arrpos;k++){
				os[k] = !os[k];
//				printf("%d ",os[k]?1:0);
			}
			for(int k=arrpos+1;k<ns;k++){
//				printf("%d ",os[k]?1:0);
			}

			for(int k=0;k<ns;k++){
				if(!os[k]){
					arrpos = k;
					break;
				}
				if(k==ns-1)	arrpos=k;
			}
//			printf("arrpos=%d\n",arrpos);
		}
		if(arrpos==ns-1 && os[ns-1]){
			printf("Hit!\n");
			fprintf(fpout,"%sCase #%d: ON",i==0?"":"\n",i+1);
		}
		else{
			fprintf(fpout,"%sCase #%d: OFF",i==0?"":"\n",i+1);
		}

		free(os);
	}
	fclose(fpin);
	fclose(fpout);
}
