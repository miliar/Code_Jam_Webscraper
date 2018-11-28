#include<vector>
#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#include<sstream>
#include<queue>
#include<stack>
#include<string>
#include<cmath>
#include<map>
#include<fstream>

#define all(c) c.begin(), c.end()
#define allr(c) c.rbegin(), c.rend()
#define tr(container, it) for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define INF (int)1e9

using namespace std ;
int K ;
string S , tp2 ;
int sz ;
vector<int> tp ;


int cal()
{
   sz = S.length() ;
   int out = sz ;
   int i , j , temp ;
   tp.clear() ;
   for(i=0;i<K;++i) tp.push_back(i) ;
   do
   {
      tp2 = "" ;
      for(i=0;i<sz;i+=K) for(j=0;j<K;++j) tp2.push_back(S[i+tp[j]]) ;
      temp = 0 ;
      for(i=1;i<tp2.size();++i) if(tp2[i] != tp2[i-1]) ++temp ;
      out = min(out,temp) ;
   }
   while(next_permutation(all(tp))) ;
   return out ;
}



int main()
{
   int N ;
   int r ;
   ifstream fin("input.txt") ;
   ofstream fout("output.txt") ;
   fin >> N ;
   for(r=1;r<=N;++r)
   {
      fin >> K >> S ;
      fout << "Case #" << r << ": " << cal() + 1 << endl ;
   }
   
   getchar() ;
   getchar() ;
   return 0 ;
}
