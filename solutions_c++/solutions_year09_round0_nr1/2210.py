#include <iostream>
#include <map>
#include <fstream>
using namespace std;



int n, l, d;
string s[5001];
string str;
ofstream fout;


void process( int k )
{
    cin >> str;
    
    map<char, bool> m[20];
    int size = 0;
    int i = 0;
    bool flag = false;
    
    while ( i < str.length() ){
        if ( str[i] != '(' && str[i] != ')' ){
            m[size][str[i]] = true;
            if ( flag == false ) size ++;
        }
        else if ( str[i] == '(' ){
            flag = true;
           //size++;
        }
        else{
            flag = false;
            size ++;
        }
        i++;
    }
    
           
    if ( size != l  ) fout << "Case #" << k << ": " << 0 << endl;
    else{
        bool ok;
        int c = 0;
        for ( int i = 0 ; i < d ; i ++ ){
            ok = true;
            for ( int j = 0 ; j < l ; j ++ )
                if ( ! m[j][s[i][j]]  ){
                    ok = false;
                    break;
                }
            if ( ok ) c ++;
        }
        fout << "Case #" << k << ": " << c << endl;
    }
}

void load()
{
    fout.open("output.out");
    cin >> l >> d >> n;
    for ( int i = 0 ; i < d ; i ++ )
        cin >> s[i];
    for ( int i = 1 ; i <= n ; i ++ )
        process(i);
    fout.close();
}


int main()
{
    load();
    return 0;
}
