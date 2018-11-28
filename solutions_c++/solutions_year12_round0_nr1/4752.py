#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in", "r", stdin); // make cin and scanf take from file not from user
	freopen("A-small-attempt0.out", "w", stdout); // make cout print to file not screen
    int alphabet[26]={(96+25),(96+8),(96+5),(96+19),(96+15),(96+3),(96+22),(96+24),(96+4),(96+21),(96+9),(96+7),(96+12),(96+2),(96+11),(96+18),(96+26),(96+20),(96+14),(96+23),(96+10),(96+16),(96+6),(96+13),(96+1),(96+17)};
    int n;
    string word , result ;
    cin >> n ;
    cin >> ws ;
    for(int i=0 ; i<n ; i++)
    {
        getline(cin, word);
        result=word;
        for(int j=0 ; j<word.size() ; j++)
        {
            if(word[j]==' ')
               result[j]=' ' ;
            else
               result[j] = (char)(alphabet[((int)word[j]-97)]) ;
        }
        cout << "Case #" << i+1 << ": " << result << endl ;
    }

    return 0;
}
