#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;

int O,B,T,Opos,Bpos,N,x;
char c,pre;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int cn=1;cn<=T;++cn){
		scanf("%d",&N);
		O = B = 0;
		Opos = Bpos = 1;
		for(int i=0;i<N;++i){
			scanf(" %c%d",&c,&x);
			if(c == 'O'){
				O += abs(Opos-x);
				if(i > 0 && c != pre) O = max(O,B);
				++O;
				Opos = x;
			}
			else{
				B += abs(Bpos-x);
				if(i > 0 && c != pre) B = max(O,B);
				++B;
				Bpos = x;
			}
			pre = c;
		}
		printf("Case #%d: %d\n",cn,max(O,B));
	}
}
