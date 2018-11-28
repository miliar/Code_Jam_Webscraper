#include <stdio.h>
#include <iostream>
#include <string.h>
using namespace std;
int ch[30][30];
int pos[30];
char com[1000];
int fin[1000];
struct NODE{
	int st;
	int cc[30];
	void clear(){
		for(int i = 0; i < 30; i ++){
			cc[i] = 0;
		}
		st = 0;
	}
};
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int i,j;
	int C,D,N;
	int T;
	int a,b,c;
	NODE nod;
	int cas = 1;
	scanf("%d",&T);
	int l;
	while(T --){
		scanf("%d",&C);
		memset(ch,-1,sizeof(ch));
		memset(pos,0,sizeof(pos));
		nod.clear();
		l = 0;
		for(i = 0; i< C;i ++){
			scanf("%s",com);
			a = com[0] -'A';
			b = com[1] -'A';
			c = com[2] -'A';
			ch[a][b] = c;
			ch[b][a] = c;
		}
		scanf("%d",&D);
		for(i = 0; i < D;i ++){
			scanf("%s",com);
			a = com[0] - 'A';
			b = com[1] - 'A';
			pos[a] |= 1 << b;
			pos[b] |= 1 << a;
		}
		scanf("%d",&N);
		scanf("%s",com);
		l = 0;
		for(i = 0; i < N; i++){
			if(l == 0){
				a = com[i] - 'A';
				nod.st |= 1 << a;
				nod.cc[a]++;
				fin[l++] = a;
			}else{
				a = com[i] - 'A';
				b = fin[l-1];
				if(ch[a][b] != -1){
					fin[l-1] = ch[a][b];
					nod.cc[b] --;
					if(nod.cc[b] == 0){
						nod.st ^= 1 << b;
					}
					nod.st |= 1 << fin[l-1];
				}else if((nod.st & pos[a]) != 0){
					l = 0;
					nod.clear();
				}else{
					a = com[i] - 'A';
					nod.st |= 1 << a;
					nod.cc[a]++;
					fin[l++] = a;
				}
			}
		}
		printf("Case #%d: ",cas++);
		if(l == 0){
			printf("[]\n");

		}else{
			printf("[%c",fin[0]+'A');
			for(i = 1;i < l; i ++){
				printf(", %c",fin[i]+'A');
			}
			printf("]\n");
		}
	}
	return 0;
}
