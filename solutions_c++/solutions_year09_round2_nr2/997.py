#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char mas[25];
int size;
// QSort
void sort(int l,int r)
{
	int i,j;
  char x,y;
  i=l;
  j=r;
  x=mas[(l+r)/2];
	do{
		while(i<size-1 && mas[i]<x) ++i;
    while(j>0 && x<mas[j]) --j;
		if(!(i>j)){
			y=mas[i];
      mas[i]=mas[j];
      mas[j]=y; 
			++i;
      --j;
		}
	}while(!(i>j));
	if(l<j) sort(l,j);
  if(i<r) sort(i,r);
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,j,tm;
	char tmp;
	scanf("%d\n",&T);
	for(int j=1;j<=T;j++){
		gets(mas);
		size=strlen(mas);
		i=size-2;
		while(i>0 && mas[i]>=mas[i+1]) i--;
		if(i>0 || (i==0 && mas[i]<mas[i+1])){
			tm=i+1;
			for(int k=tm;k<size;k++)
				if(mas[tm]=='0' || (mas[k]!='0' && mas[k]<mas[tm] && mas[k]>mas[i])) tm=k;
			tmp=mas[i];
			mas[i]=mas[tm];
			mas[tm]=tmp;
			sort(i+1,size-1);
			/*
			tm=i+1;
			for(int k=tm;k<size;k++) if((mas[k]!='0' && mas[tm]>mas[k] && mas[k]) || mas[tm]=='0') tm=k;
			tmp=mas[i];
			mas[i]=mas[tm];
			mas[tm]=tmp;
			sort(i+1,size-1);
			*/
		}else{
			sort(0,size-1);
			for(i=size+1;i>=0;--i) mas[i+1]=mas[i];
			mas[0]='0';
			tm=0;
			for(i=tm+1;i<size+1;i++) if(mas[tm]=='0' || (mas[i]!='0' && mas[i]<mas[tm])) tm=i;
			tmp=mas[0];
			mas[0]=mas[tm];
			mas[tm]=tmp;
		}
		printf("Case #%d: %s\n",j,mas);
	}
	return 0;
}