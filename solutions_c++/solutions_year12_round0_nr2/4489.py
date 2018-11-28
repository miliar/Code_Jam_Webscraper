#include<iostream>
#include<string.h>
#include<fstream>
using namespace std ;

int score[100] ;
int avg_score[100] ;
int flag[100] ;
ifstream f_cin("b.txt");
int main()
{
  int case_count ;
  int N , S , P;
  f_cin >> case_count ; 
  for(int order = 1 ; order <= case_count ; ++ order )
    {
      memset(flag,0,sizeof(flag)) ;
      f_cin >> N >> S >> P ; 
      for( int i = 0 ; i < N ; ++ i )
        {
          f_cin >> score[i] ; 
          avg_score[i] = (score[i] + 2)/ 3 ;
          if( score[i] % 3 == 0 && score[i] ) flag[i] = 1 ;
          if( score[i] % 3 == 1 ) flag[i] = 0; 
          if( score[i] % 3 == 2 ) flag[i]= 1 ; 
        }
      int count = 0 ;
      for( int i = 0 ; i < N ; ++ i )
        {
          if( avg_score[i] >= P ) { count ++ ;  continue ; }
          if( avg_score[i] >= P-flag[i] && S ) { count ++ ; --S ;}
        }
      cout << "Case #"<<order<<": "<< count << endl ;
    }

}
