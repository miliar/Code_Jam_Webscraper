#include<iostream>

using namespace std;

int t,n,p,a,b,pa,pb,temp,id;
char r;

int main(){

    freopen("A-large.in","r",stdin);
    freopen("filename.out","w",stdout);

    cin >> t;
    for( int caso = 1; caso<=t; ++caso){
        cin >> n;
        a = b = temp = 0; pa = pb = 1; id = 2;
        while( n-- ){
            cin >> r >> p;
            if( r == 'O'){
                int mayor = max(p,pa);
                int menor = min(p,pa);
                if( ((mayor-menor)+1) > temp || id == 1 ){
                    a+= (mayor-menor)+1;
                    if( id == 0 ) temp = ((mayor-menor)+1) - temp;
                    else temp += (mayor-menor)+1;
                    id = 1;
                }else{
                    a+= temp+1;
                    temp = 1;
                    id = 1;
                }
                pa = p;
            }else{
                int mayor = max(p,pb);
                int menor = min(p,pb);
                if( ((mayor-menor)+1) > temp || id == 0 ){
                    b+= (mayor-menor)+1;
                    if( id == 1 ) temp = ((mayor-menor)+1) - temp;
                    else temp += (mayor-menor)+1;
                    id = 0;
                }else{
                    b+= temp+1;
                    temp = 1;
                    id = 0;
                }
                pb = p;
            }
        }
        cout << "Case #" << caso << ": "  << max(a,b) << endl;
    }
    return 0;
}
