#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define forn(i,n) for (int i=0; i<(int)(n); i++)
#define forsn(i,m,n) for (int i=(m); i<(int)(n); i++)

int NC;

int main(){
    cin >> NC;
    string ea = "welcome to code jam";
    string gato;
    getline(cin, gato);
    forn(nc, NC){
        int tot[24][512];
        memset(tot, 0, sizeof(tot));
        string p;
        getline(cin, p);
        int N = p.size();
        tot[0][0] = (p[0] == ea[0]) ? 1 : 0; 
        forsn (i, 1, N) tot[0][i] = tot[0][i-1] + (p[i] == ea[0]);
        //forn(i, N) cout << tot[0][i] << ' '; cout << endl; 
        forsn (i, 1, 19){
            //cout << "hasta " << i << endl;;
            forsn (j, i, N){
                tot[i][j] = tot[i][j-1];
                if (p[j] == ea[i]) tot[i][j] += tot[i-1][j-1];
                tot[i][j] %= 10000; 
                //cout << tot[i][j] << ' ';  
            }
            //cout << endl;
        }
        cout << "Case #" << nc+1 << ": ";
        int R = tot[18][N-1];
        cout << R/1000; R %= 1000;;
        cout << R/100; R %= 100;
        cout << R/10; R %= 10;
        cout << R << endl;
        
        
    }    
    return 0;
}
