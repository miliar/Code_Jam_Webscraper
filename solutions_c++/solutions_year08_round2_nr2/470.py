#include <iostream>

using namespace std;

#define MAX 1000 
#define _min(a,b) (a) < (b) ? (a) : (b)

int p[MAX],rank[MAX+1];
bool isprime[MAX+1];

void make_set(int x) {
  p[x] = x;
  rank[x] = 0;
}

void link(int x,int y) {
  if (rank[x] > rank[y])
    p[y] = x;
  else {
    p[x] = y;
    if (rank[x] == rank[y])
      rank[y] = rank[y] + 1;
  }
}

int find_set(int x) {
  if (x != p[x])
    p[x] = find_set(p[x]);
  return p[x];
}

void union_set(int x,int y) {
  link(find_set(x),find_set(y));
}

void sieve()
{
 	int i, j;
	for(i = 2; i <= MAX; i++) isprime[i] = true;
	
	for(i = 3; i <= MAX; i += 2) 
		if(isprime[i]) {  
			for(j = 3; j <= (MAX/i); j += 2)		  
				  isprime[j*i] = false;
		} 
}

inline void clear() 
{
 	for(int i = 0; i <= MAX; i++) rank[i] = 0, p[i] = -1;
}

int main()
{
 	int t; cin >> t;
 	int a, b, p;
 	int i, j, k;
 	
 	sieve();	
 	
 	for(int _case = 1; _case <= t; _case++) {
			
		cin >> a >> b >> p;	
		clear();
		for(i = a; i <= b; i++) make_set(i);
		
		for(i = a; i <= b; i++)
            for(j = i+1; j <= b; j++) {
				//if(j == i) continue;
				for(k = _min(i, j); k >= p; k--) {
					if( !(k == 2 || (k % 2 != 0 && isprime[k])) ) continue;
		  		    if(i % k == 0 && j % k == 0) {
						   union_set(i,j);
						   break;
					}
				}
			}
			
		int ans = 0;
		for(i = a; i <= b; i++)	if(find_set(i) == i) ans++;
		
		cout << "Case #" << _case << ": " << ans << endl;
	}
				  
}
