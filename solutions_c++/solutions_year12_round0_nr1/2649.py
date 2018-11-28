#include <stdio.h>
int main(){
	char moto[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char ato[26]  = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int j=1;
	FILE *fp,*fp2;
	char input[256];
	fp=fopen("A-small-attempt0.in","r");
	fp2=fopen("answer.out","w");
	int count = (int) fgets(input,256,fp);
	while(fgets(input,256,fp) != NULL){
	for(int i=0;input[i]!='\0';i++){
		if(*(input+i)!=' '&&*(input+i)!='\n') *(input+i)=ato[*(input+i)-'a'];
	}
	fprintf(fp2,"Case #%d: %s\n",j,input);
	j++;
	count--;
	if(count==0) break;
	}
	fclose(fp);
	fclose(fp2);
}