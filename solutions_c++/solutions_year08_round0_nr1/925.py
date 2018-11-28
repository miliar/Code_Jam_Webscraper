#include <iostream>
#include <map>
#include <string>

using namespace std;

int main(){
    int ncases;
    cin >> ncases;
    for(int x=1;x<=ncases;x++){
        int queries[1000];
        map<string,int> engines;
        int s,q;
        string buf;
        
        cin >> s;
        cin.ignore();
        for(int i=0;i<s;i++){
            getline(cin,buf);
            engines[buf] = i;
        }
        
        cin >> q;
        cin.ignore();
        for(int i=0;i<q;i++){
            getline(cin,buf);
            if(engines.find(buf)==engines.end()) queries[i]=-1;
            else queries[i] = engines[buf];
        }
        
        if(q==0){
            cout << "Case #" << x << ": 0" << endl;
            continue;
        }
        
        int table[1000][100];
        for(int i=0;i<s;i++){   //init
            if(i==queries[q-1]) table[q-1][i]=1;
            else table[q-1][i]=0;
        }
        
        for(int i=q-2;i>=0;i--){
            for(int j=0;j<s;j++){
                if(queries[i]==j){
                    int best=1000000;
                    for(int k=0;k<s;k++){
                        if(k==j) continue;
                        best <?= table[i+1][k]+1;
                    }
                    table[i][j]=best;
                }
                else table[i][j] = table[i+1][j];
            }
        }
        /*
        for(int i=0;i<q;i++) cout << queries[i] << " ";
        
        cout << endl;
        for(int i=0;i<q;i++){
            for(int j=0;j<s;j++) cout << table[i][j];
            cout << endl;
        }
        cout << endl;
        */
        int best = 10000000;
        for(int i=0;i<s;i++) best <?= table[0][i];
        cout << "Case #" << x << ": " << best << endl;
        engines.clear();
    }
}
