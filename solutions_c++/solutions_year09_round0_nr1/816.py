#include <stdio.h>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;
const int SIZE =  500;
const int WIDTH = 30;
const int NUM = 5010;
const int BSZ = 500;
bool pat[SIZE][WIDTH];
string dic[NUM];
bool del[NUM];
char buff[BSZ];
int L,D,N;
int maxlev=0;
void init();
void work();
void showdic();
void mkpat(char * );
void showpat();
int calc();
int main(){
	//freopen("../../dat.in","r",stdin);
	scanf("%d%d%d",&L,&D,&N);
	init();
	work();
	return 0;
}
void work(){
	int i;
	for (i=1;i<=N;i++){
		scanf("%s",buff);
		mkpat(buff);
		int ans = calc();
		printf("Case #%d: %d\n",i,ans);
	}
}
void mkpat(char * str){
	memset(pat,false,sizeof(pat));
	int i,j;
	int lev=-1;
	int ed;
	for (i=0;str[i];i++){
		if (str[i]=='('){
			lev++;
			for (j=i+1;str[j] && str[j]!=')';j++){
				if (str[j]>='a' && str[j]<='z')
					pat[lev][str[j]-'a']=true;
			}
			i=j;
		}else{
			lev++;
			if (str[i]>='a' && str[i]<='z')
				pat[lev][str[i]-'a']=true;
		}
	}
	maxlev=lev+1;
	//printf("pat: %s\n",str);
	//showpat();
}
void showpat(){
	int i,j;
	for(i=0;i<maxlev;i++){
		printf("lev: %d\n",i);
		for (j=0;j<WIDTH;j++){
			if (pat[i][j]){
				printf(" %c ",j+'a');
			}
		}
		printf("\n");
	}
}
int calc(){
	memset(del,false,sizeof(del));
	int lev=0;
	int i;
	for (lev=0;lev<L;lev++){
		for (i=0;i<D;i++){
			if (del[i])
				continue;
			int ind =dic[i][lev]-'a';
			if (pat[lev][ind]==false){
				del[i]=true;
			}
		}
	}
	int cnt=0;
	for (i=0;i<D;i++){
		if (del[i]==false)
			cnt++;
	}
	return cnt;
}
void init(){
	int i;
	int t=0;
	for (i=0;i<D;i++){
		scanf("%s",buff);
		dic[t++]=string(buff);
	}
	sort(dic,dic+D);
	//showdic();
}
void showdic(){
	int i;
	for (i=0;i<D;i++){
		printf("%s\n",dic[i].c_str());
	}
}