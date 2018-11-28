// Rotate by dANNY vIOREL eSPEJO
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
typedef vector<int> vi;
typedef vector<string> vs;
int x=2, y=5;
bool busca(const vs &sopa, const string& q){
	char ch = q[0];
	int n = sopa.S;
	F(f,n)
		F(c,n)
			if( sopa[f][c] == ch ){
				for( int i = -1; i <= 1 ; i++)
					for( int j = -1; j <= 1 ; j++){
						int ind = 0, ix = c, iy = f;
						while(i || j){
							iy += i, ix += j;
							if( iy >= 0 && iy < n && ix >= 0 && ix < n){
								if( sopa[iy][ix] != q[++ind] )
									break;
								if( ind == (int)q.S-1 ){
									y = c+1, x = f+1;
									return true;
								}								
							}
							else
								break;
						}
					}
			}
    return false;
}

string ganador(vs mat, int k){
    string r = "", b = "";
    F(i, k){
        r.pb('R');
        b.pb('B');
    }
    bool red = busca(mat,r);
    bool blue = busca(mat,b);
    if( red && blue )
        return "Both";
    if( !red && !blue )
        return "Neither";
    if( red )
        return "Red";
    return "Blue";
}
string res(vs mat, int k){
    int n = mat.S;
    F(i,n){
        string aux = "";
        F(j,n)
            if( mat[i][j] != '.' )
                aux.pb(mat[i][j]);
        int dif = n - aux.S;
        string d = "";
        F(k,dif)
            d.pb('.');
        mat[i] = d + aux;
    }
    return ganador(mat,k);
}
int main(){
    int n, casos, k;
    cin >> casos;
    For(q,1,casos+1){
        cin >> n >> k;
        vs mat(n);
        F(i,n)
            cin >> mat[i];
        cout << "Case #" << q << ": " << res(mat,k) << endl;
    }
    return 0;
}
