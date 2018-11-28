#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define MaxN 100
#define MaxSize 26
int element[MaxN+5];
int size;
bool opposed[MaxSize+5][MaxSize+5];
int combine[MaxSize+5][MaxSize+5];
int c,d,n;
char s[MaxN+5];
void init(){
	memset(opposed,0,sizeof(opposed));
	memset(combine,-1,sizeof(combine));
	scanf("%d",&c);
	while (c--){
		scanf("%s",&s);
		combine[s[0]-'A'][s[1]-'A']=s[2]-'A';
		combine[s[1]-'A'][s[0]-'A']=s[2]-'A';
	}
	scanf("%d",&d);
	while (d--){
		scanf("%s",&s);
		opposed[s[0]-'A'][s[1]-'A']=1;
		opposed[s[1]-'A'][s[0]-'A']=1;
	}
	scanf("%d",&n);
	scanf("%s",&s);
}
void solve(){
	int i,j;
	size=0;
	for (i=0;i<n;i++){
		if (!size){
			element[size++]=s[i]-'A';
		}else{
			if (combine[element[size-1]][s[i]-'A']!=-1){
				element[size-1]=combine[element[size-1]][s[i]-'A'];
				continue;
			}
			for (j=0;j<size;j++){
				if (opposed[s[i]-'A'][element[j]]){
					break;
				}
			}
			if (j<size){
				size=0;
			}else{
				element[size++]=s[i]-'A';
			}
		}
	}
	printf("[");
	for (i=0;i<size;i++){
		if (i){
			printf(", ");
		}
		printf("%c",element[i]+'A');
	}
	printf("]\n");
}
int main()
{
//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);
//	freopen("data.txt","r",stdin);
	int t,i;
	scanf("%d",&t);
    for (i=1;i<=t;i++){
		printf("Case #%d: ",i);
        init();
		solve();
    }
    return 0;
}