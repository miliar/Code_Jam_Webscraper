// Snapper Chain by dANN YvIOREL eSPEJO
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#define For(i,a,b) for(int i=(a);i<(b);i++)
#define F(i,a) for(int i=0;i<(a);i++)
#define All(x)  x.begin(),x.end()
#define llena(x) F(i,x.size())cin>>x[i]
#define pb push_back
#define S size()

using namespace std;
int main(){
    int n, t, k;
    cin >> t;
    For(i,1,t+1){
        cin >> n >> k;
        int tam = 1 << n;
        k %= tam;
        if( k == tam - 1)
            cout << "Case #" << i << ": ON\n";
        else
            cout << "Case #" << i << ": OFF\n";        
    }    
    return 0;   
}
