#include <iostream>
#include <cstring>
#include <iomanip>

using namespace std;

const string p = "welcome to code jam";
int n,c=0, f[502][20];
string temp;

void process(){
    cout << "Case #" << ++c << ": ";
    int l= temp.length();    
    memset(f,0,sizeof(f));
    for(int i = 0 ; i < l + 1 ; i++) f[i][0] = 1;
    for(int i = 1 ; i < l + 1 ; i++)
        for( int j = 1; j < 20 ; j++){
                f[i][j] = f[i-1][j];
                if( temp[i-1] == p[j-1] ){
                    if(j==0) f[i][j] = 1;
                    else f[i][j] = (f[i][j]+ f[i-1][j-1])%10000;  
                }
            } 
     cout << setw(4) << setfill('0') << f[l][19] << endl;   
}

int main(){   
    freopen("sub-6.in","r",stdin);
    freopen("C.out","w",stdout);    
    scanf("%d\n",&n);
    for(int i=0; i < n; i++){
        getline(cin,temp);
        process();
    }    
    return 0;
}
