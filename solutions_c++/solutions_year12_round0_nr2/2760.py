#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;

int a[32][3] = { { 0, 0, 0 },
                 { 1, 0, 0 },
                 { 1, 1, 0 },
                 { 1, 1, 1 },
                 { 2, 1, 1 },
                 { 2, 2, 1 },
                 { 2, 2, 2 },
                 { 2, 2, 3 },
                 { 3, 3, 2 },
                 { 3, 3, 3 },
                 { 3, 3, 4 },
                 { 4, 4, 3 },
                 { 4, 4, 4 },
                 { 4, 4, 5 },
                 { 5, 5, 4 },
                 { 5, 5, 5 },
                 { 5, 5, 6 },
                 { 6, 6, 5 },
                 { 6, 6, 6 },
                 { 6, 6, 7 },
                 { 7, 7, 6 },
                 { 7, 7, 7 },
                 { 7, 7, 8 },
                 { 8, 8, 7 },
                 { 8, 8, 8 },
                 { 8, 8, 9 },
                 { 9, 9, 8 },
                 { 9, 9, 9 },
                 { 9, 9, 10 },
                 { 10, 10, 9 },
                 { 10, 10, 10 },
                };
                 

bool check( int t, int &S1, int P )
{ 
  if( a[t][0] >= P || a[t][1] >= P || a[t][2] >= P )  return 1;
  
  if( S1 > 0 )
  { 
    if( a[t][0] == P-1 && (a[t][1]-1 >= 0 || a[t][2]-1 >= 0) ||
        a[t][1] == P-1 && (a[t][0]-1 >= 0 || a[t][2]-1 >= 0) ||
        a[t][2] == P-1 && (a[t][0]-1 >= 0 || a[t][1]-1 >= 0) )  { S1--; return 1; }
    return 0;
   }
  return 0;
}


int main()
{ 
  ofstream fout;
  fout.open("B-small.txt");
  
  int T, N, S, P, t[100];
  
  scanf("%d", &T);
  
  int k = 1;
  while( k <= T )
  { 
    scanf("%d %d %d", &N, &S, &P);
    
    for( int i = 0; i < N; i++ )
    scanf("%d", &t[i]);
    
    int br = 0, S1 = S;
    for( int i = 0; i < N; i++ )
    if( check(t[i], S1, P) )  br++;
    
    fout << "Case #" << k << ": " << br << endl;
    //cout << br << endl;
    k++;
   }
  
  fout.close();
  
  //scanf("%d", &T);
  return 0;
}
/*
4
3 1 5 15 13 11
3 0 8 23 22 21
2 1 1 8 0
6 2 8 29 20 8 18 18 21


Case #1: 3
Case #2: 2
Case #3: 1
Case #4: 3
*/
