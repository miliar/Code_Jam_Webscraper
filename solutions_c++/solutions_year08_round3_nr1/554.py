#include <iostream>
#include <vector>
//#include <map>
//#include <set>
#include <string>

using namespace std;


int read_n( istream& is )
{
        int n;
        is >> n;
        string s;
        getline( is, s);
        return n;
}

struct St {
        int id;
        int n;
        bool operator<(const St& s)const { return s.n < n; }
};

int main(int,char**)
{
        int N = read_n( cin );
        for( int i = 0 ; i < N ; i++ ) {
                int P;
                cin >> P;
                int K;
                cin >> K;
                int L;
                cin >> L;

                vector<St> v;
                for( int j = 0 ; j < L ; j++ ) {
                        St s;
                        s.id = j;
                        cin >> s.n;
                        v.push_back( s );
                }

                std::sort( v.begin(), v.end() );
                
                int result = 0;
                for( int j = 0 ; j < L ; j++ ) {
                        result += ((j / K)+1)*v[j].n;
                }
                cout << "Case #" << (i+1) << ": " << result << endl;
        }

        return 1;
}


