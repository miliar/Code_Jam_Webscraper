#include<iostream>
#include<vector>
using namespace std;

int T;
int f[4][4];
string s;

int main(){
    cin >> T;
    
    for(int t=0;t<T;t++){
        bool w=false;
        for(int i=0;i<4;i++){
            cin >> s;
            for(int j=0;j<4;j++){
                if(s[j]=='X')
                    f[i][j]=2;
                else if(s[j]=='O')
                    f[i][j]=3;
                else if(s[j]=='T')
                    f[i][j]=4;
                else{
                    f[i][j]=1;
                    w=true;
                }
            }
        }
        
        bool b=false;
        cout << "Case #" << t+1 << ": ";
        for(int i=0;i<4;i++){
            vector<int> a(5,0);
            for(int j=0;j<4;j++)
                a[f[i][j]]++;
            if(a[2]==4||(a[2]==3&&a[4]==1)){
                cout << "X won" << "\n";
                b=true;
                break;
            }
            if(a[3]==4||(a[3]==3&&a[4]==1)){
                cout << "O won" << "\n";
                b=true;
                break;
            }
        }
        
        if(!b) for(int i=0;i<4;i++){
            vector<int> a(5,0);
            for(int j=0;j<4;j++)
                a[f[j][i]]++;
            if(a[2]==4||(a[2]==3&&a[4]==1)){
                cout << "X won" << "\n";
                b=true;
                break;
            }
            if(a[3]==4||(a[3]==3&&a[4]==1)){
                cout << "O won" << "\n";
                b=true;
                break;
            }
        }
        
        
        if(!b){
            vector<int> a(5,0);
            for(int j=0;j<4;j++)
                a[f[j][j]]++;
            if(a[2]==4||(a[2]==3&&a[4]==1)){
                cout << "X won" << "\n";
                b=true;
                continue;
            }
            if(a[3]==4||(a[3]==3&&a[4]==1)){
                cout << "O won" << "\n";
                b=true;
                continue;
            }
            a.clear();
            a.resize(5,0);
            for(int j=0;j<4;j++)
                a[f[3-j][j]]++;
            if(a[2]==4||(a[2]==3&&a[4]==1)){
                cout << "X won" << "\n";
                b=true;
                continue;
            }
            if(a[3]==4||(a[3]==3&&a[4]==1)){
                cout << "O won" << "\n";
                b=true;
                continue;
            }
        }
        if(b) continue;
        if(w) cout << "Game has not completed\n";
        else cout << "Draw\n";
    }
    
    return 0;
}

