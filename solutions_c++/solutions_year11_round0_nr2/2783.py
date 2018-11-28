#include <iostream>
#include <map>
#include <set>
#include <vector>

#define MAX 110

using namespace std;

int C, D, N;
char a[MAX];
char stack[MAX];
char op[MAX][2];

int main(){
    int T;
    cin >> T;
    for (int t=1; t<=T; t++){
        
        map<pair<char,char>,char> comb;
        map<char,int> ocur;
        
        cin >> C;
        for (int i=0; i<C; i++){
            string s;
            cin >> s;
            comb[pair<char,char>(s[0],s[1])] = s[2];
            comb[pair<char,char>(s[1],s[0])] = s[2];
            
            for (int j=0; j<3; j++){
                ocur[s[j]] = 0;
            }
        }
        
        cin >> D;
        for (int i=0; i<D; i++){
            string s;
            cin >> s;
            
            op[i][0] = s[0];
            op[i][1] = s[1];
            
            for (int j=0; j<2; j++){
                ocur[s[j]] = 0;
            }
        }
        
        cin >> N;
        for (int i=0; i<N; i++){
            cin >> a[i];
        }
        
        int i = 0;
        int top = 0;
        
        while ( i < N ){
            // Insertamos el elemento al final de la lista
            char actual = a[i];
            stack[top++] = actual;
            
            ocur[actual]++;
            
            // Hacemos todas las combinaciones
            while ( top > 1
                    && comb.count( pair<char,char>(stack[top-1], stack[top-2])) > 0
                  )
            {
                char nuevo = comb[ pair<char,char>(stack[top-1], stack[top-2]) ];
                
                ocur[stack[--top]]--;
                ocur[stack[--top]]--;
                
                stack[top++] = nuevo;
                ocur[nuevo]++;
            }
            
            // Verificamos si hay opuestos
            if ( top > 1 ){
                bool clear = false;
                for (int k=0; k<D && !clear; k++){
                    if ( op[k][0] == stack[top-1] && ocur[op[k][1]] > 0)
                        clear = true;
                    else if ( op[k][1] == stack[top-1]  && ocur[op[k][0]] > 0)
                        clear = true;
                }
                if ( clear ){
                    for (int k=0; k<top; k++){
                        ocur[stack[k]] = 0;
                    }
                    top = 0;
                }
            }
            
            i++;
        }
        
        cout << "Case #" << t << ": [";
        
        for (int i=0; i<top; i++){
            if ( i ){
                cout << ", ";
            }
            cout << stack[i];
        }
        cout << "]" << endl;
    }
    return 0;
}
