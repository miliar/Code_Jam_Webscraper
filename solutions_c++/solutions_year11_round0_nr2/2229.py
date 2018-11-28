#include <cstdio>
#include <stack>

using namespace std;

char got['a']['a'];
char op['a']['a'];
char buc['a'];
stack <char> S;
char oak[1000];
char str[1000];

void newprob(int tt){
	for(int i='A';i<='Z';i++){
		buc[i] = 0;
		for(int j='A';j<='Z';j++){
			got[i][j] = 0;
			op[i][j] = 0;
		}
	}
	while(!S.empty())S.pop();
	int a; scanf("%d",&a);
	for(int i=0;i<a;i++){
		char tmp[4];
		scanf("%s",tmp);
		got[tmp[0]][tmp[1]] = tmp[2];
		got[tmp[1]][tmp[0]] = tmp[2];
	}
	int b; scanf("%d",&b);
	for(int i=0;i<b;i++){
		char tmp[4];
		scanf("%s",tmp);
		op[tmp[0]][tmp[1]] = 1;
		op[tmp[1]][tmp[0]] = 1;
	}
	int n; scanf("%d",&n);
	scanf("%s",str);
	for(int i=0;i<n;i++){
		if(!S.empty()){
			if(got[S.top()][str[i]] != 0){
				char old = S.top();
				buc[old]--;
				S.pop();
				buc[got[old][str[i]]]++;
				S.push(got[old][str[i]]);
			}else{
				bool ok = false;
				for(char c = 'A'; c <= 'Z';c++){
					if(buc[c] != 0 && op[str[i]][c] == 1){
						ok = true;
						while(!S.empty()){
							buc[S.top()] = 0;
							S.pop();
						}
					}
				}
				if(!ok){
					buc[str[i]]++;
					S.push(str[i]);
				}
			}
		}else{
			buc[str[i]]++;
			S.push(str[i]);
		}
	}
	int lev = 0;
	printf("Case #%d: [",tt);
	while(!S.empty()){
		oak[lev++] = S.top();
		S.pop();
	}
	if(lev == 0){
		printf("]\n");
		return;
	}
	for(int i=lev-1;i>=1;i--)printf("%c, ",oak[i]);
	printf("%c]\n",oak[0]);
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)newprob(i+1);
	return 0;
}

/*
1
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
*/
