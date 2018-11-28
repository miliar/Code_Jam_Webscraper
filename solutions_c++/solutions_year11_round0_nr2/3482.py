/*
   Google Code Jam - Qualification Round 2011
   Problem B. Magicka

   George Vafiadis
*/

#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <list>
#include <map>
using namespace std;

// Base elements: {Q, W, E, R, A, S, D, F}

#define JOIN(X,Y)   joins [X-'A'][Y-'A']
#define OPPOSE(X,Y) oppose[X-'A'][Y-'A']
#define REMEMBER(X)  ++letters[X-'A']
#define FORGET(X)  --letters[X-'A']
#define INIT    for(int i = 0; i < 8; ++i) \
                     for(int j = 0; j < 8; ++j) \
                     { \
                         JOIN  (base[i], base[j]) = 0; \
                         OPPOSE(base[i], base[j]) = false; \
                     } \

char joins[26][26]  = {0};
bool oppose[26][26] = {false};
char base[] = "QWERASDF";

void readBBN()
{
  int C;
  cin >> C;
  for(int i = 0; i < C; ++i)
   {
     char c1, c2, c3;
     cin >> c1 >> c2 >> c3;
     JOIN(c1, c2) = JOIN(c2, c1) = c3;
   }
}

void readBB()
{
  int D;
  cin >> D;
  for(int i = 0; i < D; ++i)
  {
    char c1, c2;
    cin >> c1 >> c2;
    OPPOSE(c1, c2) = OPPOSE(c2, c1) = true;
  }
}

int main(int argc, char * argv[])
{
 int T;

 cin >> T;
 for(int test = 0; test < T; ++test)
  {
   int N;
   int letters[26]  = {0};
   char result[101];
   int stackIndex = 0;

   INIT;

   readBBN();
   readBB();

   cin >> N;

  for(int i = 0; i < N; ++i)
   {
     char c;
     cin >> c;

     if( stackIndex == 0 )
      {
        result[stackIndex++] = c;
        REMEMBER(c);
      }
     else
     {
       char & top = result[stackIndex-1];
       char s;

         if( (s = JOIN(c, top) ) != 0 )
          {
            FORGET(top);
            REMEMBER(s);
            top = s;
          }
         else
          {
            for(int k = 0; k < 26; ++k)
                if( letters[k] != 0 && OPPOSE('A' + k, c) )
                 {
                    stackIndex = 0;
                    for(int i = 0; i < 26; ++i)
                      letters[i] = 0;
                    break;
                 }

            if( stackIndex != 0 )
            {
              result[stackIndex++] = c;
              REMEMBER(c);
            }
          }
     }
   }

  cout << "Case #" << (test+1) << ": ";
  cout << "[";
  if( stackIndex > 0 )
   {
     cout << result[0];
     for(int i = 1; i < stackIndex; ++i)
          cout << ", " << result[i];
   }
  cout << "]" << endl;

 }

 return 0;
}
