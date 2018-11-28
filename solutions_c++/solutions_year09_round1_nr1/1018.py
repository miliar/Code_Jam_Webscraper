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

int64 convert( int& sum, int b)
{
	int64 result=0;
	int64 n=1;
	int i=sum;
	sum=0;
	
	while( i >0)
	{
		sum+= (i%b)*(i%b);
		result += ((i%b)* n);
		i=i/b;
		n=n*10;
	
	}
	
	return result;

}

int main() {
	freopen("input.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int t;
	scanf("%d\n", &t);
	For(test, 1, t) {
              
		string s;
       getline(cin, s, '\n');
	   
	   stringstream buffer;
	   buffer.str(s);
	   vi bases;
	   while (! buffer.eof()){
	   
			int a=0;;
	   
			buffer>> a;
	   
			if( (a!=2) && (a!=4) )
			{
			   bases.push_back(a);
			}
		
		}
		int ans=2;
		
		//vi vals(0, bases.size() );
		int siz = bases.size();
		while(1)
		{
			int match =0;
                FOREACH(IT, bases)
		        {
					int base = *IT;
					
					
					if ( base ==3)
					{
						int sum=ans;
						while(1)
						{
							int64 x = convert( sum, 3);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==2)||(x ==11)||(x ==12)||(x ==22))
							{
								break;
							}
							
						}
						
					}
					if ( base ==5)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 5);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==4)||(x ==20)||(x ==31)||(x ==23)||(x ==33))
							{
								break;
							}
						
						}
					
					}
					if ( base ==6)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 6);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==32)||(x ==21)||(x ==5)||(x ==41)||(x ==25)||(x ==45)||(x ==105)||(x ==42))
							{
								break;
							}
						
						}
					
					}
					
					if ( base ==7)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 7);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==2)||(x ==4)||(x ==22)||(x ==11)||(x ==34)||(x ==13)||(x ==23)||(x ==16)||(x ==52)||(x ==41)||(x ==63)||(x ==44))
							{
								break;
							}
						
						}
					
					}
					if ( base ==8)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 8);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==4)||(x ==20)||(x ==5)||(x ==31)||(x ==12)||(x ==32)||(x ==15)||(x ==24)||(x ==64))
							{
								break;
							}
						
						}
					
					}
					if ( base ==9)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 9);
							if(sum ==1)
							{
								match++;
								break;
							}
							if((x ==55)||(x ==58)||(x ==108)||(x ==72)||(x ==58)||(x ==45)||(x ==75)||(x ==82))
							{
								break;
							}
						
						}
					
					}
					
					if ( base ==10)
					{
						int sum=ans;
						while(1)
						{
							
							int64 x = convert( sum, 10);
							int myints[] = {1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100 };
							vi poss(myints, myints + (sizeof(myints) / sizeof(int)) ) ;
							if( cpresent(poss,sum) )
							{
								match++;
								break;
							}
							if( sum<100)
							{
                                break;
                                }
							
						
						}
					
					}
		
		
		
		        }
			
			if(match == bases.size() )
				break;
		  
			ans++;
		  }		 
		
		
		
		
		
		printf("Case #%d: %d\n", test, ans);
	}

	exit(0);
}
