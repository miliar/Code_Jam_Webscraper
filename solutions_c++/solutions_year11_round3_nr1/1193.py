// Problem A. Square Tiles //
#include <iostream>
#include <fstream>
#include <inttypes.h>

using namespace std;

/*
Input
  	
Output
 
3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##.. 	

Case #1:
Impossible
Case #2:
.
Case #3:
./\..
.\//\
./\\/
.\/.. 
*/

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output.txt");
    
    int cases=0;
    in>>cases;
    
    for (int i=0; i<cases; i++)
    {
        int h,w;
        in>>h>>w;
        char arr[h][w];
        
        for (int j=0; j<h; j++)
            for (int k=0; k<w; k++)
                in>>arr[j][k];
                
        
        for (int j=0; j<h; j++)
            for (int k=0; k<w; k++)
            {
                if ((arr[j][k]=='#') &&
                    (arr[j+1][k]=='#') &&
                    (arr[j][k+1]=='#') &&
                    (arr[j+1][k+1]=='#') &&
                    j+1<h && k+1<w
                    )
                    {
                          arr[j][k]='/';
                          arr[j+1][k]='\\';
                          arr[j][k+1]='\\';
                          arr[j+1][k+1]='/';
                    }
            }
          
        bool possible = true;
        cout<<"Case #"<<(i+1)<<":\n";
        out<<"Case #"<<(i+1)<<":\n";
        for (int j=0; j<h; j++)
            for (int k=0; k<w; k++)
                if (arr[j][k]=='#') {possible=false; break;}
        
        if (possible)  
        for (int j=0; j<h; j++)
        {
            for (int k=0; k<w; k++)
                {
                     cout<<arr[j][k];
                     out<<arr[j][k];
                }
            cout<<endl;
            out<<endl;
        }
        else {cout<<"Impossible\n";out<<"Impossible\n";}
    }
    
    in.close();
    out.close();
    system("pause");
}

