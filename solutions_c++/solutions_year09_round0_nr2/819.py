#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

const int MAXH = 100;
const int MAXW = 100;

int T, H, W;
int a[MAXH][MAXW];
char b[MAXH][MAXW];
char ch, th;

void flow(int x, int y)
{    
     int min = 10001;
     int xnext, ynext;
     
//     cout << x << y << a[x][y] << endl;
     
     if (x > 0) {
         min = a[x-1][y];
         xnext = x - 1;
         ynext = y;  
     }
     
     if (y > 0 && a[x][y-1] < min) {
         min = a[x][y-1];
         xnext = x;
         ynext = y - 1;  
     }
     
     if (y+1 < W && a[x][y+1] < min) {
         min = a[x][y+1];
         xnext = x;
         ynext = y + 1;  
     }     
     
     if (x+1 < H && a[x+1][y] < min) {
         min = a[x+1][y];
         xnext = x + 1;
         ynext = y;  
     }     
     
//     cout << min << xnext << ynext << a[xnext][ynext] << endl;
     
     if (min < a[x][y])
     {   
          if (b[xnext][ynext] != '*') th = b[xnext][ynext];
          else flow(xnext, ynext);
     }
     
     b[x][y] = th;
}

int main(int argc, char *argv[])
{
    ifstream cin("b-large.in");
    ofstream cout("b-large.out");
    cin >> T;   
    
    for (int k = 0; k < T; k++)        
    {
        cin >> H >> W;
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
            {
                cin >> a[i][j];
                b[i][j] = '*';
            }    
            
        ch = 'a';
        for (int i = 0; i < H; i++)
            for (int j = 0; j < W; j++)
                if (b[i][j] == '*')
                {
                     th = ch;       
                     flow(i, j);
                     if (th == ch) ch++;
                }
        
       cout << "Case #" << k+1 << ":" << endl;
       for (int i = 0; i < H; i++)
       {
            cout << b[i][0];
            for (int j = 1; j < W; j++)
                cout << " " << b[i][j]; 
            cout << endl;
       }
    }
    
    
    
    cout.close();
    cin.close();
    //system("PAUSE");
    return EXIT_SUCCESS;
}
