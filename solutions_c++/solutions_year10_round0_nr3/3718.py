#include <iostream>

using namespace std;


struct BigInt {
    string value;
    BigInt (string s){
        value = s;
    }
    BigInt()
    {
        value = "0";
    }
};




int char_to_int( char ch )
{
    int k = ch - 48;
    return k;
}

char int_to_char ( int k )
{
    char ch = 48 + k;
    return ch ;
}


string int_to_string (int k)
{
    if ( k == 0 ) return "0";
    string result = "";
    while ( k > 0 ){
        result = int_to_char(k%10) + result;
        k /= 10;
    }
    return result;
}

BigInt cong1(BigInt a, BigInt b)
{
    string sa = a.value;
    string sb = b.value;
    int lena = sa.length()-1;
    int lenb = sb.length()-1;
    string result = "";
    int nho = 0;
    
    for ( int i = lenb ; i >= lenb - lena ; i -- ){
        int k = char_to_int(sb[i]) + char_to_int(sa[i-lenb+lena]) + nho;
        nho = k / 10;
        result += int_to_char(k%10);
    }
    for ( int i = lenb-lena-1; i >= 0 ; i -- ){
        int k = char_to_int(sb[i]) + nho;
        nho = k / 10;
        result += int_to_char(k%10);        
    }
    if ( nho > 0 )
        result += int_to_char(nho);
    
    string temp = "";
    for ( int i = result.length()-1; i >=0 ; i -- )
        temp += result[i];
        
    return BigInt(temp);
}


BigInt cong(BigInt a, BigInt b)
{
    if ( a.value.length() <= b.value.length() )
        return cong1(a, b);
    return cong1(b, a);
}

int test, r, k, n;
int a[10000], f[10000], g[10000], t[10000];

void process()
{
    for ( int i = 0 ; i < n ; i ++ ){
        f[i] = a[i];
        int j = i + 1;
        while ( j % n != i && f[i] + a[j%n] <= k ){
            f[i] += a[j%n];
            j ++;
        }
        g[i] = j%n;
    }
    
    for ( int i = 0 ; i < n ; i ++ ){
        t[i] = 0;
    }
    
    int vt = 0;
    BigInt result("0");
    int count = 1;
    while ( true ){
        result = cong(result, BigInt(int_to_string(f[vt])));
        t[vt] += count;
        count ++;
        if ( t[g[vt]] > 0 ) break;
        if ( count == r+1 ){
            cout << result.value << endl;
            return;
        }
        vt = g[vt];
    }
    
    
    int u = t[g[vt]];
    int v = t[vt];
    
    BigInt temp("0");
    for ( int i = u ; i <= v ; i ++ ){
        temp = cong(temp, BigInt(int_to_string(f[vt])));
        vt = g[vt];
    }
    
    
    BigInt result2("0");
    for ( int i = 0 ; i < ( r - count + 1 ) / ( v - u +1); i ++ )
        result2 = cong(result2, temp);
    //cout << ( r - count ) / ( v - u +1) << endl;
    vt = g[vt];
    for ( int i = 0 ; i < ( r - count + 1 ) % ( v - u +1) ; i ++ ){
        result2 = cong(result2, BigInt(int_to_string(f[vt])));
        vt = g[vt];
    }
    
    result = cong(result, result2);
    
    cout << result.value << endl;
    
}


void load()
{
    cin >> test;
    for ( int i = 0 ; i < test ; i ++ ){
        cin >> r >> k >> n ;
        for ( int j = 0 ; j < n ; j ++ ){
           cin >> a[j];
        }
        cout << "Case #" << i + 1 << ": ";
        process();
    }
}


int main()
{
    load();
    return 0;
}
