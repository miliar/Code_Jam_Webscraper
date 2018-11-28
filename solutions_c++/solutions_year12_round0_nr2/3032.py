#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int n, s, p;
int data[105];
FILE *fin = fopen("B-large.in","r");
FILE *fout = fopen("out.txt","w");
int main()
{
	int ca, k =0; 
	fscanf(fin,"%d",&ca);
	while(ca--){
		fscanf(fin,"%d%d%d",&n,&s,&p);
		int i;
		for(i=0;i<n;++i)
			fscanf(fin,"%d",&data[i]);
		fprintf(fout,"Case #%d: ",++k);
		int ans=0;
		for(i=0;i<n;++i){
			int temp = data[i] / 3;
			if(temp>=p) ans++;
			else if(data[i]!=0){//²»ÖªµÀ°¡
			if((temp+1==p)&&(data[i]%3>=1)) ans++;
			else if(s!=0&&(temp+2==p)&&(data[i]%3==2)) {ans++;s--;}
			else if(s!=0&&(temp+1==p)&&(data[i]%3==0)) {ans++;s--;}
			}
		}
		fprintf(fout,"%d\n",ans);
	}
	return 0;
}