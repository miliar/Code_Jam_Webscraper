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



double do_sort(int n){
    if(n == 1){
        return 0.0;
    }
    if(n == 2){
        return 2.0;
    }
    if(n == 3){
        return 3.0;
    }
    return 1.0*n;
}
/*
double prob(int n, int acc){
    if(n == 1) return acc+1;
    
    return (n*1.0/n
}*/

int main()
{
    int T, N, teste;
    vector <int> L;
    vector <int> L_sorted;
    
    teste = 0;
    cin >> T;
	while(teste++ < T){
        L.clear();
        L_sorted.clear(); 
        
        cin >> N;
        fori(i, N){
            int a;
            cin >> a;
            L.push_back(a);
            L_sorted.push_back(a);
        }
        
        sort(all(L_sorted));
        int diffs = 0;
        fori(i, size(L)){
            if(L.at(i) != L_sorted.at(i))
                diffs++;
        }
        
        printf("Case #%d: %.6f\n", teste, do_sort(diffs) );
	}
	
	return 0;
}
