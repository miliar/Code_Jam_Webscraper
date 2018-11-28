#include <iostream>
#include <cstdio>
#include <vector>
#include <cctype>

using namespace std;

const int MAXD=5050;
vector<string> dict;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);

    int L,D,N;
    cin >> L >> D >> N;
    for( int i=0; i<D; i++ ) {
        string str;
        cin >> str;
        dict.push_back(str);
    }

    for( int test=1; test<=N; test++ ) {
        string str;
        cin >> str;
        vector<string> pat;
        int ans=0;

        for( int j=0; j<str.size(); j++ ) {
            if( isalpha(str[j]) ) pat.push_back(string(1,str[j]));
            else { //parentheses
                for( int k=j+1; ; k++ ) {
                    if( str[k]==')' ) {
                        pat.push_back( str.substr(j+1,k-j-1) );
                        j=k;
                        break;
                    }
                }
            }
        }
        for( int i=0; i<D; i++ ) {
            bool ok=true;
            for( int j=0; j<L; j++ ) {
                if( pat[j].find(dict[i][j]) == string::npos ) {
                    ok=false;
                    break;
                }
            }
            if(ok) ans++;
        }
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}






