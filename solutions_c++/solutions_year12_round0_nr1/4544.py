#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <functional>
#include <sstream>

using namespace std;

int ts[] = {
    'y','h','e','s','o',
    'c','v','x','d','u',
    'i','g','l','b','k',
    'r','z','t','n','w',
    'j','p','f','m','a',
    'q'
};

int main(int argc, char const *argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int n;
    cin >> n;
    string token;
    string answer;
    for(int c=0; c<n; ++c) {
        answer = "";
        getline(cin, token);
        if(token.size() > 0) {
            for(size_t j=0; j<token.size(); ++j) {
                if(token[j] != ' ')
                    answer += ts[token[j]-'a'];
                else
                    answer += ' ';
            }
            cout << "Case #" << c + 1 << ": " << answer << endl;
        } else
            --c;
    }
    return 0;
}
