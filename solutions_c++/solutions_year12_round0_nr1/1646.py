#include <iostream>
#include <sstream>
#include <string>
#include <cstdio>

using namespace std;

int mapme[500];

string lines[500];

int main() {
    
mapme[(int)'a']=(int)'y';
mapme[(int)'b']=(int)'h';
mapme[(int)'c']=(int)'e';
mapme[(int)'d']=(int)'s';
mapme[(int)'e']=(int)'o';
mapme[(int)'f']=(int)'c';
mapme[(int)'g']=(int)'v';
mapme[(int)'h']=(int)'x';
mapme[(int)'i']=(int)'d';
mapme[(int)'j']=(int)'u';
mapme[(int)'k']=(int)'i';
mapme[(int)'l']=(int)'g';
mapme[(int)'m']=(int)'l';
mapme[(int)'n']=(int)'b';
mapme[(int)'o']=(int)'k';
mapme[(int)'p']=(int)'r';
mapme[(int)'q']=(int)'z';
mapme[(int)'r']=(int)'t';
mapme[(int)'s']=(int)'n';
mapme[(int)'t']=(int)'w';
mapme[(int)'u']=(int)'j';
mapme[(int)'v']=(int)'p';
mapme[(int)'w']=(int)'f';
mapme[(int)'x']=(int)'m';
mapme[(int)'y']=(int)'a';
mapme[(int)'z']=(int)'q';


    int n;
    cin>>n;

    getchar();
    
    for ( int i = 0; i < n; ++i ) {
        
        getline ( cin, lines[i] );
        
        istringstream fin(lines[i]);
        string word, word2;
        
        cout<<"Case #"<<i+1<<":";
        
        while ( fin>>word ) {
        
            word2 = word;
            for ( int j = 0; j < (int)word.size(); ++j )
                word2[j] = mapme[ (int)word[j] ];
            
            cout<<" "<<word2;
        }
        cout<<"\n";
    }
    return 0;
}
