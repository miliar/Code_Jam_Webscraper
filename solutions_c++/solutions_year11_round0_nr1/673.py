#include <cstdio>
#include <algorithm>

using namespace std;

int resoud(){
	int N;
	scanf("%d",&N);
	int tO=0,tB=0;
	int posO=1,posB=1;
	int prec=0;
	for (int i=0;i<N;i++){
		char s[5];
		int pos;
		scanf("%s%d",s,&pos);
		if (s[0]=='O'){
			prec=tO=max(tO+abs(pos-posO),prec)+1;
			posO=pos;
		}
		else{
			prec=tB=max(tB+abs(pos-posB),prec)+1;
			posB=pos;
		}
	}
	return prec;
}

int main(){
	int T;
	scanf("%d",&T);
	for (int i=0;i<T;i++)
		printf("Case #%d: %d\n",i+1,resoud());
	return 0;
}
