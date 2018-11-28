#include<iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int a ,b;
FILE *fin =fopen("C-small-attempt0.in","r");
FILE *fout = fopen("out.txt","w");
int main()
{
	int ca; fscanf(fin,"%d",&ca);
	int k = 0;
	while(ca--){
		fscanf(fin,"%d%d",&a,&b);
		int i; int ans = 0;
		for(i=a;i<b;++i){
			if(i<10||i>=1000) continue;
			if(i<100){
				int shu = i % 10;
				shu = shu * 10 + i / 10;
				if(shu>i&&shu<=b) ans++;
			}
			else if(i<1000){
				int shu = i % 100;
				shu = shu * 10 + i / 100;
				if(shu>i&&shu<=b) ans++;
				shu = i % 10;
				shu = shu * 100 + i / 10;
				if(shu>i&&shu<=b) ans++;
			}
		}
	 fprintf(fout,"Case #%d: %d\n",++k,ans);
	}
	return 0;
}