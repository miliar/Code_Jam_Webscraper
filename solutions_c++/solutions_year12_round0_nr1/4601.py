#include<iostream>
#include<string>
#include<vector>
#include <cstdio>

using namespace std;
int replace[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
vector<string> res;

void replace_fun( string s ){

    int i;
    for( i = 0; i < s.length(); i++ ){
        if( s[i] != ' ' ){
            s[i] = replace[ s[i] - 'a' ];
        }
    }
    res.push_back( s );

}

void print_res( ){
    int i;
    for( i = 0; i < res.size(); i++ ){
        cout << "Case #" << i+1 << ": " <<res[i] << endl;
    }

}

int main( ){

    int n, i;
    char j;
    string s;

    cin >> n;
    j = getchar();

    for( i = 0; i < n; i++ ){
        getline( cin, s );
        replace_fun( s );
    }
    print_res();
    return 0;

}
