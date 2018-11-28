#include <string>
#include <vector>
#include <iostream>
#include <map>
using namespace std;

int sub1(){
 
  int N;
  int S;
  int p;
  cin >> N;
  cin >> S;
  cin >> p;
  vector<int> t(N);
  for ( int i=0 ; i<N ; i++ )
    cin >> t[i];

  /*
  cout << N <<", "<< S <<","<< p << " ";  
  for ( int i=0 ; i<N ; i++ )
    cout <<","<< t[i] ;
  cout << endl;  
  */
  int score[N][3];
  for ( int i=0 ; i<N ; i++ ){
    score[i][0]= t[i]/3;
    score[i][1]=(t[i] - score[i][0])/2;
    score[i][2]= t[i] - score[i][0] - score[i][1];
  }
  
  int ret=0;
  for ( int i=0 ; i<N ; i++ ){
    int tmax=-1;
    for ( int j=0 ; j<3 ; j++ )
      tmax=max(tmax, score[i][j] );
    
    if (tmax>=p)
      ret++;
    if (tmax==p-1 && score[i][1]==score[i][2] && S>0 && tmax!=0){
      ret++;
      S--;
      //cout << "(*) ";
    }
    
    //cout << score[i][0] <<","<<  score[i][1] <<","<< score[i][2] <<endl;
    
  }
  return ret;
}


int main (int argc, char*argv[]){

  int T;
  cin >> T;
  
  for ( int i=0 ; i<T ; i++ ){
    cout << "Case #" << i+1 << ": " ;
    /*
      for ( unsigned int j=0 ; j<G[i].size() ; j++ )
      if ( 'a'<=G[i][j] && G[i][j]<='z' )
      cout << table[G[i][j]-'a'] ;
      else
      cout << ' ' ;
      }*/
    
    cout << sub1();
    
    cout << endl;
  }
 
  
  return 1;
};


