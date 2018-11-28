#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include <queue>

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
    int N, M, teste;
    char c;
    queue <int> L_O, L_B;
    queue <char> L;
    teste = 0;
    
    cin >> N;
	while(teste++ < N){
        while (!L.empty() || !L_B.empty() || !L_O.empty())
        {
            L_O.pop();
            L_B.pop();
            L.pop();
        }
        
        cin >> M;
        
        fori(i,M){
            int p;
            cin >> c >> p;
            if(c == 'O'){
                L_O.push(p);
            } else if(c == 'B') {
                L_B.push(p);
            } else {
                fprintf(stderr, "ERRO!\n");
            }
            L.push(c);
        }
        
        int seg = 0;
        int pO = 1, pB = 1;
        int pressed = 0;
        while(!L.empty()){
            seg++;
            pressed = 0;
            
            PRINT("TIME %d: ", seg);
            //Moving BLUE
            if(size(L_B) != 0){
                int go = L_B.front();
                
                if(go > pB){
                    pB++;
                    PRINT("Blue moves to %d", pB);
                } else if(go < pB){
                    pB--;
                    PRINT("Blue moves to %d", pB);
                } else {
                    //press button if it's my time
                    if(L.front() == 'B'){
                        //Pressing the button
                        PRINT("Blue press button %d", go);
                        L.pop();
                        L_B.pop();
                        pressed = 1;
                    }  else {
                        PRINT("Blue waits at %d", pB);
                    }
                }
            }
            PRINT(" and ");
            //Moving ORANGE
            if(size(L_O) != 0){
                int go = L_O.front();
                
                if(go > pO){
                    pO++;
                    PRINT("Orange moves to %d", pO);
                } else if(go < pO){
                    pO--;
                    PRINT("Orange moves to %d", pO);
                } else {
                    //press button if it's my time
                    if(pressed) continue;
                    if(L.front() == 'O'){
                        //Pressing the button
                        PRINT("Orange press button %d", go);
                        L.pop();
                        L_O.pop();
                    } else {
                    PRINT("Orange waits at %d", pO);
                    } 
                }
            }
            PRINT("\n");
        }
        
		cout << "Case #"<< teste << ": " << seg << endl;
	}
	
	return 0;
}
