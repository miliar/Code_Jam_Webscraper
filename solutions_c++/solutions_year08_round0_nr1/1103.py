#include <iostream>
#include <map>
#include <vector>

using namespace std;

int N, S, Q;
int q[1000];
int qq[1000][100];
        
int calc( int server, int n ) {
    
    if( n==Q ) return 0;
    if( qq[n][server] != -1 ) return qq[n][server];
        
    int r;
    if( server != q[n] ) {
        
        r = calc(server, n+1);
    } else {
        
        r = Q;
        for(int x=0; x<S; x++)
            if( x != server )
                r = min( r, calc( x , n+1 ) );
        r++;
    }        
    
    return qq[n][server]=r;
}   

int main() {
    
    cin >> N;
    for(int t=1; t<=N; t++) {
        
        char s[200];
        map<string, int> se;
            
        cin >> S;
        cin.getline(s,200);
        
        for(int x=0; x<S; x++) {
        
            cin.getline(s,200);
            se[string(s)]=x;
        }       
        
        cin >> Q;
        cin.getline(s,200);
        for(int x=0; x<Q; x++) {
        
            cin.getline(s,200);
            q[x]=se[string(s)];
        }
        
        for(int x=0; x<Q; x++)
            for(int y=0; y<S; y++)
                qq[x][y]=-1;
                
        int m = Q;
        for(int x=0; x<S; x++)
            m = min( m, calc( x , 0 ) );
        
        cout << "Case #" << t << ": " <<m << endl;
    }
}
