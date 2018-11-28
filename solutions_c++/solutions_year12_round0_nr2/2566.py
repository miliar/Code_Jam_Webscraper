#include<iostream>
#include<math.h>
//#include<algorithm>
using namespace std;

int main(){
	FILE * file=fopen("d:\\a.txt","r");
	FILE * file2=fopen("d:\\a2.txt","w");
	int t =0,n=0, s=0,p=0,i=0,j=0,res=0,n1=0,n2=0,score=0;
	//while(fscanf(file,"%s",buffer)!=EOF){
	fscanf(file, "%d", &t);
	i =1;
	while(i<=t){
		fscanf(file,"%d%d%d",&n,&s,&p);
		j=n1=n2=0;
		while(j<n){
			fscanf(file,"%d",&score);
			if(score>=3*p-2)n1++;
			else if(score>=max(3*p-4,2))n2++;
			j++;
		}
		fprintf(file2,"Case #%d: %d\n", i,n1+min(n2,s));
		i++;
	}
	//while(gets(buffer)){
	fclose(file);
	fclose(file2);
	//getchar();
	//getchar();
	return 0;
}