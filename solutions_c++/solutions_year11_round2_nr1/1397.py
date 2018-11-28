/*
ID: dhxav
PROG: a
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("A-large.out");
    ifstream fin ("A-large.in");
    
    int T, N;
    char table[105][105];
    int temp1, temp2;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> N;
        
        for (int j=0; j<N; j++)
            fin >> table[j];
            
        double rpi[100] = {0};
        double wp[100] = {0};
        double owp[100] = {0};
        double oowp[100] = {0};
        int game[100] = {0};
            
        for (int j=0; j<N; j++)
        {
            for (int k=0; k<N; k++)
            {
                if (table[j][k]!='.')
                   game[j]++;
                if (table[j][k]=='1')
                   wp[j]++;
            }
            wp[j] = wp[j]/(double)game[j];
        }
        
        for (int j=0; j<N; j++)
        {
             for (int k=0; k<N; k++)      
             {
                 if (table[j][k]=='1' && game[k]>1)
                    owp[j] += wp[k]*(double)game[k]/(double)(game[k]-1);
                 else if (table[j][k]=='0' && game[k]>1)
                      owp[j] += (wp[k]*(double)game[k]-1)/(double)(game[k]-1);
             }
             owp[j] = owp[j]/(double)game[j];
        }
        
        for (int j=0; j<N; j++)
        {
             for (int k=0; k<N; k++)      
             {
                 if (table[j][k]!='.')
                    oowp[j] += owp[k];
             }
             oowp[j] = oowp[j]/(double)game[j];
        }
        
        for (int j=0; j<N; j++)
            rpi[j] = 0.25*wp[j] + 0.50*owp[j] + 0.25*oowp[j];
            
        fout << "Case #" << i+1 << ": " << endl;
        
        for (int j=0; j<N; j++)
            fout << rpi[j] << endl;
    }
    
    return 0;
}
