/*
ID: dhxav
PROG: magicka
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ofstream fout ("B-large.out");
    ifstream fin ("B-large.in");
    
    int T, C, D, N;
    char combine[72][3];
    char opposed[56][2];
    char invoke[100];
    int buffer, size, temp;
    
    fin >> T;

    for (int i=0; i<T; i++)
    {
        fin >> C;
        
        for (int j=0; j<C; j++)
        {
            fin >> combine[j][0] >> combine[j][1] >> combine[j][2];
            combine[j+C][0] = combine[j][1];
            combine[j+C][1] = combine[j][0];
            combine[j+C][2] = combine[j][2];
        }
            
        fin >> D;
        
        for (int j=0; j<D; j++)
        {
            fin >> opposed[j][0] >> opposed[j][1];
            opposed[j+D][0] = opposed[j][1];
            opposed[j+D][1] = opposed[j][0];
        }
            
        fin >> N;
        
        for (int j=0; j<N; j++)
            fin >> invoke[j];
            
        size = N;
        
        for (int j=1; j<size; j++)
        {
            temp=0;
            
            for (int k=0; k<2*C; k++)
            {
                if (invoke[j-1]==combine[k][0] && invoke[j]==combine[k][1])
                {
                   invoke[j-1] = combine[k][2];
                   for (int l=j+1; l<size; l++)
                       invoke[l-1] = invoke[l];
                   size--;
                   j--;
                   temp = 1;
                   break;
                }
            }
                
            for (int k=0; k<j; k++)
            {
                if (temp==1)
                   break;
                   
                for (int l=0; l<2*D; l++)
                {
                    if (invoke[k]==opposed[l][0] && invoke[j]==opposed[l][1])
                    {
                       buffer = j+1;
                       for (int m=j+1; m<size; m++)
                           invoke[m-buffer] = invoke[m];
                       size -= buffer;
                       j=-1;
                       temp = 1;
                       break;
                    }
                }
            }
        }
                             
        fout << "Case #" << i+1 << ": [";
        
        for (int j=0; j<size-1; j++)
            fout << invoke[j] << ", ";
        
        if (size>0)
           fout << invoke[size-1] << "]" << endl;
        else
            fout << "]" << endl;
    }
    
    return 0;
}
