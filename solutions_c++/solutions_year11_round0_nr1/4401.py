#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;
#define f first
#define s second
#define mp make_pair
typedef long long ll;
int T,n,t,pos,l,L,r,R,cpO,cpB;
pair<int,int>P[1000],Q[1000];
char ch;
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d\n",&T); 
	for(int test=1;test<=T;test++){
		l=L=r=R=0;
		scanf("%d ",&n); 		
		for(int i=1;i<=n;i++){
			scanf("%c %d ",&ch,&pos);
			if(ch=='O') 	P[r++]=mp(pos,i);
			else 		Q[R++]=mp(pos,i);
		}
		P[r].s=Q[R].s=(1<<29);
		cpO = cpB =1;
		for(t=0;l<r || L<R;t++){
			if(P[l].s<Q[L].s){
				if(Q[L].f>cpB) cpB++; if(Q[L].f<cpB) cpB--;
				if(P[l].f==cpO){ l++; continue;}
				if(P[l].f>cpO) cpO++; if(P[l].f<cpO) cpO--; 			
			}else{
				if(P[l].f>cpO) cpO++; if(P[l].f<cpO) cpO--;
				if(Q[L].f==cpB){ L++; continue;}
       				if(Q[L].f>cpB) cpB++; if(Q[L].f<cpB) cpB--;
			}
		}
		printf("Case #%d: %d\n",test,t);
	}
}
