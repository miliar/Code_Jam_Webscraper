#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int n,m,test,cur = 1;
char s[10];
int order[1000],pos1,pos2,tim1,tim2;

int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	for ( scanf("%d",&test) ; cur <= test ; cur++ ){
		scanf("%d",&n);
		printf("Case #%d: ",cur);
		for ( int i = 0 ; i < n ; i++ ){
			scanf("%s %d",s,&m);
			if (s[0]=='O') order[i] = m; else order[i] = -m;
		}
		tim1 = 0;
		tim2 = 0;
		pos1 = 1;
		pos2 = 1;
		for ( int i = 0 ; i < n ; i++ ){
			if (order[i]>0){
				tim1 = max(tim2,tim1+abs(pos1-order[i]))+1;
				pos1 = order[i];
			} else {
				tim2 = max(tim1,tim2+abs(pos2+order[i]))+1;
				pos2 = -order[i];
			}
		}
		printf("%d\n",max(tim1,tim2));
	}
}
