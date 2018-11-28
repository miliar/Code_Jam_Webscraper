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


int N;
int cant[56];
int us[56];
int tot;

int main(){
    int NC;
    cin >> NC;
    
    forn(nc, NC){
        forn(i, 56) { us[i] = 0; cant[i] = 0;}
        tot = 0;
        cin >> N;
        forn(i,N){
            //int ind = 0;
            char k;
            forn(j,N){
                cin >> k;
                if(k=='1') cant[i] = j;
            }
        }     
        
        forn(i, N){
            for (int j=i; j<N; j++){
                if(cant[j] <= i){
                    tot += j-i;
                    for(int k=j; k>i; k--) swap(cant[k], cant[k-1]);
                    //cout << "fila " << i << " -> "  << j << endl; 
                    break;
                }
            }
        }
    cout << "Case #" << nc+1 << ": " << tot << endl;
    }
    return 0;
}

