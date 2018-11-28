#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include <deque>

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
    int T, C, D, N, teste;
    char par[27];
    char pair_sub[27];
    vector < pair<char,char> > opposed;
    deque <char> L;
    
    teste = 0;
    
    cin >> T;
	while(teste++ < T){
        fori(i, 27){
            par[i] = -1;
            pair_sub[i] = -1;
        }
        
        opposed.clear();
        L.clear();
        
        cin >> C;
        fori(i, C){
            char c1, c2, c3;
            cin >> c1 >> c2 >> c3;
            par[c1 - 'A'] = c2;
            par[c2 - 'A'] = c1;
            pair_sub[c1 - 'A'] = pair_sub[c2 - 'A'] = c3;
            PRINT("SUB pair: %c %c -> %c\n", c1, c2, c3);
        }
        
        cin >> D;
        fori(i, D){
            char c1, c2;
            cin >> c1 >> c2;
            opposed.push_back( make_pair(c1,c2) );
            PRINT("Opposed pair: %c %c\n", c1, c2);
        }
                
        PRINT("------------------\n");
        
        cin >> N;
        PRINT("Reading %d\n",N);
        fori(i, N){
            char c;
            cin >> c;
            PRINT("Invoking %c\n",c);
            //trying substitution
            int again;
            do{
                again = 0;
                if(size(L)==0){
                    L.push_front(c);
                    break;
                }
                char c1 = L.front();
                
                if(par[c1-'A'] == c){
                    again = 1;
                    L.pop_front();
                    PRINT("Substituing pair %c %c with \'%c\'\n", c1, c, pair_sub[c-'A']);
                    c = pair_sub[c-'A'];
                } else {
                    L.push_front(c);
                }
            }while(again);
            
            //Trying to clear the list
            fori(j,size(opposed)){
                int found_1, found_2;
                found_1 = found_2 = 0;
                
                char c1 = opposed.at(j).first;
                char c2 = opposed.at(j).second;
                
                fori(k,size(L)){
                    if(L.at(k) == c1) found_1 = 1;
                    if(L.at(k) == c2) found_2 = 1;
                }
                
                if(found_1 && found_2){
                    PRINT("Cleaning -> found opposed par %c %c\n",c1,c2);
                    L.clear();
                }
            }
        }
        
		cout << "Case #"<< teste << ": ";
		cout << "[";
		if(size(L)>0){
		  cout << L.at(size(L)-1);
		}
		for(int i=size(L)-2; i>=0; i--){
		  cout << ", " << L.at(i);
		}
		cout << "]" << endl;
		PRINT("------------------\n\n\n");
	}
	
	return 0;
}
