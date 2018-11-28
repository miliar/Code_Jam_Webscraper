#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <queue>

using namespace std;

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    char f[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    int t;
    cin >> t;
    string s;
    getline(cin,s,char(10));
    for (int i=1;i<=t;i++){
        cout << "Case #" << i<<": ";
        getline(cin,s,char(10));
        for (int j=0;j<s.length();j++){
            if (s[j]==' ')
                cout << ' ';
            else
                cout << f[s[j]-'a'];
        }
        cout << endl;
    }
}

