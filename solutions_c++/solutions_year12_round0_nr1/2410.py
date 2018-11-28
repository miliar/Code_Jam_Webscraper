#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

/* Alphabet -> Googlerese
 * A -> Y
 * B -> N
 * C -> F
 * D -> I
 * E -> C
 * F -> W
 * G -> L
 * H -> B
 * I -> K
 * J -> U
 * K -> O
 * L -> M
 * M -> X
 * N -> S
 * O -> E
 * P -> V
 * Q -> Z
 * R -> P
 * S -> D
 * T -> R
 * U -> J
 * V -> G
 * W -> T
 * X -> H
 * Y -> A
 * Z -> Q
*/

char convert(char c)
{
    switch(c)
    {
        case 'y':
            return 'a';
        case 'n':
            return 'b';
        case 'f':
            return 'c';
        case 'i':
            return 'd';
        case 'c':
            return 'e';
        case 'w':
            return 'f';
        case 'l':
            return 'g';
        case 'b':
            return 'h';
        case 'k':
            return 'i';
        case 'u':
            return 'j';
        case 'o':
            return 'k';
        case 'm':
            return 'l';
        case 'x':
            return 'm';
        case 's':
            return 'n';
        case 'e':
            return 'o';
        case 'v':
            return 'p';
        case 'z':
            return 'q';
        case 'p':
            return 'r';
        case 'd':
            return 's';
        case 'r':
            return 't';
        case 'j':
            return 'u';
        case 'g':
            return 'v';
        case 't':
            return 'w';
        case 'h':
            return 'x';
        case 'a':
            return 'y';
        case 'q':
            return 'z';
        case ' ':
            return ' ';
    }
    
    return '!';
}

int main()
{
    int T;
    char G[101];
    
    cin >> T;
    cin.getline(G, 1000);
    
    for(int ix = 0; ix < T; ix++)
    {
        cin.getline(G, 1000);
        
        printf("Case #%i: ", ix+1);
        
        for(unsigned int iy = 0; iy < strlen(G); iy++)
            cout << convert(G[iy]);
        
        if(ix+1 != T)    
            cout << endl;
    }

    return 0;
}
