#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>

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
#define trace(x...)
#define PRINT(x...) trace(printf(x))
#define watch(x) trace(cout << #x " = " << x << "\n")

#define GRANDE 6000

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

vector<int> release;
int prisao[10000];
int main()
{
	int T, P, Q, aux;
// 	scanf("%d\n", &T);
	cin >> T;
	for(int teste=1; teste<=T; teste++){
		cin >> P >> Q;
// 		scanf("%d %d\n",&P, &Q);
		
		
		release.clear();
		fori(i,Q){
			cin >> aux;
			release.pb(aux);
		}
		
		PRINT("Release: -");
			fori(i,size(release)){
				PRINT("%d - ",release[i]);
			}
		PRINT(".\n");
		
		int min_custo = INF;
		int custo = 0;
		do {
			PRINT("Release: -");
			fori(i,size(release)){
				PRINT("%d - ",release[i]);
			}
			PRINT(".\n");
			
			fori(i,10000) prisao[i] = 1;
			custo = 0;
			fori(i,size(release)){	//libertando a negada em ordem
				PRINT("Libertando %d\n",release[i]);
				prisao[release[i]] = 0;
				for(int j = release[i]+1; j<=P; j++){
					if(prisao[j] == 0){
						PRINT("ub stop at j=%d\n",j);
						break;
					}
					custo++;
				}
				for(int j = release[i]-1; j>0; j--){
					if(prisao[j] == 0){
						PRINT("lb stop at j=%d\n",j);
						break;
					}
					custo++;
				}
			}
			if(min_custo > custo) min_custo = custo;
			PRINT("CUSTO (P:%d,Q:%d) %d. MIN: %d\n",P,Q,custo, min_custo);
		} while ( next_permutation ( all(release) ) );
		printf("Case #%d: %d\n",teste,min_custo);
	}
	return 0;
}