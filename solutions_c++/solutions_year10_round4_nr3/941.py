#include <fstream>
#include <iostream>
#include <string>
#include <stdio.h>


using namespace std;

int main()
{
    ofstream fout ("gcj3.txt.in");
    ifstream fin ("gcj3.in.in");
    
    int c;
    
    fin >> c;
    
    for(int i=0; i<c; i++)
    {
    int r;
    fin >> r;
    
    int ret[r][4];
    
    for(int j=0; j<r; j++)
    {
    fin >> ret[j][0];
    fin >> ret[j][1];
    fin >> ret[j][2];
    fin >> ret[j][3];
    }
    
    int tab[100][100];
    
    for(int k=0; k<100; k++)
    for(int l=0; l<100; l++)
    tab[k][l]=0;
    
    for(int j=0; j<r; j++)
    for(int k=ret[j][0]-1; k < ret[j][2]; k++)
    for(int l=ret[j][1]-1; l< ret[j][3]; l++)
    tab[k][l]=1;
    
    
    
    int tabaux[100][100];
    int res;
    
 for(res=0; res>=0; res++)
    {
                        for(int k=0; k<100; k++)
                        for(int l=0; l<100; l++)
                        tabaux[k][l] = tab[k][l];
                        
                        int teste=0;
                        
                        for(int k=0; k<100; k++)
                        for(int l=0; l<100; l++)
                        if(tabaux[k][l]>0)
                        teste++;
                        
                        if(teste==0)
                        break;
    
    for(int k=0; k<100; k++)
    for(int l=0; l<100; l++)
    {
    
    if(tabaux[k][l] == 0)
    {
                    if(k*l != 0)
                    if( tabaux[k-1][l]*tabaux[k][l-1] != 0)
                    tab[k][l]=1;
    }
    else
    {
                    
                    if(k==0)
                    {
                            if(l==0)
                            tab[k][l]=0;
                            else
                            if(tabaux[k][l-1]==0)
                            tab[k][l]=0;
                    }
                    else
                    {
                            if(l==0)
                            {
                            if(tabaux[k-1][l]==0)
                            tab[k][l]=0;
                            }
                            else
                            {
                            if(tabaux[k-1][l]+tabaux[k][l-1]==0)
                            tab[k][l]=0;
                            }
    
                    }
    }
}
    
    
                    
                                    
    }
    
    fout << "Case #" << i+1 << ": " << res << endl;
    
    
    }
    
    return 0;
    
}
