#include <iostream>
#include <fstream>

using namespace std;

int main( )
{
  ifstream inData( "B-large.in" );
  ofstream outData( "B-large.out" );

  int T, N, S, p, total, totalSur;
  inData >> T;
  int score, partialScore, modScore;

  cout << T<< endl;

  for( int t=0; t<T; t++ ){
    total = 0; totalSur = 0;
    inData >> N; inData >> S; inData >> p;
    cout << N << " " << S << " " << p << endl;
    for( int n=0; n<N; n++ ){
      inData >> score;
      partialScore = (int) score/3;
      modScore = score % 3;
      if( partialScore >= p ){
	total++; totalSur++; 
      }else{
	switch( modScore ){
	case 0:
	  if( partialScore + 1 >= p && partialScore > 0)
	    totalSur++;
	  break;
	case 1:
	  if( partialScore + 1 >= p ){
	    total++;
	    totalSur++;
	  }
	  break;
	default:
	  if( partialScore + 1 >= p )
	    total++;
	  if( partialScore + 2 >= p )
	    totalSur++;
	  break;
	}
      }
    }
    int partial = totalSur - total;
    if( partial > S ) 
      partial = S;
    outData << "Case #" << t+1 << ": " << (total + partial) << endl;
  }

  inData.close();
  outData.close();

  return 0;
}
