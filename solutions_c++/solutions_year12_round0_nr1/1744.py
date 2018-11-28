#include<fstream>
using namespace std;

int tt,n,p,m;
char t[30]="yhesocvxduiglbkrztnwjpfmaq",s[200];

int main(void){
	FILE *in,*out;
	int i,j;

	in=fopen("A-small-attempt0.in","r");
	out=fopen("output.txt","w");

	fscanf(in,"%d",&tt);
	fgets(s,200,in);
	for(i=1;i<=tt;i++){
		fgets(s,200,in);
		n=strlen(s);
		fprintf(out,"Case #%d: ",i);
		for(j=0;j<n;j++){
			if(s[j]>='a' && s[j]<='z') fprintf(out,"%c",t[s[j]-'a']);
			else fprintf(out,"%c",s[j]);
		}	
	}
	return 0;

}