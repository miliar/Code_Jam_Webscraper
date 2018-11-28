#include <iostream>
#include <string>
#include <vector>
#define MAX 20

using namespace std;

main(){
    int L, D, N, count=1, score=0, achou, achou2; 
    vector<string> dicionario, tokens;
    string str, palavra="";
    vector<string> separado;
    cin >> L >> D >> N;
    for(int i=0;i<D;i++){
        cin >> str;
        dicionario.push_back(str);    
    }
    for(int i=0;i<N;i++){
        cin >> str;
        tokens.push_back(str);
    }
    for(int i=0;i<N;i++){
        int k=0;
        for(int j=k;j<tokens[i].size();j++){
            if(tokens[i][j]!='('){
                palavra+=tokens[i][j];
                separado.push_back(palavra);
                palavra="";
                k++;
            }
            else{
                while(tokens[i][j]!=')'){
                    palavra+=tokens[i][j];
                    k=j++;
                }
                separado.push_back(palavra);
                palavra="";
            }
        }
        for(int j=0;j<D;j++){
            for(int l=0;l<L;l++){
                if(separado[l].find(dicionario[j][l])==string::npos){
                    score++;
                    break;   
                }  
            }
        }
        cout << "Case #" << count << ": " << (D-score) << endl;
        count++;
        score=0;
        separado.clear();
    }
}
