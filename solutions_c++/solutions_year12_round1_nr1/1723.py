#include<iostream>
#include<math.h>
//#include<algorithm>
using namespace std;

FILE * file=fopen("d:\\a.txt","r");
FILE * file2=fopen("d:\\ao.txt","w");
//while(fscanf(file,"%s",buffer)!=EOF){
//while(gets(buffer)){
//"%.*s"
#define INFINITE 300000;
int t, a, b;
float prob[100000];
int main(){
	int i =1,j,k;
	float pr,e1,e2,e3,e;
	fscanf(file, "%d", &t);
	while(i<=t){
		fscanf(file, "%d%d", &a, &b);
		j=0;
		pr = 1;
		e =INFINITE
		while(j<a){
			fscanf(file, "%f", &prob[j]);
			pr*=prob[j];
			j++;
		}
		//
		e1 = pr * (b+1-a)+ (1-pr)*(2*b+2-a);
		if(e1< e)e = e1;
		e2 = b+2;
		if(e2< e)e = e2;
		j=a;
		pr = 1;
		while(j>=1){
			e3 = (2*j+b+1-a)*pr +(2*j+2*b+2-a)*(1-pr);
			if(e3< e)e=e3;
			pr*=prob[a-j];
			j--;
		}
		//
		fprintf(file2, "Case #%d: %.6f\n", i,e);
		i++;
	}
	//getchar();
	//getchar();
	return 0;
}