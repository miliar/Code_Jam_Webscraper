#include <cstdio>
#include <iostream>
#include <cassert>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <vector>
#include <deque>

using namespace std;

class big_dec
{
public:
    deque<char> num;
    void translate(const char * str, unsigned int len) {
        num.clear();
        for(unsigned int i=len; i; ) {
            i--;
            char b = str[i];
            b -= '0';
            num.push_back(b);
        }
    };
    void print() {
        char line[100];
        unsigned int i = num.size();
        line[i] = 0;
        for( unsigned int j=0; i; j++) {
            i--;
            line[j] = num[i] + '0';
        }
        printf("%s", line);
    };
    void add(const big_dec & y) {
        char c = 0;
        unsigned int s1 = num.size(), s2 = y.num.size();
        if( s1 < s2 ) {
            for(unsigned int i=s1; i<s2; i++) {
                num.push_back(0);
            }
        }
        num[0] += y.num[0];
        if( num[0] >= 10 ) {
            c = 1;
            num[0] -= 10;
        }
        for(unsigned int i=1; i<s2; i++) {
            num[i] += c;
            num[i] += y.num[i];
            if( num[i] >= 10 ) {
                c = 1;
                num[i] -= 10;
            } else
                c = 0;
        }
        if( c ) {
            for(unsigned int i=s2; c && i<s1; i++) {
                num[i] += c;
                if( num[i] >= 10 ) {
                    c = 1;
                    num[i] -= 10;
                } else
                    c = 0;
            }
            if( c )
                num.push_back(1);
        }
    };
    void sub(const big_dec & y) {
        char c = 0;
        unsigned int s1 = num.size(), s2 = y.num.size();
        for(unsigned int i=0; i<s2; i++) {
            unsigned int _sub = c + y.num[i];
            if( num[i] < _sub ) {
                num[i] += 10;
                num[i] -= _sub;
                c = 1;
            } else {
                num[i] -= _sub;
                c = 0;
            }
        }
        if( c ) {
            for(unsigned int i=s2; c && i<s1; i++) {
                if( num[i] < c ) {
                    num[i] += 10;
                    num[i] -= c;
                    c = 1;
                } else {
                    num[i] -= c;
                    c = 0;
                }
            }
        }
        for(unsigned int i = s1-1; i; i--) {
            if( !num[i] )
                num.pop_back();
            else
                break;
        }
    };
    int cmp( const big_dec & y ) {
        unsigned int s1 = num.size(), s2 = y.num.size();
        if( s1 > s2 )
            return 1;
        else if( s1 < s2 )
            return -1;
        else {
            for(unsigned int i = s1; i; ) {
                i--;
                char a = num[i], b = y.num[i];
                if( a > b )
                    return 1;
                else if( a < b )
                    return -1;
            }
            return 0;
        }
    };
    void mod(const big_dec & y) {
        int _cmp = cmp(y);
        if( _cmp < 0 )
            return;
        else if( !_cmp ) {
            num.resize(1);
            num[0] = 0;
            return;
        } else {
            big_dec z;
            z.num = y.num;
            unsigned int s1 = num.size(), s2 = z.num.size();
            z.shl(s1-s2);
            if( cmp(z)<0 )
                z.shr(1);
            sub(z);
            mod(y);
        }
    };
    void shr(unsigned int b) {
        for( ; b; b--)
            num.pop_front();
    };
    void shl(unsigned int b) {
        for( ; b; b--)
            num.push_front(0);
    };
    int positive() {
        if( num.size()>1 )
            return 1;
        else if( num[0]>0 )
            return 1;
        else
            return 0;
    };
};

int main()
{
    int C;
    char input[1024][64];
    big_dec n[1024], m[1024];
    
    cin >> C;

    for(int i=1; i<=C; i++) {
        unsigned int N;
        cin >> N;
        for(unsigned int j=0; j<N; j++) {
            cin >> input[j];
            n[j].translate(input[j], strlen(input[j]));
            m[j].num = n[j].num;
        }
        unsigned int k=0;
        for(unsigned int j=1; j<N; j++) {
            if( n[k].cmp(n[j])>0 )
                k = j;
        }

        unsigned int pos_count = 0;
        for(unsigned int j=0; j<N; j++) {
            m[j].sub(n[k]);
            if( m[j].positive() )
                pos_count ++;
        }
        
        // find min k
        for( k=0; (!m[k].positive()) && k<N; k++ )
            ;
        for(unsigned int j=k+1; j<N; j++) {
            if( m[j].positive() )
                if( m[k].cmp(m[j])>0 )
                    k = j;
        }
        while( pos_count > 1 ) {
            // foreach m[j], mod m[k]
            for( unsigned int j=0; j<N; j++ ) {
                if( j!= k )
                    if( m[j].positive() ) {
                        m[j].mod(m[k]);
                        if( ! m[j].positive() )
                            pos_count --;
                    }
            }
            // find min k
            for( k=0; (!m[k].positive()) && k<N; k++ )
                ;
            for(unsigned int j=k+1; j<N; j++) {
                if( m[j].positive() )
                    if( m[k].cmp(m[j])>0 )
                        k = j;
            }
        }
        
/*        cout << "[";
        n[0].print();
        cout << "] [";
        m[k].print();
        cout << "]" << endl; */
        n[0].mod(m[k]); 
        if( n[0].positive() ) {
            m[k].sub(n[0]);                
            cout << "Case #" << i << ": ";
            m[k].print();
            cout << endl;
        } else {
            cout << "Case #" << i << ": 0" << endl;
        }
    }
    
    cin >> C;
    return 0;
}
