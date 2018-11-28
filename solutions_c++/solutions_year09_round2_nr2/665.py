#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int t, tcnt;
    string n;

    in >> t ;

    for( tcnt=1; tcnt<=t; tcnt++ ) {
        in >> n;
        out << "Case #" << tcnt << ": " ;
        if( !next_permutation(n.begin(), n.end()) ) {
            sort(n.begin(), n.end() );
            int i;
            char temp;
            for( i=0; i<n.size(); i++ ) 
                if( n[i] != '0' ) break;
            temp = n[i];
            n[i] = n[0];
            n[0] = temp;
            n.insert( n.begin()+1, '0' );
            out << n << endl;
            
        } else {
            out << n << endl;
        }
    }

    return 0;
}