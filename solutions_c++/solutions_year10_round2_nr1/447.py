#include <fstream>
#include <iostream>
#include <string>
#include <string.h>

using namespace std;

int main()
{
    ofstream fout ("jam1.txt");
    ifstream fin ("jam1.in");
    
    int t;
    fin >> t;
    int n, m;
    
    for(int y=0; y<t; y++)
    {
    fin >> n;
    fin >> m;
    
    string velha[n+m];
    string nova[m];
    
    for(int j=0; j<n; j++)
    fin >> velha[j];
    
    for(int j=0; j<m; j++)
    fin >> nova[j];
    
    int res=0;
    for(int i=0; i <m; i++)
    {
    int aux=0;
    int resaux=0;
    for(int j=0; j< nova[i].size(); j++)
    if(nova[i][j] == '/')
    aux++;
    
    for(int j=0; j<n+i; j++)
    {
    int resaux2 = 0;
    int s;
    for(s=0; (s< nova[i].size())&&(s < velha[j].size()); s++)
    {
    if(nova[i][s] != velha[j][s])
    break;
    
    if(nova[i][s] == '/')
    resaux2++;
    }
    
    
    
    if( (s < velha[j].size()) && (s < nova[i].size()))
    resaux2--;
    
    if( s == velha[j].size())
    {
    if( (s < nova[i].size())&& (nova[i][s] != '/'))
    resaux2--;
    }

    if( s == nova[i].size())
    {
    if( (s < velha[j].size())&& (velha[j][s] != '/'))
    resaux2--;
    }
    
    if(resaux2 > resaux)
    resaux = resaux2;
    
    }
    
    velha[n+i] = nova[i];

    

    
    res += aux - resaux;
        
    }
    
    fout << "Case #" << y+1 << ": " << res << endl;
    
    
    }
    
        
    return 0;
    
}
