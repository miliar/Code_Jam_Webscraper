#include <stdio.h>
#include <algorithm>
using namespace std;

int tc,h,w,data[110][110],inf=100000;
char hasil[110][110],cnow;

char find(int j,int k){
	if (hasil[j][k]=='*'){
		int a,b,c,d,now,low;
		now=data[j][k];
		if (j>0) a=data[j-1][k];
		else a=inf;
		if (k>0) b=data[j][k-1];
		else b=inf;
		if (j<h-1) d=data[j+1][k];
		else d=inf;
		if (k<w-1) c=data[j][k+1];
		else c=inf;
		low=min(min(a,b),min(c,d));
		if ((now<=a)&&(now<=b)&&(now<=c)&&(now<=d)){
			hasil[j][k]=cnow;
			cnow++;
		}
		else if (a==low) hasil[j][k]=find(j-1,k);
		else if (b==low) hasil[j][k]=find(j,k-1);
		else if (c==low) hasil[j][k]=find(j,k+1);
		else if (d==low) hasil[j][k]=find(j+1,k);
	}
	return hasil[j][k];
}

void relabel(int j,int k,char tmp){
	char ttmp=hasil[j][k];
	hasil[j][k]=tmp;
	if ((j>0)&&(hasil[j-1][k]==ttmp)) relabel(j-1,k,tmp);
	if ((k>0)&&(hasil[j][k-1]==ttmp)) relabel(j,k-1,tmp);
	if ((j<h-1)&&(hasil[j+1][k]==ttmp)) relabel(j+1,k,tmp);
	if ((k<w-1)&&(hasil[j][k+1]==ttmp)) relabel(j,k+1,tmp);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	for (int i=0;i<tc;i++){
		scanf("%d %d",&h,&w);
		for (int j=0;j<h;j++)
			for (int k=0;k<w;k++){
				scanf("%d",&data[j][k]);
				hasil[j][k]='*';
			}
		cnow='A';
		for (int j=0;j<h;j++)
			for (int k=0;k<w;k++){
				hasil[j][k]=find(j,k);
			}
		cnow='a';
		for (int j=0;j<h;j++)
			for (int k=0;k<w;k++)
				if ((hasil[j][k]>='A')&&(hasil[j][k]<='Z')){
					relabel(j,k,cnow);
					cnow++;
				}
		printf("Case #%d:\n",i+1);
		for (int j=0;j<h;j++){
			for (int k=0;k<w-1;k++)
				printf("%c ",hasil[j][k]);
			printf("%c\n",hasil[j][w-1]);
		}
	}
	return 0;
}