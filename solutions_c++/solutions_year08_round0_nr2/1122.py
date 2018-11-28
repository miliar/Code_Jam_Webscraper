#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<stdio.h>

#define INF (int)1e9

using namespace std ;

int stA[110] , stB[110] , arA[110] , arB[110] ;

int N , T , NA , NB ;


pair<int,int> cal()
{
   sort(stA,stA+NA) ;
   sort(stB,stB+NB) ;
   sort(arA,arA+NB) ;
   sort(arB,arB+NA) ;
   
   pair<int,int> out = make_pair(0,0) ;
   int i , j ;
   for(i=0,j=0;i<NB && j<NA;++j)
   {
      if(arA[i] <= stA[j]) ++i ;
      else ++out.first ;
   }
   for(;j<NA;++j) ++out.first ;
   for(i=0,j=0;i<NA && j<NB;++j)
   {
      if(arB[i] <= stB[j]) ++i ;
      else ++out.second ;
   }
   for(;j<NB;++j) ++out.second ;
   return out ;
}


int main()
{
   ifstream fin("B-large.in") ;
   ofstream fout("output.txt") ;
   fin >> N ;
   int i , j , tm ;
   string tp ;
   for(i=1;i<=N;++i)
   {
      fin >> T ;
      fin >> NA >> NB ;
      for(j=0;j<NA;++j)
      {
         fin >> tp ;
         tm = ((tp[0]-'0')*10 + (tp[1]-'0'))*60 + ((tp[3]-'0')*10 + (tp[4]-'0')) ;
         stA[j] = tm ;
         fin >> tp ;
         tm = ((tp[0]-'0')*10 + (tp[1]-'0'))*60 + ((tp[3]-'0')*10 + (tp[4]-'0')) ;
         arB[j] = tm + T ;
      }
      for(j=0;j<NB;++j)
      {
         fin >> tp ;
         tm = ((tp[0]-'0')*10 + (tp[1]-'0'))*60 + ((tp[3]-'0')*10 + (tp[4]-'0')) ;
         stB[j] = tm ;
         fin >> tp ;
         tm = ((tp[0]-'0')*10 + (tp[1]-'0'))*60 + ((tp[3]-'0')*10 + (tp[4]-'0')) ;
         arA[j] = tm + T ;
      }
      pair<int,int> tp = cal() ;
      fout << "Case #" << i << ": " << tp.first << " " << tp.second << endl ;
   }
   return 0 ;
}
