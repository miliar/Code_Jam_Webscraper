#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string D[100],alph;
bool valid[100];
int N,cont;

int points(string guess){
    //cout << "guess = " << guess << endl;
    int ret = 0,cont = 0,L = guess.size();
    
    for(int i = 0;i < N;++i){
        if(D[i].size() == L && D[i] != guess) valid[i] = true, ++cont;
        else valid[i] = false;
    }
    
    for(int i = 0;i < N;++i){
        if(D[i] == guess){
            valid[i] = true;
            ++cont;
            break;
        }
    }
    
    for(int k = 0;k < 26 && cont > 1;++k){
        bool ok = false;
        
        for(int i = 0;i < N;++i){
            if(!valid[i]) continue;
            //cout << D[i] << " ";
            
            for(int j = L - 1;j >= 0;--j){
                if(D[i][j] == alph[k])
                    ok = true;
            }
        }
        //cout << endl << "ok = " << ok << endl;
        if(!ok) continue;
        
        bool lose = true;
        
        for(int i = 0;i < L;++i)
            if(guess[i] == alph[k])
                lose = false;
        //cout << "k = " << k << ", lose = " << lose << endl;
        if(lose) ++ret;
        
        for(int i = 0;i < N;++i){
            if(!valid[i]) continue;
            
            bool check = true;
            
            for(int j = 0;j < L;++j){
                if(guess[j] == alph[k] && D[i][j] != alph[k])
                    check = false;
                if(guess[j] != alph[k] && D[i][j] == alph[k])
                    check = false;
            }
            
            if(!check) valid[i] = false, --cont;
        }
    }
    
    //cout << "ret = " << ret << endl;
    
    return ret;
}

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T,M;
    
    cin >> T;
    
    for(int tc = 1;tc <= T;++tc){
        printf("Case #%d:",tc);
        
        cin >> N >> M;
        
        for(int i = 0;i < N;++i) cin >> D[i];
        
        while(M--){
            cin >> alph;
            //cout << "alph = " << alph << endl;
            
            int mx = -1,ind = 0;
            
            for(int i = 0;i < N;++i){
                int aux = points(D[i]);
                
                if(aux > mx){
                    mx = aux;
                    ind = i;
                }
            }
            
            cout << " " << D[ind];
        }
        
        cout << endl;
    }
    
    return 0;
}
