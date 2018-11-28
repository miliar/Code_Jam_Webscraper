#include<cstdio>
#include<cstring>
using namespace std;
char a[]="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	int n,i,j;
	char ch;
	FILE * file1=fopen("A-small-attempt0.in","r");
	FILE * file2=fopen("b.out","w");
	fscanf(file1,"%d",&n);
	ch=fgetc(file1);
	for(i=1;i<=n;i++){
		fprintf(file2,"Case #%d: ",i);
		ch=fgetc(file1);
		while(!feof(file1)){
			if(ch=='\n')
				break;
			if(ch==' ')
				fputc(' ',file2);
			else
				fputc(a[ch-'a'],file2);
			ch=fgetc(file1);
		}
		fputc('\n',file2);
	}
	fclose(file1);
	fclose(file2);
}