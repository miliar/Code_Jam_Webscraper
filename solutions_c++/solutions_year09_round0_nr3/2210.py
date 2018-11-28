#include <iostream>

#define M 10000

using namespace std;


string g = "welcome to code jam";
int n;
string s[50];
string str;

void pre()
{
    int l = g.length()-1;
    s[l] = g[l];
    for ( int i = l-1 ; i >= 0 ; i -- )
        s[i] = s[i+1] + g[i];
}


void process(int k)
{
    int f[502][50];
    getline( cin, str );
    int l = g.length()-1;
    int sl = str.length()-1;
    
    f[sl][l+1] = 1;
    if ( str[sl] == g[l] ) f[sl][l] = 1;
    else f[sl][l] = 0;
    
    for ( int i = 0 ; i < l ; i ++ )
        f[sl][i] = 0;
        
    for ( int i = 0; i < sl ; i ++ )
        f[i][l+1] = 1;
        
    for ( int i = sl-1 ; i >= 0 ; i -- )
        for ( int j = l ; j >= 0 ; j -- ){
            if ( str[i] != g[j] )
                f[i][j] = f[i+1][j];
            else f[i][j] =  ( f[i+1][j+1] + f[i+1][j] ) % M; 
        }
       
           
    cout << "Case #" << k << ": ";
    if ( f[0][0] < 10 ) cout << "000" << f[0][0] << endl;
    else if ( f[0][0] < 100 ) cout << "00" << f[0][0] << endl;
    else if ( f[0][0] < 1000 ) cout << "0" << f[0][0] << endl;
    else cout << f[0][0] << endl;    
}


void load()
{
    cin >> n;
    string temp;
    getline(cin, temp);
    for ( int i = 1 ; i <= n ; i ++ )
        process(i);
}



int main()
{
   // pre();
    load();
    return 0;
}
