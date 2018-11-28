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

int H, W, NC;
int p[128][128];
int padre[11000];

int getp(int a){ return (padre[a] == -1) ? (a) : (padre[a] = getp(padre[a])); }
int une(int a, int b){ padre[getp(b)] = getp(a); }
inline int indi(int a, int b){ return (W*a + b); }

int sacap(int a, int b){
    int ea = 1000000;
    int inda=-1, indb=-1;
    if (a>0 && p[a-1][b] < ea){ inda = a-1; indb = b; ea = p[a-1][b]; }
    if (b>0 && p[a][b-1] < ea){ inda = a; indb = b-1; ea = p[a][b-1]; }
    if (b<W-1 && p[a][b+1] < ea){ inda = a; indb = b+1; ea = p[a][b+1]; }
    if (a<H-1 && p[a+1][b] < ea){ inda = a+1; indb = b; ea = p[a+1][b]; }
    
    //cout << "viendo " << a << ' ' << b << " --> " << inda << ' ' << indb << endl;
    if (ea<p[a][b]) { une(indi(inda, indb), indi(a, b)); }    
    
    return 0;
}

int main(){
    
    cin >> NC;
    forn(nc, NC){
        cin >> H >> W;  
        forn(i, H*W) padre[i] = -1;  
        forn (i, H) forn(j, W) cin >> p[i][j];
        forn(i, H) forn (j, W) sacap(i, j);
        int letra[11000];
        forn (i, H*W+1) letra[i] = -1;
        int ind = 0;
        forn(i, H) forn (j, W){
            int k = indi(i,j);
            if (letra[getp(k)] == -1){
                letra[getp(k)] = ind++;
            }
        }
        cout << "Case #" << nc+1 << ":" << endl;
        forn(i, H){
            forn (j, W){
                int k = indi(i,j);
                cout << char(letra[getp(k)] + 'a');
                if (j<W-1) cout << ' ';
                //if (char(letra[getp(k)] + 'a') == 'c') cout << "ERRORRRRRRRRRRRRRRRRRRRRR" << endl << endl;
            }
            cout << endl;
        }    
    }
    
    return 0;
}
