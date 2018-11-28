/*
TASK: G2011_Q_2 - Magicka
LANG: C++
NAME: untitled.cpp
*/
#include <cstdio>
#include <algorithm>

#define CMAX 36
#define DMAX 28
#define NMAX 110

using namespace std;

struct COMB
{
	char x,y,z;
};
struct OPS
{
	char x,y;
};

COMB comb[CMAX];
OPS ops[DMAX];
char table[NMAX],ret[NMAX];
int flags[30];

bool check(int index,char c1,char c2)
{
	return (comb[index].x==c1&&comb[index].y==c2)||(comb[index].x==c2&&comb[index].y==c1);
}

void func()
{
	int c; scanf("%d",&c);
	for(int i=0;i<c;i++){
		scanf("\n%c%c%c",&comb[i].x,&comb[i].y,&comb[i].z);
	}

	int d; scanf("%d",&d);
	for(int i=0;i<d;i++){
		scanf("\n%c%c",&ops[i].x,&ops[i].y);
	}

	//int n,cnt=0; scanf("%d%s",&n,table);
	//char prev='#';
	//for(int i=0;i<n;i++){
	//	//combine
	//	bool cmb=false;
	//	for(int j=0;j<c;j++){
	//		if(check(j,prev,table[i])){
	//			prev = ret[cnt-1] = comb[j].z;
	//			cmb = true;
	//			break;
	//		}
	//	}
	//	if(!cmb){
	//		prev = ret[cnt++] = table[i];
	//	}

	//	//oppose
	//	for(int j=0;j<d;j++){
	//		for(int k=0;k<cnt-1;k++){
	//			if((ops[j].x==ret[k]&&ops[j].y==ret[cnt-1])||(ops[j].y==ret[k]&&ops[j].x==ret[cnt-1])){
	//				prev = '#'; cnt = 0;
	//				break;
	//			}
	//		}
	//	}
	//}

	//printf("[");
	//for(int i=0;i<cnt;i++){
	//	if(0!=i) printf(", ");
	//	printf("%c",ret[i]);
	//}
	//printf("]\n");

	int n,cnt=0; scanf("%d",&n); table[cnt++] = 'Z'+1;
	fill(flags,flags+30,0);
	for(int i=0;i<n;i++){
		//combine
		char ch; scanf("\n%c",&ch);
		for(int j=0;j<c;j++){
			if(check(j,table[cnt-1],ch)){
				ch = comb[j].z;
				cnt--; flags[table[cnt]-'A']--;
				break;
			}
		}
		flags[ch-'A']++; table[cnt++] = ch;

		//oppose
		for(int j=0;j<d;j++){
			if((ch==ops[j].x&&0!=flags[ops[j].y-'A'])||(ch==ops[j].y&&0!=flags[ops[j].x-'A'])){
				cnt = 1;
				fill(flags,flags+30,false);
				break;
			}
		}
	}

	printf("[");
	for(int i=1;i<cnt;i++){
		if(1!=i) printf(", ");
		printf("%c",table[i]);
	}
	printf("]\n");

	return;
}

int main()
{
	FILE *fin=NULL,*fout=NULL;
	fin = freopen("input.txt","r",stdin);
	fout = freopen("output.txt","w",stdout);

	int t; scanf("%d",&t);
	for(int i=0;i<t;i++){
		printf("Case #%d: ",i+1);
		func();
	}

	//finalize
	if(NULL!=fin) fclose(fin);
	if(NULL!=fout) fclose(fout);

	return 0;
}