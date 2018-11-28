// Theme Park by dANNY vIOREL eSPEJO
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#define For(i,a,b) for(int i=(a);i<(b);i++)
#define F(i,a) for(int i=0;i<(a);i++)
#define All(x)  x.begin(),x.end()
#define llena(x) F(i,x.size())cin>>x[i]
#define pb push_back
#define S size()
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;

int main(){
    int n, t, r, k, aux;
    cin >> t;
    For(i,1,t+1){
        cin >> r >> k >> n;
        queue<int> q;
        int cost = 0;
        F(w,n){
            cin >> aux;
            q.push(aux);
        }
        F(w,r){
            int parcial = 0;
            int cont = 0;
            while(cont < n){
                aux = q.front();
                if( parcial + aux <= k ){
                    cost += aux;
                    parcial += aux;
                    q.pop();                
                    q.push(aux);
                }
                else{
                    break;
                }
                cont++;
            }
        }
        cout << "Case #" << i << ": " << cost << endl;
    }
    return 0;
}
