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
typedef pair<int,int> pii;

#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define present(container, element) (container.find(element) != container.end()) 
#define cpresent(container, element) (find(All(container),element) != container.end()) 



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

const double pi = 2*acos(0.0);
const double eps = 1e-9;

int s2i(string &s){
  int x;
  sscanf(s.c_str(), "%d", &x);
  return x;
}
        /* 
        vector<string> nazwy;
        
        string s;
        int n=0;
        while (1){
      cin >> s;
      if (!isdigit(s[0])) nazwy.pushback(s);
      else break;
    }
    ceny[0]=atoi(s.c_str());
    */



int main() {
	freopen("input2.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d\n", &t);
	For(test, 1, t) {
              
            
			
			vi list;
			int c;
			c = getchar();
			
			while(c>='0' && c<='9' )
			{
				list.push_back( int(c-'0'));
				c=getchar();
			
			}
            
			if(! next_permutation( All(list)))
            {
                sort(All(list));
                //if(list[0])
                list.insert( list.begin() +1, 0) ;
                int i =0;
                while(! list[i])
                {
                              i++;
                              
                              }
                list[0] = list[i];
                list[i] = 0;
                
                
                }             
		
		
		
		
		
		printf("Case #%d: ", test);
		
		FOREACH(it, list)
		{
		            cout<< (*it);
                    }
              cout<< endl;
		
	}

	exit(0);
}
