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


int main(){
    int N, D, L;
    string tmp;
    vector<string> dic;
    vi ind[20][32];
    int how[5000];
    
    cin >> L >> D >> N;
    forn(i,D){
        cin >> tmp;
        //cout << tmp << endl;
        dic.pb(tmp);
        //forn(j, L) ind[j][int(tmp[j]-'a')].pb(i);
    }
    forn(i, N){
        int ap[32][20];
        memset(ap,0,sizeof(ap));
        char c; int pos = 0;
        while(pos<L){
            cin >> c;
            if(c=='('){
                while(cin >> c && c!=')'){ ap[int(c-'a')][pos] = 1; }
            }else{
                ap[int(c-'a')][pos] = 1;
            }
            pos++;
        }
        int T = 0;
        forn(j, D){
            //cout << "viendo " << dic[j] << " ";
            int cond = 1;
            forn (k, L) if (ap[int(dic[j][k]-'a')][k] != 1) { cond = 0; break; }
            //cout << endl;
            if (cond==1) T++;    
        }
        cout << "Case #" << i+1 << ": " << T << endl;
    }
    
    return 0;
}
