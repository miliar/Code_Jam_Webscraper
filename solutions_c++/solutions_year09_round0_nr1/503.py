#include <cstdio>
#include <cstring>
#include <unistd.h>

char buf[1048576];
char cmd[1048576];

int main(){
	int n,m,k;
	while(scanf("%d %d %d",&n,&m,&k)==3){
		FILE* fout = fopen("a.tmp","w");
		for(int i=0;i<m;i++){
			scanf("%s",buf);
			fprintf(fout,"%s\n",buf);
		}
		fclose(fout);
		for(int i=1;i<=k;i++){
			scanf("%s",buf);
			for(int j=0;buf[j];j++){
				if(buf[j] == '(') buf[j] = '[';
				if(buf[j] == ')') buf[j] = ']';
			}

			strcpy(cmd,"cat a.tmp | grep \"");
			strcat(cmd,buf);
			strcat(cmd,"\" | wc -l");

			FILE* fp = popen(cmd,"r");
			int a;
			fscanf(fp,"%d",&a);
			fclose(fp);
			printf("Case #%d: %d\n",i,a);
		}	
	}
	return 0;
}
