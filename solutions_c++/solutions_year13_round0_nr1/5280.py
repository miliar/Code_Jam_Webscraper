#include <iostream> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <sstream>
#include <fstream>

using namespace std; 

int main()
{
    char field[4][4];
    int cases;
    
    ifstream input;
    ofstream output ("out.txt");
    input.open("in.txt");
    char s;
    string s2;
    int j;
    if (!input) {cout<<"hm";}
    input>>s2;
    istringstream buffer(s2);
    buffer  >>cases; 
    bool casedone;
    for(int i=0;i<cases;i++)
    {
        casedone=false;
        j=15;
        while(j+1)
        {
            input>>field[j/4][j%4];
            j--;
            
        }
        int x,o,d;
        
        
        for(int k=0;k<4;k++)
        {
            x=0;
            for(int l=0;l<4;l++)
            {
                if ((field[k][l]=='X')||(field[k][l]=='T')) x++;
            }
            if (x==4) {output<<"Case #"<<i+1<<": X won \n";cout<<"X wins"<<"\n";k=4;casedone=true;}
        }
        if (casedone) continue;
        
        
        for(int k=0;k<4;k++)
        {
            x=0;
            for(int l=0;l<4;l++)
            {
                if ((field[l][k]=='X')||(field[l][k]=='T')) x++;
            }
            if (x==4) {output<<"Case #"<<i+1<<": X won \n";cout<<"X wins"<<"\n";k=4;casedone=true;}
        }
        if (casedone) continue;
        
        x=0;
        for(int k=0;k<4;k++)
        {
           if ((field[k][k]=='X')||(field[k][k]=='T')) x++;
           
        }
        if (x==4) {output<<"Case #"<<i+1<<": X won \n";cout<<"X wins"<<"\n";continue;}

        x=0;
        for(int k=0;k<4;k++)
        {
            if ((field[k][3-k]=='X')||(field[k][3-k]=='T')) x++;
            
        }
        if (x==4) {output<<"Case #"<<i+1<<": X won \n";cout<<"X wins"<<"\n";continue;}
        
        
        for(int k=0;k<4;k++)
        {
            o=0;
            for(int l=0;l<4;l++)
            {
                if ((field[k][l]=='O')||(field[k][l]=='T')) o++;
            }
            if (o==4) {output<<"Case #"<<i+1<<": O won \n";cout<<"O wins"<<"\n";k=4;casedone=true;}
        }
        if (casedone) continue;
        
        for(int k=0;k<4;k++)
        {
            o=0;
            for(int l=0;l<4;l++)
            {
                if ((field[l][k]=='O')||(field[l][k]=='T')) o++;
            }
            if (o==4) {output<<"Case #"<<i+1<<": O won \n";cout<<"O wins"<<"\n";k=4;casedone=true;}
        }
        if (casedone) continue;
        
        
        o=0;
        for(int k=0;k<4;k++)
        {
            if ((field[k][k]=='O')||(field[k][k]=='T')) o++;
            
        }
        if (o==4) {output<<"Case #"<<i+1<<": O won \n";cout<<"O wins"<<"\n";continue;}
        
        o=0;
        for(int k=0;k<4;k++)
        {
            if ((field[k][3-k]=='O')||(field[k][3-k]=='T')) o++;
            
        }
        if (o==4) {output<<"Case #"<<i+1<<": O won \n";cout<<"O wins"<<"\n";continue;}
        
        d=0;
        for(int k=0;k<4;k++)
        {
            for(int l=0;l<4;l++)
            {
                if ((field[l][k]!='.')) d++;
            }
            if (d==16) {output<<"Case #"<<i+1<<": Draw"<<"\n";cout<<"draw"<<"\n";k=4;casedone=true;}
        }
        if (casedone) continue;
        output<<"Case #"<<i+1<<": Game has not completed\n";
        cout<<"unfinished"<<"\n";
    }
    
    
    return 0;
}