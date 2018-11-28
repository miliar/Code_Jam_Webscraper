#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t;
    char matriz[6][6];
    cin>>t;
    
    
    for(int i=1; i<=t; i++)
    {
        
        char ganador='T';
        int xt,yt;
        bool completo = true;
        for(int ii=0; ii<4; ii++)
            for(int jj=0; jj<4; jj++)
                {
                    cin>>matriz[ii][jj];
                    if(matriz[ii][jj]=='T')
                        {xt=ii;yt=jj;}
                    if(matriz[ii][jj]=='.')
                        completo = false;
                }
                
                
        for(int ii=0; ii<4; ii++)
        {
            char val = matriz[ii][0];
            if(val == '.') continue;
            bool cumple = true;
            for(int jj=1; jj<4 && cumple; jj++)
                if(val!=matriz[ii][jj] && matriz[ii][jj]!='T') cumple= false;
                
            if(cumple) ganador = val;
        }
        
        if(ganador!='T')
        {
            cout<<"Case #"<<i<<": "<<ganador<<" won\n";    
            continue;
        }
        
        for(int ii=0; ii<4; ii++)        
        {
            char val = matriz[0][ii];
            if(val == '.') continue;
            bool cumple = true;
            for(int jj=1; jj<4 && cumple; jj++ )
                if(val!=matriz[jj][ii] && matriz[jj][ii]!='T') cumple = false;
                
            if(cumple) ganador = val;            
        }
        if(ganador!='T')
        {
            cout<<"Case #"<<i<<": "<<ganador<<" won\n";
            continue;            
        }
        
        
        matriz[xt][yt]='X';
        
        if((matriz[0][0]=='X' &&
            matriz[1][1]=='X' &&
            matriz[2][2]=='X' &&
            matriz[3][3]=='X') ||
            (matriz[0][3]=='X' &&
            matriz[1][2]=='X' &&
            matriz[2][1]=='X' &&
            matriz[3][0]=='X')
        )
        {
            cout<<"Case #"<<i<<": X won\n";
            continue;
        }
        
        
        matriz[xt][yt]='O';
        
        if((matriz[0][0]=='O' &&
            matriz[1][1]=='O' &&
            matriz[2][2]=='O' &&
            matriz[3][3]=='O') ||
            (matriz[0][3]=='O' &&
            matriz[1][2]=='O' &&
            matriz[2][1]=='O' &&
            matriz[3][0]=='O')
        )
        {
            cout<<"Case #"<<i<<": O won\n";
            continue;
        }
        
        if(completo)
            cout<<"Case #"<<i<<": Draw\n";
        else 
            cout<<"Case #"<<i<<": Game has not completed\n";
        
    }
    
}