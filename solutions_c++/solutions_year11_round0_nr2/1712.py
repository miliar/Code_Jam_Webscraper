#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;

int t, top;
char st[200], com[26][26], str[200], a, b, A='A';
bool opp[26][26];

int main(){
	int time=0, i, j, n;
	scanf("%d", &t);
	while(t--){
		memset(com, 0, sizeof(com));
		memset(opp, 0, sizeof(opp));
		top=0;
		scanf("%d", &n);
		while(n--){
			scanf(" %s", str);
			com[str[0]-A][str[1]-A]=com[str[1]-A][str[0]-A]=str[2];
		}
		scanf("%d", &n);
		while(n--){
			scanf(" %s", str);
			opp[str[0]-A][str[1]-A]=opp[str[1]-A][str[0]-A]=1;
		}
		scanf("%d %s", &n, str);
		for(i=0; i<n; i++){
			if(top>0&&com[st[top-1]-A][str[i]-A]){
				st[top-1]=com[st[top-1]-A][str[i]-A];
			}
			else{
				st[top++]=str[i];
				for(j=0; j<top-1; j++)
					if(opp[st[j]-A][str[i]-A]){
						top=0;
						break;
					}
			}
		}
		printf("Case #%d: [", ++time);
		if(top>0){
			printf("%c", st[0]);
			for(i=1; i<top; i++)
				printf(", %c", st[i]);
		}
		puts("]");
	}
    return 0;
}
