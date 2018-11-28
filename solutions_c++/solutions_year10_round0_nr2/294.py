#include <cstdio>
#include <cstring>
#include <algorithm>

const int BAS = 10;
char s[1000];

struct Tlong{
	int a[128];

	Tlong () {
		memset(a, 0, sizeof(a));
		a[0] = 1;
	}

	Tlong (int aa) {
		memset(a, 0, sizeof(a));
		a[0] = 1;
		a[1] = aa;
	}
	
	void read(){
		memset(a, 0, sizeof(a));
		scanf(" %s ", s);
		a[0] = strlen(s);
		for (int i=1; i<=a[0]; ++i)
			a[i] = s[a[0] - i]-'0';
	}
	
	void write(){
		for (int i=a[0]; i>0; --i)
			printf("%d", a[i]);
			
	}

	Tlong operator * (const int other)const{
		Tlong res;
		res.a[0] = a[0] + 1;
		for (int i=1; i<=a[0]; ++i){                     
			res.a[i+1] = (res.a[i] + a[i] * other) / BAS;
			res.a[i] = (res.a[i] + a[i] * other) % BAS;
		}
		while (res.a[0]>1 && res.a[res.a[0]]==0)
			--res.a[0];
		return res;
	}

	bool operator <= (const Tlong &other)const{
		if (a[0] != other.a[0])
			return a[0] < other.a[0];
		for (int i=a[0]; i>0; --i){
			if (a[i] != other.a[i])
				return a[i] < other.a[i];
		}
		return 1;
	}       

/*	Tlong operator + (const Tlong &other)const{
		Tlong res;
		res.a[0] = std::max(a[0], other.a[0]) + 1;
		for (int i=1; i<=res.a[0]; ++i){                     
			res.a[i+1] = (res.a[i] + a[i] + other.a[i]) / BAS;
			res.a[i] = (res.a[i] + a[i] + other.a[i]) % BAS;
		}
		while (res.a[0]>1 && res.a[res.a[0]]==0)
			--res.a[0];
		return res;
	}*/

	Tlong operator - (const Tlong &other)const{
		Tlong res;
		res.a[0] = a[0];
		for (int i=1; i<=a[0]; ++i){                     
			res.a[i] = res.a[i] + a[i] - other.a[i];
			while (res.a[i] < 0){
				res.a[i] += BAS;
				--res.a[i+1];
			}
		}
		while (res.a[0]>1 && res.a[res.a[0]]==0)
			--res.a[0];
		return res;
	}
    /*             
	int operator % (const int other)const{
		int q = 0;
		for (int i=a[0]; i>0; --i){
			q = (q * BAS +a[i]) % other;
		}
		return q;
	}
*/
	Tlong operator / (const int other)const{
		Tlong res;
		res.a[0] = a[0];
		int q = 0;
		for (int i=a[0]; i>0; --i){
			res.a[i] = (q * BAS +a[i]) / other;
			q = (q * BAS +a[i]) % other;
		}
		while (res.a[0]>1 && res.a[res.a[0]]==0)
			--res.a[0];
		return res;
	}
	
	Tlong shift(int f)const{
		Tlong res;
		res.a[0] = a[0] + f;
		for (int i=a[0]; i>=1; --i)
			res.a[i+f] = a[i];
		return res;	
	}
	
	Tlong operator % (const Tlong other)const{
		Tlong res;
		for (int i=0; i<=a[0]; ++i){
			res.a[i] = a[i];
		}
		Tlong q;
		for (int i=a[0]-other.a[0]; i>=0; --i){
			q = other.shift(i);
			while (q <= res)
				res = res - q;
		}
		return res;	
	}
	
};

Tlong gcd(Tlong a, Tlong b){
	if (a.a[0] == 1 && a.a[1] == 0)
		return b;
	if (b.a[0] == 1 && b.a[1] == 0)
		return a;
	if (a.a[1] % 2 == 0 && b.a[1] % 2 == 0)
		return gcd(a/2, b/2) * 2;
	if (a.a[1] % 2 == 0)
		return gcd(a/2, b);
	if (b.a[1] % 2 == 0)
		return gcd(a, b/2);
	if (a <= b)
		return gcd(a, b-a);
	return gcd(a-b, b);
}

Tlong a[1024]; 
Tlong b[1024];

int main(){	
#ifndef ONLINE_JUDGE
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
#endif
	int ktest;
	
	scanf("%d", &ktest);
	
	for (int itest=0; itest<ktest; ++itest){
		printf("Case #%d: ", itest+1);
		int n;
		scanf("%d ", &n);
		for (int i=0; i<n; ++i)
			a[i].read();
			
		a[n] = a[0];
		
		for (int i=0; i<n; ++i){
			if (a[i] <= a[i+1])
				b[i] = a[i+1] - a[i];
			else
				b[i] = a[i] - a[i+1];
		}
		
		Tlong ans = b[0];
		for (int i=1; i<n; ++i)
			ans = gcd(ans, b[i]);
		
		Tlong res = a[0] % ans;
		if (res.a[0] == 1 && res.a[1] == 0)	
			res = ans;
			
		(ans-res).write();
		printf("\n");
		
			
//		int res = a[0] % ans;
//		if (res == 0)
//			res = ans;
//		printf("%d\n", ans - res);
	}	
		
    return 0;
}
