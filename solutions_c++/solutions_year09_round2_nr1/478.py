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

typedef double tint;

struct nodo{
    vector<nodo> next;
    string name;
    tint p;
}h;

void lee(nodo &a){
    char c;
    //while(cin >> c && c!='(');
    //cout << "leyendo" << endl;
    cin >> a.p;
    //cout << a.p << " " << endl;
    while(cin >> c && c==' ');
    if(c!=')'){
        string tmp;
        tmp+=c;
        while(cin >> c && c!=' ' && c!='(') tmp+=c;
        //cin >> tmp;
        //reverse(tmp.begin(), tmp.end());
        //tmp += c;
        //reverse(tmp.begin(), tmp.end());
        a.name = tmp;
        nodo h1; h1.name.clear();
        if(c==' ') while(cin >> c && c!='(');
        lee(h1);
        a.next.pb(h1);
        while(cin >> c && c!='(');
        nodo h2;
        h2.name.clear();
        lee(h2);
        a.next.pb(h2);
        while(cin >> c && c!=')');
    }
}

void imprime(nodo a){
    cout << "nodo " << a.p;
    if(sz(a.name)!=0){
        cout << " nombre: " << a.name << endl;
        imprime(a.next[0]);
        cout << endl;
        imprime(a.next[1]);
        cout << endl;
    }
    cout << endl;
}

vector<string> lista;

void calcula(nodo w, tint p){
    if(sz(w.name) == 0){ p*= w.p; printf("%.7Lf\n",p); }
    else{
        nodo tmp;
        if(find(lista.begin(), lista.end(), w.name) != lista.end()) tmp = w.next[0];
        else tmp = w.next[1];
        
        p*= w.p;
        calcula(tmp, p);
    }
}

int main(){
    int NC, L;
    
    cin >> NC;
    forn(nc, NC){
        //char cc; cin >> cc; cout << cc << endl;
        h.next.clear(); h.name.clear();
        cin >> L;
        char c;
        while(cin >> c && c!='('); //cout << c;
        lee(h);    
        //imprime(h);
        
        int A; cin >> A;
        cout << "Case #" << nc+1 << ":" << endl;
        forn(i, A){
            string tmp;
            lista.clear();
            cin >> tmp;
            //cout << tmp << " ";
            int C; cin >> C;
            forn(j, C){string tt; cin >> tt; lista.pb(tt); }
            calcula(h, 1);
        }
    }
    
    return 0;
}
