#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

template<typename T> inline T sqr(T a) { return a*a; }
template<typename T> inline int Size(const T& c) { return (int)c.size(); }
template<typename T> inline void checkMin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void checkMax(T& a, T b) { if (b > a) a = b; }

struct para{
long long x,y;
};

long long i,j,k,l,p,o,m,n,g,N,x,y,A,B,C,D,M;
para pom;

int main() {
cin>>N;
vector<para> lista;
for(i=0;i<N;i++)
	{
	cin>>n;
	cin>>A;
	cin>>B;
	cin>>C;
	cin>>D;
	cin>>pom.x;
	cin>>pom.y;
	cin>>M;
	lista.push_back(pom);
        for(j=1;j<n;j++)
          {
          pom.x=((A * pom.x) + B)%M;
          pom.y = ((C * pom.y) + D)%M;
          lista.push_back(pom);
          }
        m=0;
        for(k=0;k<n;k++)
          for(l=k+1;l<n;l++)
            for(p=l+1;p<n;p++)
              {
              o=lista[k].x+lista[l].x+lista[p].x;
              g=lista[k].y+lista[l].y+lista[p].y;
              if (((o%3)==0)&&((g%3)==0)) m++;
              }
        cout<<"Case #"<<(i+1)<<": "<<m<<endl;
        lista.clear();
	}
}
