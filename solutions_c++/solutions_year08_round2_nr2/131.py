/* CopyRight (c) cnHawk */
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <string>
#include <vector>
#include <ctime>
#include <map>
#include <set>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;
const int M = 1024*1024;
int prime[M];
int pp[M], pnum;

void init(){
    memset(prime, -1, sizeof(prime));
    pnum = 0;
    int i, j;
    prime[0] = prime[1] = 0;
    for(i = 2; i < 1024; i++){
        if(prime[i]){
            for(j = i * i; j < M; j+=i){
                prime[j] = 0;
            }
        }
    }
    for(i = 2; i < 1000000; i++){
        if(prime[i]) pp[pnum++] = i;
    }
    //printf("pnum = %d\n", pnum);
}

/* disj set */
int father[M]; 
void DisjointSet(int n){//init
	int i;
	for(i = 0; i <= n; i++){
		father[i] = i;
	}
}
int FindRoot(int i, int depth = 0){
    //if(depth > 10)perror("max!!!!!!!!!11\n");
	if(father[i] == i)return i;
	father[i] = FindRoot(father[i], depth+1);
	return father[i];
}
void Merge(int y, int x){
	x = FindRoot(x);
	y = FindRoot(y);
	father[y] = x;
}
bool JudgeSet(int x, int y){
	return FindRoot(x) == FindRoot(y);
}

char snote[1024];

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("b.out", "w",stdout);
    //freopen("err.out", "w",stderr);
    init();
    int kase, N;
    scanf("%d", &N);
    for(kase = 1; kase <= N; kase++){
        LL A, B, P, prev;
        int m, i;
        scanf("%I64d%I64d%I64d", &A, &B, &P);
        DisjointSet((int)(B-A));
        //while(1);
        LL j;
        for(i = 0; i < pnum && pp[i] < (int)(B-A); i++){
            if((LL)pp[i] < P) continue;
            m = pp[i];
            j = A/m*m;
            if(j < A) j+=(LL)m;
            prev = j;
            j += (LL)m;
            //sprintf(snote, "AB=%I64d,%I64d,  m = %d, j=%I64d", A, B, m, j);
            //perror(snote);
            for(; j <= B; j+=(LL)m){
                Merge(int(j-A), int(prev-A));
            }
            //printf(snote, "AB=%I64d,%I64d,  m = %d, *******j=%I64d", A, B, m, j);
            //perror(snote);
        }
        int ans = 0;
        for(i = 0; i <= (int)(B-A); i++){
            if(father[i] == i) ans++;
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    //fprintf(stderr, "Clock: %d\n", clock()/CLOCKS_PER_SEC);
    return 0;
}
                
            
            
            
            
            
            
            
        
