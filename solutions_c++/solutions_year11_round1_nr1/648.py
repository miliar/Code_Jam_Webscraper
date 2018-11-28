#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

ifstream in("in.txt");
ofstream out("out.txt");

typedef long long LL;

LL gcd( LL a, LL b ) {
    if( a==0 ) return b;
    while( b!= 0 ) {
        if( a>b ) a = a-b;
        else b = b-a;
    }
    return a;
}

int main() {
    int T;
    in >> T;
    for( int test=1; test<=T; test++ ) {
        long long N, PdD=100, Pd, PgD=100, Pg;
        long long PdGCD, PgGCD;
        bool ans;
        in >> N >> Pd >> Pg;

        if( (Pg == 100 && Pd != 100) || (Pg==0 && Pd!=0) ) ans = false;
        else {
            PdGCD = gcd(Pd,PdD);
            PgGCD = gcd(Pg,PgD);
            Pd /= PdGCD;
            PdD /= PdGCD;
            Pg /= PgGCD;
            PgD /= PgGCD;

            if( PdD > N ) ans = false;
            else ans = true;
        }
        //cout << "Case #" << test << ": " << ((ans)?"Possible":"Broken") << endl;
        out << "Case #" << test << ": " << ((ans)?"Possible":"Broken") << endl;
    }

    return 0;
}



