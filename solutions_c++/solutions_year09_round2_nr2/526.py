#include <iostream>
#include <vector>
#include <string>
#include <sstream>
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


int main(){
    int NC;
    string tmp;
    vi N;
    char c;
    
    cin >> NC;
    forn(nc, NC){
        N.clear();
        cout << "Case #" << nc+1 << ": ";
        cin >> tmp;
        stringstream in(tmp);
        while(in >> c) N.pb(int(c-'0'));
        
        //forn(i,sz(N)) cout << N[i]; cout << endl;
        
        int a = -1, b = -1;
        for(int i=sz(N)-1; i>=0; i--){
            for(int j=i-1; j>=0; j--){
                if(N[j]<N[i] && (a==-1 || j>a || (j==a && N[i]<N[b]) ) ){ a=j; b=i; }
            }
        }
        //cout << a << ' ' << b << endl;
        if(a!=-1){
            swap(N[a], N[b]);
            sort(N.begin()+a+1, N.end());
            forn(i,sz(N)) cout << N[i]; cout << endl;    
        }else{
            sort(N.begin(), N.end());
            int ind = 0;
            while(N[ind]==0) ind++;
            cout << N[ind] << 0;
            forn(i,sz(N)) if(i!=ind) cout << N[i];
            cout << endl;
        }
    }
    
    return 0;
}
