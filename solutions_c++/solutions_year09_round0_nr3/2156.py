#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int mem[501][4],n,cout;
char st[501];
int aa[256][5],bb[256][5];
void init(){
	int l=strlen(st);
	int i;
	for(i=0;i<l;i++)
		if(st[i]=='m')
			mem[i][3]=1;
}

void atry(){
	int l=strlen(st);
	int i,j,t,k,bt,at;
	for(i=l-1;i>=0;i--)
	  for(k=1;k<=3;k++){
	    if(mem[i][k]==0)
			continue;
	    at=aa[st[i]][k];
		bt=bb[st[i]][k];
		for(j=i-1;j>=0;j--){
			if(st[j]==at){
				mem[j][bt]+=mem[i][k];
				mem[j][bt]%=10000;
			}
		}
	}
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d\n",&n);
    aa['m'][3]='a';bb['m'][3]=1;
	aa['a'][1]='j';bb['a'][1]=1;
	aa['j'][1]=' ';bb['j'][1]=3;
	aa[' '][3]='e';bb[' '][3]=3;
	aa['e'][3]='d';bb['e'][3]=1;
	aa['d'][1]='o';bb['d'][1]=3;
	aa['o'][3]='c';bb['o'][3]=2;
	aa['c'][2]=' ';bb['c'][2]=2;
	aa[' '][2]='o';bb[' '][2]=2;
	aa['o'][2]='t';bb['o'][2]=1;
	aa['t'][1]=' ';bb['t'][1]=1;
	aa[' '][1]='e';bb[' '][1]=2;
	aa['e'][2]='m';bb['e'][2]=1;
	aa['m'][1]='o';bb['m'][1]=1;
	aa['o'][1]='c';bb['o'][1]=1;
	aa['c'][1]='l';bb['c'][1]=1;
	aa['l'][1]='e';bb['l'][1]=1;
	aa['e'][1]='w';bb['e'][1]=1;

	int i,j;
	for(i=1;i<=n;i++){
		cout=0;
		memset(mem,0,sizeof(mem));
		gets(st);
		init();
		atry();
		for(j=0;j<strlen(st);j++)
			if(st[j]=='w'&&mem[j][1]!=0)
				cout+=mem[j][1];
		cout%=10000;
		printf("Case #%d: %04d\n",i,cout);
	}
}