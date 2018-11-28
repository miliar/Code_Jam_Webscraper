#include<iostream>
#include<map>
#include <string>

using namespace std;

int t,c,d,n;
map<string,string> mapa;

string changes[39];
int deletes[300];

int main(){

freopen("B-large.in","r",stdin);
freopen("filename.out","w",stdout);

    cin >> t;
    for( int caso = 1; caso <=t; ++caso ){
        mapa.clear();
        cin >> c;
        for( int i = 0; i<c; ++i ){
            char a,b,c;
            string temp = "",temp2="", temp3="";
            cin >> a >> b >> c;
            temp2+=a; temp2+=b;
            temp3+=c;
            mapa[temp2] = c;
            temp2 ="";
            temp2+=b; temp2+=a;
            mapa[temp2] = c;
        }
        cin >> d;
        for( int i = 0; i<d; ++i ) cin >> changes[i];
        cin >> n;
        string val = "";
        for( int i = 0; i<n; ++i ){
            char letter;
            cin >> letter;
            val += letter;
            if( val.size() > 1 ){
                string temp4 = "", temp8="";
                temp4 += val[val.size()-2];
                temp4 += val[val.size()-1];
                temp8 += val[val.size()-1]; temp8 += val[val.size()-2];
                if( mapa[temp4] != "" || mapa[temp8] != "" ){
                    //cout << " el mapa estaba lleno " << mapa[temp4] << endl;
                    //cout << val << endl;
                    string tales = val.substr (0,val.size()-2);
                    val = tales + mapa[temp4];
                    //cout << val << endl;
                }else{
                    //cout << " el mapa no estaba lleno " << temp4 << " " << temp8 << endl;
                    for( int j = 0; j <= 299; ++j ) deletes[j] = 0;
                    //cout << val << endl;
                    for( int j = 0; j <= val.size(); ++j ){
                        deletes[int(val[j])]++;
                    }
                    for( int j = 0; j< d; ++j ){
                        if( deletes[int(changes[j][0])] > 0 && deletes[int(changes[j][1])] > 0 ){
                            val = "";
                        }
                    }
                    //cout << val << endl;
                }
            }
        }
        cout << "Case #" << caso << ": [";
        for( int i = 0; i<val.size(); ++i ){
            cout << val[i];
            if( i!= (val.size()-1) ) cout << ", ";
        }
        cout << "]" << endl;
    }
    return 0;
}
