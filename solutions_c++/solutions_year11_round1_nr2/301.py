#include<iostream> 
#include<stdio.h> 
#include<set> 
#include<vector> 
#include<map> 
#include<string> 
#include<algorithm> 
#include<sstream> 
#include<string.h> 
#include<stdlib.h> 
#include<cmath> 
using namespace std ;
#define MAXD 10002

int n ;
string D[MAXD] ;

vector<string> dic[12] ;
vector<int> ord[12] ;

string solve(string list)
{
 string best = "" ;
 int bestMistakes = -1 ;
 int bestOrd = -1 ;
 
 for(int i = 1;i < 12;i++) if(dic[i].size() > 0)
 {
  for(int j = 0;j < dic[i].size();j++)
  {
   int curMistake = 0,where2[32] = {} ;
   string guess = dic[i][j] ;

   for(int kk = 0;kk < guess.size();kk++)
    where2[guess[kk] - 'a'] |= 1 << kk ;

   int total = dic[i].size(),present = 0 ;
   string consistent[MAXD] ;
   vector<int> where[MAXD] ;
   
   for(int jj = 0;jj < dic[i].size();jj++)
   {
    where[jj].clear() ;
    where[jj].resize(26,0) ;
    for(int kk = 0;kk < dic[i][jj].size();kk++)
     where[jj][dic[i][jj][kk] - 'a'] |= 1 << kk ;

    consistent[jj] = dic[i][jj] ;
    for(int jjj = 0;jjj < consistent[jj].size();jjj++)
     present |= 1 << consistent[jj][jjj] - 'a' ;
   }
  
   for(int k = 0;total > 1 && k < 26;k++)
   {
    if(!(present & 1 << list[k] - 'a')) { continue ; }
    if(where2[list[k] - 'a'] == 0) curMistake++ ;
    
    for(int ii = 0;ii < total;ii++)
     if(where[ii][list[k] - 'a'] != where2[list[k] - 'a'])
      consistent[ii] = "" ;

    present = 0 ;
    int ntotal = 0 ;
    for(int jj = 0;jj < total;jj++) if(consistent[jj] != "")
    {
     for(int jjj = 0;jjj < consistent[jj].size();jjj++)
      present |= 1 << consistent[jj][jjj] - 'a' ;
     where[ntotal] = where[jj] ;
     consistent[ntotal++] = consistent[jj] ;
    }
    total = ntotal ;
   }
 
 //  cout << curMistake << " " << guess << endl ;
   if(curMistake > bestMistakes || curMistake == bestMistakes && ord[i][j] < bestOrd)
   {
    bestMistakes = curMistake ;
    best = guess ;
    bestOrd = ord[i][j] ;
   }
  }
 }
 return best ;
}

void preprocess()
{
 for(int i = 0;i < 12;i++) dic[i].clear(),ord[i].clear() ;
 for(int i = 0;i < n;i++)
 {
  dic[(int)D[i].size()].push_back(D[i]) ;
  ord[(int)D[i].size()].push_back(i) ;
 }
}

int main()
{
 int runs ;
 cin >> runs ;
 for(int t = 1;t <= runs;t++)
 {
  cout << "Case #" << t << ":";
  int q ;
  cin >> n >> q ;
  for(int i = 0;i < n;i++) cin >> D[i] ;
  
  preprocess();
  while(q--)
  {
   string letter ;
   cin >> letter;
   string best = solve(letter) ;
 //  cout << "answer: " << best << endl ;;
   cout << " " << best ;
  }
  cout << endl ;  
 }
 return 0 ;
}
