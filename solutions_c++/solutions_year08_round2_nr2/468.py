#include <math.h>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define FOR(i,s,n) for (int i=(s);i<(n);i++)
#define ISS istringstream
#define OSS   ostringstream
typedef vector<int> VI;
typedef pair<int,int> PI;

int dx4[] = {-1, 1, 0 , 0};
int dy4[] = {0, 0, -1 ,1 };

int dx8[] = {-1, -1, -1,  0,  0,  1,  1,  1,};
int dy8[] = {-1,  0,  1, -1,  1, -1,  0,  1 };

template<class X,class Y> ostream &operator<<(ostream &s, pair<X,Y> p){s<<p.first<<'@'<<p.second;return s;}
template<class T> ostream &operator<< (ostream& o, vector<T> v) { o << "("; for (int i=0;i<(int)v.size();i++) o << (i?",":"") << v[i]; o << ")"; return o; }
#define vector_include(Item, Vector) (find(Vector.begin(), Vector.end(),Item ) != Vector.end())

int s[1001];

int primes[168] = { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997 };

int find(int i) {
	if(s[i]!=i)
        s[i]=find(s[i]);
	return s[i];
}

vector<int> primeFac(int i, int p) {
    vector<int> res;
    int j=0;
    while(primes[j] < i && j < 168) {
        if(! (i%primes[j]) && primes[j] >= p ) res.push_back(primes[j]);
        j++;
    }
    return res;
}

int solve(int a, int b, int p) {
    vector< vector<int> > pf(1001);
    FOR(i,a,b+1) {
        s[i] = i;
        pf[i] = primeFac(i,p);
    }
    FOR(k,0,168) {
        if(primes[k] < p) continue;
        FOR(i,a,b+1) {
            FOR(j,i+1,b+1) {
                    if(find(i) == find(j)) continue;
                    if( i % primes[k] == 0 && j % primes[k] == 0)
                        s[find(i)] = find(j);

            }
        }
    }

    set<int> w;
    FOR(i,a,b+1) w.insert(s[i]);
	return w.size();
}

int main() {
    int cases;
    cin >> cases;
	FOR(i,0,cases) {
	    int a,b,p;
	    cin >> a >> b >> p;
		cout << "Case #" << (i+1) << ": " <<  solve(a,b,p) << endl;
	}
}

