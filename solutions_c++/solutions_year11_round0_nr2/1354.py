#include <cstdio>
#include <vector>
#include <stack>

using namespace std;

char comb[30][30];
vector<char> ref[30];
stack<char> pilha;
stack<char> p2;
int esta[30];
char str[200];


int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int casos, a, b, n;
	scanf("%d", &casos);
	for(int t=1; t<=casos; t++){
		scanf("%d",&a);
		for(int i=0; i<30; i++){
			esta[i] = 0;
			ref[i].clear();
			for(int j=0; j<30; j++)
				comb[i][j] = 0;
		}
		for(int i=0; i<a; i++){
			scanf("%s",str);
			comb[str[0]-'A'][str[1]-'A'] = comb[str[1]-'A'][str[0]-'A'] = str[2];
		}
		
		scanf("%d",&b);
		for(int i=0; i<b; i++){
			scanf("%s",str);
			ref[str[0]-'A'].push_back(str[1]);
			ref[str[1]-'A'].push_back(str[0]);
		}
		
		scanf("%d",&n);
		scanf("%s",str);
		
		int cod, cod2;
		char ch;
		for(int i=0; i<n; i++){
			cod = str[i]-'A';
			if(pilha.empty()==false){
				ch = pilha.top();
				cod2 = ch - 'A';
				
				if(comb[cod][cod2] != 0){
					pilha.pop();
					pilha.push(comb[cod][cod2]);
					esta[cod2]--;
					esta[comb[cod][cod2]]++;
				}else{				
					bool tem = false;
					for(int j=0; j<ref[cod].size() && !tem; j++)
						tem |= (esta[ref[cod][j]-'A'] > 0);
					if(tem){
						while(!pilha.empty()){
							esta[pilha.top()-'A']--;
							pilha.pop();
						}
					}else{
						pilha.push(str[i]);
						esta[str[i]-'A']++;
					}
				}				
			}else{
				pilha.push(str[i]);
				esta[str[i]-'A']++;;
			}
		}
		while(pilha.empty()==false){
			p2.push(pilha.top());
			pilha.pop();
		}
		printf("Case #%d: [",t);
		while(p2.size()>1){
			printf("%c, ",p2.top());
			p2.pop();
		}
		if(p2.size()==1){
			printf("%c",p2.top());
			p2.pop();
		}	
		printf("]\n");
	}
}
