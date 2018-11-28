#include <cstdio>
int T;
struct Case {
	int n;
	int k;
};
Case a[10000];
int result[10000];
int dy[30];
int scan(FILE *fi) {
	fscanf(fi,"%d",&T);
	int i;
	for(i=0;i<T;i++) {
		fscanf(fi,"%d%d",&a[i].n,&a[i].k);
	}
	fclose(fi);
	return 0;
}
int print(FILE *fo) {
	int i;
	for(i=0;i<T;i++) {
		fprintf(fo,"Case #%d: ",i+1);
		if(result[i]) fprintf(fo,"ON\n");
		else fprintf(fo,"OFF\n");
	}
	return 0;
}
int proc(Case d) {
	if(d.k==0) return 0;
	if((d.k-dy[d.n-1])%(dy[d.n-1]+1)==0) return 1;
	return 0;
}
int Proc() {
	int i;
	dy[0]=1;
	for(i=1;i<30;i++) {
		dy[i]=2*dy[i-1]+1;
	}
	for(i=0;i<T;i++) {
		if(i==30)
			printf("");
		result[i]=proc(a[i]);
	}
	return 0;
}
int main() {
	scan(fopen("INPUT.TXT","rt"));
	Proc();
	print(fopen("OUTPUT.TXT","wt"));
	return 0;
}