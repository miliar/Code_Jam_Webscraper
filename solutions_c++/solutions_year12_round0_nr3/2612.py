#include<iostream>
#include<math.h>
//#include<algorithm>
using namespace std;

int main(){
	FILE * file=fopen("d:\\a.txt","r");
	FILE * file2=fopen("d:\\a2.txt","w");
	int t =0,a=0,b=0,c=0,i=0,j=0,k=0,res =0,n=0,temp=0;
	int sign[7];
	//while(fscanf(file,"%s",buffer)!=EOF){
	fscanf(file, "%d", &t);
	i =1;
	while(i<=t){
		fscanf(file,"%d%d",&a,&b);
		
		c=a;
		res=0;
		while(c<=b){
			temp=c;
			n=1;
			while(temp/10!=0){temp/=10;n++;}
			j=1;
			while(j<n){
				temp= c/pow(10.0,j)+c%(int)pow(10.0,j)*pow(10.0,n-j);
				if(temp <=b&&temp>=a&&temp!=c&&temp>=pow(10.0,n-1)){
					k=1;
					while(k<j){
						if(sign[k]==temp)break;
						k++;
					}
					if(k==j){res++;sign[j]=temp;}
				}
				j++;
			}
			memset(sign,0,28);
			c++;
		}
		fprintf(file2,"Case #%d: %d\n", i,res/2);
		i++;
	}
	//while(gets(buffer)){
	fclose(file);
	fclose(file2);
	//getchar();
	//getchar();
	return 0;
}