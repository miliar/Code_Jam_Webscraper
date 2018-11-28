#include<iostream>
#include<cstring>

using namespace std;

char TRANS[] = {
         'y',
         'h',
         'e',
         's',
         'o',
         'c',
         'v',
         'x',
         'd',
         'u',
         'i',
         'g',
         'l',
         'b',
         'k',
         'r',
         'z',
         't',
         'n',
         'w',
         'j',
         'p',
         'f',
         'm',
         'a',
         'q'
     };

int main()
{
    int T=0,i=0,L=0;
    char G[101];
    cin>>T;

    // Learnt some new stuff !!!
    cin.ignore(101, '\n');

    for(int j=1;j<=T;j++)
    {
        cin.getline(G,101);
        L = strlen(G);
        for(int i=0;i<L;i++)
        {
            if( G[i]!=' ' )
            {
                G[i] = TRANS[(int)G[i]-97];
            }
        }
        cout<<"Case #"<<j<<": "<<G<<"\n";
    }
    return 0;
}
