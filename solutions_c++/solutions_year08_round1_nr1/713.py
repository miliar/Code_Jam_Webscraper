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

#define Foreach(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define Add(v, b) v.push_back(b)
#define Del(v, i) v.erase(v.begin()+i)
#define Getp(v, i) (*v)[i]
#define Get(v, i) (v)[i]
#define ST first
#define ND second



typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

typedef pair<int,int> pii;
typedef pair<string,int> psi;
typedef pair<int, string> pis;
typedef pair<double, double> pdd;
typedef pair<string,double> psd;
typedef pair<double, string> pds;


typedef double** mx;

template<typename T> inline T pot2(T a) { return a*a; }
template<typename T> inline T pot(T a, int n) { T total=1; Rep(i, n){ total*=a; } return total; }

template<typename T> inline int size(const T& c) { return (int)c.size(); }
template<typename T> inline void ckmin(T& a, T b) { if (b < a) a = b; }
template<typename T> inline void ckmax(T& a, T b) { if (b > a) a = b; }

template<typename T> inline void sort(T& v){ std::sort(All(v));}
template<typename T> inline void reverse(T& v){	std::reverse(All(v));}
	
	
bool comparable(const int var1,const int var2){ 	if(var1>var2)	return true;	return false; } 	

template<typename T> inline void sortd(T& v){	std::sort(v.begin(), v.end(), comparable);}
template<typename T> inline void show(T& v){	For(i, 0, v.size()-1)	cout<<Get(v, i);	}


//lectura de datos
int readTime() {
	int h, m;
	scanf("%d:%d", &h, &m);
	return m+60*h;
}

char buf[1024*1024];
int readi(){ int d; scanf("%d", &d);   return d; }
float readf(){ float d; scanf("%f", &d);   return d; }
void reads(char* buf){ gets(buf); }

void Tokenize(const string& str,  vector<string>& tokens,	const string& delimiters = " "){    
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);    
	string::size_type pos     = str.find_first_of(delimiters, lastPos);
	while(string::npos != pos || string::npos != lastPos)	{        
		tokens.push_back(str.substr(lastPos, pos - lastPos));        
		lastPos = str.find_first_not_of(delimiters, pos);        
		pos = str.find_first_of(delimiters, lastPos);
	}
}

#define INF 1e10

template<typename T,  typename E> inline int putInMap(T s, map<T,E> mapa){
	int index=mapa.count(s);
	if(index>0) return mapa[s];
	index=mapa.size();
	mapa[s]=index;
	return index;
}
            
          
       
           
int main(int argc, char *argv[])
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	
	
	char buf[1024*1024];
	
	reads(buf);
	int num=atoi(buf);
	                    
	For(test, 1, num) {	
					
		//leemos
		reads(buf);
		int n=atoi(buf);
		vi A(n), B(n);
		Rep(i, n){ A[i]=readi();	}
		reads(buf);
		Rep(i, n){ B[i]=readi();}
		reads(buf);
		
		sort(A);
		sortd(B);
		long long val=0;
		Rep(i,n){ val=val+(A[i]*B[i]);}
		
		
		printf("Case #%d: %d", test, val);
		printf("\n");
	
	}	                  

	return EXIT_SUCCESS;
}  