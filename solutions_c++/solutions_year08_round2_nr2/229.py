#include <vector>
#include <list>
#include <map>
#include <set>
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


#include <string.h>
#include <stdlib.h>

using namespace std;
 
typedef long long int lint;
typedef pair<lint,lint> par;
 
#define sz size
#define pb push_back
#define all(x) (x).begin() , (x).end()
#define sqr(x) (x)*(x)
#define x first
#define y second
#define rep(i,n)  for (int (i)=0;(i)<(int)(n);(i)++)
#define Rep(i,a,n) for (int (i)=(int)(a);(i)<(int)(n);(i)++)

#define MAX 100000
#define MAX2 1010

char isprime[MAX];
int primos[MAX];
int tot=0;

struct st{
	int p[MAX2],rank[MAX2], number[MAX2];
	int size;
 
	void init(int s){
		size = s;
		for (int i = 0; i < size; i++) 
			{p[i]=i; rank[i]=0; number[i]=1;}
	}
 
	void link(int x, int y) {
		  if (rank[x] <= rank[y]) {
		    p[x] = y;
			number[y] += number[x];
		    if (rank[x] == rank[y])
		      rank[y]++;
		} else link(y, x);
	}
 
	int find_set(int x) {
	  if (x != p[x]) p[x] = find_set(p[x]);
	  return p[x];
	}
 
	void union_set(int x,int y) {
	  link(find_set(x), find_set(y));
	}
};



void cria_crivo() {
     rep(i,MAX)
	isprime[i]=0;
     isprime[0] = isprime[1] = 1;
     for (int i=2 ; i <= MAX ; i++)
         if (!isprime[i])
            for (int j=i+i;j<=MAX;j+=i)
                isprime[j]=1;
     rep(i,MAX)
	if (!isprime[i])
		primos[tot++]=i;
}

int main() {
	int C;
	cin >> C;
    	cria_crivo();
	rep(i,C) {
		st s;
		s.init(MAX2);
		int A,B,P;
		cin >> A >> B >> P;
		int first=0;
		while (primos[first]<P)
			first++;
		int mat[1001][100]={};
		int r[1001]={};
		Rep(j,first,tot) {
			if (primos[j]>B) break;
			int z=1;
			int num=primos[j];
			while (z*num<=B) {
				if (z*num>=A && z*num<=B)
					mat[z*num][r[z*num]++]=num;
				z++;
			}
		}
		Rep(j,A,B+1) {
			Rep(k,j+1,B+1) {
				int exist = 0;
				rep(l,r[j])
				rep(m,r[k])
					if (mat[j][l]==mat[k][m])
						exist=1;

				if (exist) {
					//cout << j << " " << k << endl;
					s.union_set(j,k);
				}
			}
		}

		set<int> ss;
		Rep(j,A,B+1)
			ss.insert(s.find_set(j));
		cout << "Case #" << i+1 << ": " << ss.sz() << endl;

	}
	return 0;
}

