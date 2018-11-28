#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

char map[16];
int T;
int notfull=0;
char input[128];
char out[128];

void get(){
	for(int i=0;i<4;i++){
		gets(input);
		for(int j=0;j<4;j++){
			int a;
			switch(input[j]){
			case 'O':
				a=1;break;
			case 'X':
				a=2;break;
			case 'T':
				a=3;break;
			case '.':
				notfull=1;
				a=4;break;
			}
			map[i*4+j]=a;
		}
	}
	gets(input);
}

int hantei(int p){
	for(int i=0;i<4;i++){
		int ok=1;
		for(int j=0;j<4;j++){
			if(map[4*i+j]!= p && map[4*i+j]!= 3){
				ok=0;
			}
		}
		if(ok)return 1;
	}
	for(int i=0;i<4;i++){
		int ok=1;
		for(int j=0;j<4;j++){
			if(map[i+j*4]!= p && map[i+j*4]!= 3){
				ok=0;
			}
		}
		if(ok)return 1;
	}
	{
		int ok=1;
		for(int j=0;j<4;j++){
			if(map[3+3*j]!= p && map[3+j*3]!= 3){
				ok=0;
			}
		}
		if(ok)return 1;
	}
	{
		int ok=1;
		for(int j=0;j<4;j++){
			if(map[0+5*j]!= p && map[0+j*5]!= 3){
				ok=0;
			}
		}
		if(ok)return 1;
	}
	return 0;
}
void solve(){
	if(hantei(1)){
		sprintf(out,"O won");
	}else if(hantei(2)){
		sprintf(out,"X won");
	}else if(notfull){
		sprintf(out,"Game has not completed");
	}else{
		sprintf(out,"Draw");
	}
	return;
}

int main(int argc,char **argv){
	scanf("%d\n",&T);
	for(int i=0;i<T;i++){
		notfull=0;
		get();
		solve();
		printf("Case #%d: %s\n",i+1,out);
	}
}
