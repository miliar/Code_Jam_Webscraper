#include <iostream>
#include <fstream>

using namespace std;

const int HWmax = 100;
const int altmax = 10000;
int minalt, minH, minW;
int grid[HWmax+2][HWmax+2][2];
int H, W;

int findbasin(int Hj, int Wj);

int main()
{
    
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    
    int T;
    int Ti, Hi, Wi;
    int maxi, maxj;
    int basin;
    
    fin >> T;
    for (Ti=0; Ti<T; Ti++)
    {
        fin >> H >> W;
        fout << "Case #" << (Ti+1) << ": " << endl;
        
        //reset
        for (maxi=0; maxi<HWmax+2; maxi++)
            for (maxj=0; maxj<HWmax+2; maxj++)
            {
                grid[maxi][maxj][0] = altmax;
                grid[maxi][maxj][1] = 0;
            }
            
        for (Hi=0; Hi<H; Hi++)
        {
            for (Wi=0; Wi<W; Wi++)
            {
                fin >> grid[Hi+1][Wi+1][0];
                //fout << grid[Hi+1][Wi+1][0] << " ";
            }
            //fout << endl;
        }
        
        for (Hi=1; Hi<H+1; Hi++)
        {
            for (Wi=1; Wi<W+1; Wi++)
            {
                if (!grid[Hi][Wi][1])
                {
                   grid[Hi][Wi][1] = findbasin(Hi,Wi);
                }
                //fout << grid[Hi][Wi][1] << " ";
            }
            //fout << endl;
        }
        
        //convert to letters
        int count = 0;
        int ci;
        int convert[H*W+1];
        char mychar;
        
        for (ci=0; ci<H*W+1; ci++)
        {
            convert[ci] = 0;
        }
        
        for (Hi=1; Hi<H+1; Hi++)
        {
            for (Wi=1; Wi<W+1; Wi++)
            {
                if (!convert[grid[Hi][Wi][1]])
                {
                    count++;
                    convert[grid[Hi][Wi][1]] = count;     
                }
                 mychar = (char)(96+convert[grid[Hi][Wi][1]]);
                 fout << mychar << " ";
            }
            fout << endl;
        }
        
        
    }
    
    fin.close();
    fout.close(); 
     
    return 0;
}

int findbasin(int Hj, int Wj)
{
    if (grid[Hj][Wj][1])
       return grid[Hj][Wj][1];
    else
    {
        minalt = grid[Hj][Wj][0];
        minH = Hj;
        minW = Wj;
        
        //North
        if (grid[Hj-1][Wj][0] < minalt)
        {
           minalt = grid[Hj-1][Wj][0];
           minH = Hj-1;
           minW = Wj;
        }
        //West
        if (grid[Hj][Wj-1][0] < minalt)
        {
           minalt = grid[Hj][Wj-1][0];
           minH = Hj;
           minW = Wj-1;
        }
        //East        
        if (grid[Hj][Wj+1][0] < minalt)
        {
           minalt = grid[Hj][Wj+1][0];
           minH = Hj;
           minW = Wj+1;
        }
        //South
        if (grid[Hj+1][Wj][0] < minalt)
        {
           minalt = grid[Hj+1][Wj][0];
           minH = Hj+1;
           minW = Wj;
        }
        if (minalt == grid[Hj][Wj][0])
           grid[Hj][Wj][1] = (Hj-1)*W + Wj;
        else
        {   
            grid[Hj][Wj][1] = findbasin(minH, minW);
        }
    }
    return grid[Hj][Wj][1];
}
