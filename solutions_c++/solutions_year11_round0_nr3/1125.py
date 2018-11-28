#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

#define pb push_back
#define fori(i, n) for ( int i = 0; i < (n); i++ )
#define forr(i, a, b) for ( int i = (a); i <= (b); i++ )
#define size(a) int((a).size())
#define all(x) (x).begin(),(x).end()
#define sorting(x) sort(all(x))
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end()
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define print_m(m) for(int i = 0;i<(int) m.size();i++) print_v(m[i]); cout << endl;
#define print_v(v) { for(int j = 0;j<(int) v.size();j++) cout << v[j] << " "; cout << endl; }
#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x " = " << x << "\n")

#define GRANDE 6000

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

int main()
{
    int T, N, teste;
    vector <int> L;
    
    teste = 0;
    
    cin >> T;
	while(teste++ < T){
        L.clear();
        
        cin >> N;
        int not_possible = 0;
        fori(i, N){
            int a;
            cin >> a;
            L.push_back(a);
            not_possible ^= a;
        }
        
        
        sort(all(L));
        int sum = 0;
        for(int i=1; i<size(L); i++){
            PRINT("I %d: %d\n",i,L.at(i));
            sum += L.at(i);
        }
        
        if(not_possible){
       		cout << "Case #"<< teste << ": NO" << endl;
        } else {
        	cout << "Case #"<< teste << ": " << sum << endl;
        }
	}
	
	return 0;
}
