#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class BigInteger
{
public:
    vector<char> number;
    
    BigInteger() {}
    BigInteger(const string& s)
    {
        for ( int i = s.size()-1; i >= 0; --i )
            number.push_back( s[i]-'0' );
        (*this) = clearZeros(*this);
    }
    
    BigInteger( const BigInteger& b )
    {
        number = b.number;
    }
    
    void print()
    {
        for ( int i = number.size()-1; i >= 0; --i )
            cout << (char)(number[i]+'0');
            
        if ( number.size() == 0 ) cout << "0";
    }
    
    bool operator!=( const BigInteger& b )
    {
        return b.number != number;
    }
    
    bool operator<( const BigInteger& b )
    {
        if ( b.number.size() != number.size() )
            return (number.size() < b.number.size());
        
        for ( int i = number.size()-1; i >= 0; --i )
            if ( number[i] < b.number[i] )
                return true;
            else if ( number[i] > b.number[i] )
                return false;
        return false;
    }
    
    BigInteger operator+( const BigInteger& b )
    {
        BigInteger a;
        BigInteger c;
        if ( *this < b )
        {
            a = BigInteger( b );
            c = BigInteger( *this );
        }
        else
        {
            a = BigInteger( *this );
            c = BigInteger( b );
        }
        
        bool carry = false;
        int i;
        for ( i = 0; i < c.number.size(); ++i )
        {
            if ( carry )
            {
                carry = false;
                ++c.number[i];
            }
            
            a.number[i] += c.number[i];
            if ( a.number[i] > 9 )
            {
                a.number[i] -= 10;
                carry = true;
            }
        }
        
        while (carry and i < a.number.size())
            if (a.number[i] == 9)
            {
                a.number[i] = 0;
                ++i;
            }
            else
            {
                ++a.number[i];
                carry = false;
            }
        
        if (carry) a.number.push_back(1);
        return a;
    }
    
    BigInteger operator-( const BigInteger& b )
    {
        if ( *this < b ) return *this;
     
        BigInteger a( *this ); 
        BigInteger c( b );
        
        bool emp = false;
        int i;
        for ( i = 0; i < c.number.size(); ++i )
        {
            if ( emp )
            {
                emp = false;
                ++c.number[i];
            }
            
            if ( a.number[i] >= c.number[i] )
            {
                a.number[i] -= c.number[i];
            }
            else
            {
                emp = true;
                a.number[i] -= (c.number[i]-10);
            }
        }
        while(emp)
        {
            if ( a.number[i] > 0 )
            {
                --a.number[i];
                emp = false;
            }
            else
            {
                a.number[i] = 9;
                ++i;
            }
        }
        
        a = clearZeros(a);
                
        return a;
    }
    
    BigInteger clearZeros( BigInteger& b )
    {
        while(true)
            if ( b.number.back() == 0 )
                b.number.pop_back();
            else break;
        return b;
    }
    
    BigInteger gcd( const BigInteger& c )
    {
        BigInteger a(*this);
        BigInteger b(c);
        
        if ( !(a != BigInteger(string("0"))) )
           return b;
           
        while (b != BigInteger(string("0")))
        {
            /*a.print();
            cout << " ";
            b.print();
            cout << endl;
            */
            if (b < a)
               a = a - b;
            else
               b = b - a;
        }
        return a;
    }
};

bool operator<(const BigInteger& a, const BigInteger& b)
{
    return a < b;
}

int main()
{
    int c;
    cin >> c;
    
    int n;
    vector<BigInteger> v;
    string s;
    for (int caso = 1; caso <= c; ++caso)
    {
        cin >> n;
        v.clear();
        for (int i = 0; i < n; ++i)
        {
            cin >> s;
            v.push_back( BigInteger(s) );
        }
        sort( v.begin(), v.end() );
        
        cout << "Case #" << caso << ": ";
        
        vector<BigInteger> diffs;
        for (int i = 1; i < v.size(); ++i)
            diffs.push_back( v[i]-v[i-1] );
            
        BigInteger aux( diffs[0] );
        for (int i = 1; i < diffs.size(); ++i)
            aux = aux.gcd( diffs[i] );
            
        BigInteger t(aux);
        
        while ( t < v[0] )
        {
            t = t+aux;
            /*cout << "\t\t";
            t.print();
            cout << endl;*/
        }
        
        /*cout << endl << "\t";
        aux.print();
        cout << " ";
        v[0].print();
        cout << " ";
        t.print();
        cout << endl;
        */
        t = t-v[0];

        t.print();        
        cout << endl;
    }
}
