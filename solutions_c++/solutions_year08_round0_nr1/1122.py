#include<iostream>
#include<fstream>
#include<string>
#include<map>
#include<stdio.h>

#define INF (int)1e9

using namespace std ;

map<string,int> etoi ;
int arr[1010] ;
int t[110] ;

int N , S , Q ;

int cal()
{
   int st = 0 , i , j , out = 0 ;
   while(true)
   {
      if(st >= Q) break ;
      j = S ;
      memset(t,-1,sizeof t) ;
      for(i=st;i<Q && j>0;++i) if(t[arr[i]] == -1) { t[arr[i]] = i ; --j ; }
      if(j>0) break ;
      --i ;
      ++out ;
      st = i ;
   }
   return out ;
}


int main()
{
   FILE * fin = fopen("A-large.in","r") ;
   FILE * fout = fopen("output.txt","w") ;
   fscanf(fin,"%d",&N) ;
   int i , j ;
   char s[110] ;
   for(i=1;i<=N;++i)
   {
      fscanf(fin,"%d",&S) ;
      etoi.clear() ;
      fgetc(fin) ;
      for(j=0;j<S;++j)
      {
         fgets(s,109,fin) ;
         string tp(s) ;
         etoi[tp] = j ;
      }
      fscanf(fin,"%d",&Q) ;
      fgetc(fin) ;
      for(j=0;j<Q;++j) 
      {
         fgets(s,109,fin) ;
         string tp(s) ;
         arr[j] = etoi[tp] ;
      }
      fprintf(fout,"Case #%d: %d\n",i,cal()) ;
   }
   return 0 ;
}
