#include <iostream>
#include <cstdio>
#include <fstream>
#include <cstdlib>
#include <set>
using namespace std;

int br;

void check( int n, int A, int B )
{ 
  // pravim "i" string chrez itoa(i, string, 10);
  // mestim otzad napred i za vsqko premestvane pravim string-a v int(cqlo chislo) chrez atoi(string)
  // proverqvame dali poluchenoto e po-malko ili ravno na B, ako e taka broim go
  // ako ne, prodyljavame s mesteneto; obsht broi premestvaniq -> kolkoto digits-1 e chisloto
  // stava slojnost O( abs(A-B)*7 ), t.e. v nai-loshiq sluchai e O( 1000000 * 7 )
  
  set <int> s;
  
  char S[10];
  itoa(n, S, 10);
  int sz = strlen(S);
  
  int k = 0;
  while( k < sz-1 )
  { 
    char ch = S[sz-1];
    for( int j = sz-1; j >= 1; j-- )
    S[j] = S[j-1];
    S[0] = ch;
    
    int m = atoi(S);
    if( A <= m && m <= B && n < m )  s.insert(m);
    
    k++;
   }
  
  br += s.size();
}


int main()
{ ofstream fout;
  int T, A, B;
  
  scanf("%d", &T);
  
  fout.open("C-large.txt");
  
  int k = 1;
  while( k <= T )
  { 
    br = 0;
    fout << "Case #" << k << ": ";
    
    scanf("%d %d", &A, &B);
    for( int i = A; i <= B; i++ )
    check(i, A, B);
    
    fout << br << endl;
    
    k++;
   }
  
  fout.close();
  
  //scanf("%d", &T);
  return 0;
}
/*
102400 bytes
Input 

Output 
 
4
1 9
10 40
100 500
1111 2222

Case #1: 0
Case #2: 3
Case #3: 156
Case #4: 287

*/
