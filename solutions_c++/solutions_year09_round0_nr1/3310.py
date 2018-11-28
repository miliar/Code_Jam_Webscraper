#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

#define in "test.in"
#define out "test.out"

int N, L, D;
vector<string> Words, Aux;

int main()
{
    int total = 0;
    
    freopen(in,"r",stdin);
    freopen(out,"w",stdout);
    
    scanf("%d%d%d\n", &L, &D, &N);
    for ( int i = 1; i <= D; i++ )
    {
        char line[20];
        fgets(line,19,stdin);
        Words.push_back(line);
    }    
    
    for ( int i = 1; i <= N; i++ )
    {
        Aux.clear(); total = 0;
        char line[1000]; int j = 0;
        fgets(line,999,stdin);
        
        while ( line[j] != '\n' ) 
        {
            if ( line[j] == '(' ) 
            {
                string p = ""; j++;
                while ( line[j] != ')' ) p += line[j], j++;
                Aux.push_back(p);
            }    
            else 
            {
                string p = ""; p += line[j];
                Aux.push_back(p);
            }    
            j++;
        }  
        
        for ( int k = 0; k < Words.size(); k++ )
        {
            bool ok;
            for ( int j = 0; j < Aux.size(); j++ )
            {
                ok = 0;
                for ( int t = 0; t < Aux[j].size(); t++ )
                    if ( Words[k][j] == Aux[j][t] ) ok = 1;
                
                if ( !ok ) break;
            }    
            
            if ( ok ) total++;
        }  
        
        printf("Case #%d: %d\n", i, total);
    }    
}    
