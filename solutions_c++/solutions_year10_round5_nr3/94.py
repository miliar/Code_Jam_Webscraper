#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <climits>
#include <cmath>
#include <cctype>
#include <sstream>
#include <map>
#include <set>
#include <cstdio>
#include <queue>
#define f(i,x,y) for(int i=x;i<y;i++)
#define fd(i,y,x) for(int i=y;i>=x;i--)
#define ll long long
#define clr(A,x) memset(A,x,sizeof(A))
#define oo 1<<30
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
using namespace std;
int lim = -2000000;


int main(){
	int T; cin >> T;
	f(t,1,T+1){
		set<int> A;
		int n; cin >> n;
		map<int, int> p;
		
		
		f(i,0,n){
			int a, b; scanf("%d %d", &a, &b);
			p[a] = b;
			if(b > 1) A.insert(a);
		}
		int veces = 0;
		
		while(!A.empty()){
         int z;
			int indice = *A.begin();
			veces += p[indice] / 2;
			p[indice - 1] += p[indice]/2;
			p[indice + 1] += p[indice]/2;
			//cout<<veces<<endl;
			p[indice] %= 2;
			if(p[indice] == 0) p.erase(indice);
			A.erase(indice);
			if(p[indice - 1] > 1) A.insert(indice - 1);
			if(p[indice + 1] > 1) A.insert(indice + 1);
		}
		printf("Case #%d: %d\n", t, veces);
	}
}
