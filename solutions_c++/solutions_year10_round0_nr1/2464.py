#include <iostream>
using namespace std;

int main(){
	int t,tt,n,k;
	tt = 0;
	FILE *fin =/*stdin;//*/ fopen("A-large.in","r");
	FILE *fout = /*stdout;//*/fopen("QA.out","w");
	fscanf(fin,"%d",&t);
	tt = 0;
	while(t--){
		tt++;
		fscanf(fin,"%d %d",&n,&k);
		int t = (1<<n);
		t = k%t;
		if(t == (1<<n)-1)
			t = 1;
		else
			t = 0;
		fprintf(fout,"Case #%d: %s\n",tt,t==1?"ON":"OFF");
	}
	fclose(fin);
	fclose(fout);
}