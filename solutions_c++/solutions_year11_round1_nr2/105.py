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

int T;
string cad[10101];
int pierde[10101];
int ord[10101];

bool orden(int x,int y){
	if( pierde[x]!=pierde[y] ) return pierde[x] > pierde[y];
	return x<y;
}

vector<vint > v,w;

int main()
{
	cin >> T;
	f(cases,0,T){
		int n,m; cin >> n >> m;
		clr(pierde,0);
		f(i,0,n) ord[i] = i;
		
		f(i,0,n) cin >> cad[i];
		cout << "Case #"<<cases+1<<":";
		f(iii,0,m){
			string lista; cin >> lista;
			clr(pierde,0);
			v.clear(); w.clear();
			f(i,0,10) v.poner( vint(0,0) );
			f(i,0,n) v[ cad[i].size()-1 ].poner( i );
			
			f(i,0,lista.size()){
				char x = lista[i];
				int sz = 0;
				
				f(j,0,v.size()){
               map<int,int> ind;
					set<int> mask;
					vint M;
					f(k,0,v[j].size()){
						int m = 0;
						string s = cad[ v[j][k] ];
						f(t,0,s.size()){
							m<<=1;
							if( s[t]==x ) m++;
						}
						mask.insert(m);
						M.poner(m);
					}
					vint msk( all(mask) );
					f(k,0,msk.size()) ind[msk[k]] = k;
					f(k,0,msk.size()) w.poner( vint(0,0) );
					
					f(k,0,M.size()) w[sz+ind[M[k]] ].poner( v[j][k] );
					sz += msk.size();
					
					if( msk.back() ){
						f(k,0,M.size())if( M[k]==0 ) pierde[ v[j][k] ]++;// cout<<x;
					}
				}
//				cout << x << " " << w.size()<<endl;
				v.clear();
				v = w;
				w.clear();
			}
			
			f(i,0,n) ord[i] = i;
//			f(i,0,n) cout<<pierde[i]<<" "; cout<<endl;
			sort(ord,ord+n,orden);
			cout << " " << cad[ ord[0] ];
		}
		cout << endl;
	}
}
