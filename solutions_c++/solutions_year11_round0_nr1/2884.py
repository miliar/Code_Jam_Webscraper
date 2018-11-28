// Bot trust

#include <iostream>
#include <list>
#include <vector>
#include <map>
#include <assert.h>
using namespace std;

int readint() {
    int x;
    cin >> x;
    return x;
}
int abs(int x) {
    return (x > 0) ? x : -x;
}
int max(int x, int y) {
    return (x > y) ? x : y;
}
void move(const string & label, int & pos, int & t, int otherPos, int otherT ) {
    int dest=readint();
    int delta = abs(dest - pos);

    if (delta > 0) {
        // cout << t << ":" << label << " walks from "<< pos << " to " << dest << endl;
    }
    t += delta;
    pos = dest;
    // cout << t << ":" << label << " is in " << dest << "(after " << delta <<" s)"<<endl;

    if (t<otherT) {
       // cout << t << ":" << label << " must wait in ("<< dest <<") up to " << otherT << "(waits " << otherT-t << " sec)" << endl;
    }

    t = max( t, otherT ) + 1;
    // cout << t << ":" << label << " push button at " << t << "s" << endl;
}
int main() {
    int T = readint();
    for(int t=0;t<T; t++) {
        int N = readint();

        int posO = 1, posB = 1;
        int tO = 0, tB = 0;

        for(int n=0;n<N;n++) {
            char ch;
            cin >> ch;
            switch(ch) {
                case 'O':
                              move( "O", posO, tO, posB, tB );
                              break;
                case 'B':
                              move( "B", posB, tB, posO, tO );
                              break;
                default:
                          assert( 0 );
            }
        }

        int result = max(tO, tB);
        cout << "Case #" << t+1 << ": " << result << endl;
    }
    return 0;
}
