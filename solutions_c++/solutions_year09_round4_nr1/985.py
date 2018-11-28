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
#define WATCH(x) trace(cout << #x " = " << x << "\n")

#define GRANDE 6000

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

int vec[GRANDE];
int resp;

void troca(int i, int j){
	PRINT("TROCA at %d,%d - %d com %d\n",i,j,vec[i],vec[j]);
	int aux = vec[j];
	vec[j] = vec[i];
	vec[i] = aux;
	resp++;
}

int main()
{
	int testes;
	cin >> testes;
	fori(t, testes){
		resp = 0;
		int N;
		cin >> N;
		fori(i,N){
			vec[i] = 0;
		}
		
		WATCH(N);
		
		int aux; char c;
		fori(i,N){
			fori(j,N){
				cin >> c;
				while(c == '\n'){ cin >> c; }
				if(c == '1'){
					vec[i] = j;
				}
			}
		}
		
		fori(i,N) PRINT("%d ", vec[i]);
		PRINT("\n");
		
		for(int i=0; i<N; i++){
			if(vec[i] > i){
				//find someone good and put there...
				int j=i+1;
				for(j=i+1; j<N; j++){
					if(vec[j] <= i) break;
				}
				//bring down j
				for(int z = j; z > i; z--){
					troca(z,z-1);
				}
			}
		}
		
		fori(i,N) PRINT("%d ", vec[i]);
		PRINT("\n");
		
		cout << "Case #"<< t+1 << ": " << resp << endl;
	}
	return 0;
}