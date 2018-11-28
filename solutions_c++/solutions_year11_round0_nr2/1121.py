#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
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
#define vint vector<int>
#define clr(A,x) memset(A,x,sizeof(A))
#define CLR(v) f(i,0,n) v[i].clear()
#define oo (1<<30)
#define ones(x) __builtin_popcount(x)
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define poner push_back
#define eps (1e-9)
using namespace std;

int T,C,D,N,len;
string combine[100], clear[100], cad;
map< string,char > sumar;
map<char,char> opuesto;

int main()
{
	cin >> T;
	f(cases,0,T){
		sumar.clear();
		opuesto.clear();
		string pila(1000,0);
		int sz = 0;
		cin >> C;
		f(i,0,C){
			cin >> combine[i];
			string ab = combine[i].substr(0,2);
			sumar[ab] = combine[i][2];
			reverse( all(ab) );
			sumar[ab] = combine[i][2];
		}
		cin >> D;
		f(i,0,D){
			cin >> clear[i];
			opuesto[ clear[i][0] ] = clear[i][1];
			opuesto[ clear[i][1] ] = clear[i][0];
		}
		cin >> len;
		cin >> cad;
		
		printf("Case #%d: ",cases+1 );
		
		f(t,0,len){
			pila[sz++] = cad[t];
			if( sz>=2 && sumar.count( pila.substr(sz-2,2) ) ){
				char c = sumar[ pila.substr(sz-2,2) ];
				sz-=2;
				pila[sz++] = c;
			}else{
				f(i,0,sz)if( pila[i]==opuesto[ cad[t] ] ){
					sz = 0;
					break;
				}
			}
		}
		printf("[");
		f(i,0,sz){
			if( i ) printf(", ");
			printf("%c", pila[i] );
		}
		printf("]\n");
	}
}
