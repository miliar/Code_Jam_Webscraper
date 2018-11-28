#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
const int MaxN=200;

using namespace std;
int T,N;
char s[MaxN],Ans[MaxN];
char C[MaxN][MaxN],D[MaxN][MaxN];
int main(){
	scanf("%d", &T);
	for (int t=1;t<=T;t++){
		memset(C,0,sizeof(C));
		memset(D,0,sizeof(D));
		int c,d;
		cin >> c;
		for (int i=0;i<c;i++){
			char ch[10];
			cin >> ch;
			C[ch[0]][ch[1]]=ch[2];
			C[ch[1]][ch[0]]=ch[2];
		}
		cin >> d;
		for (int i=0;i<d;i++){
			char ch[10];
			cin >> ch;
			D[ch[0]][ch[1]]='A';
			D[ch[1]][ch[0]]='A';
		}
		cin >> N;
		cin >> s;
		int tot=0;
		for (int i=0;i<N;i++){
			Ans[tot++]=s[i];
			if (tot==1) continue;
			if (C[Ans[tot-2]][Ans[tot-1]]){
				Ans[tot-2]=C[Ans[tot-2]][Ans[tot-1]];
				tot--;
			}else{
				for (int j=tot-2;j>=0;j--)
				if (D[Ans[j]][Ans[tot-1]]){
					tot=0;
					break;
				}
			}
		}
		printf("Case #%d: [", t);
		for (int i=0;i<tot;i++){
			if (i) printf(", ");
			printf("%c", Ans[i]);
		}
		printf("]\n");
	}
	return 0;
}
