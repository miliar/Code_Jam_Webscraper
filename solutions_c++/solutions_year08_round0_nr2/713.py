#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std ;

#define FILEIO
#define debug1

struct TimeTable
{
  string s, e ;
  int sh, sm, eh, em ;
} ;

class Comp
{
public:
  bool operator() ( const TimeTable &s1, const TimeTable &s2 ){
    return s1.s < s2.s ;
  }
} ;

class Comp2
{
public:
  bool operator() ( const TimeTable &s1, const TimeTable &s2 ){
    return s1.e < s2.e ;
  }
} ;

string MakeTime( string s, int time )
{
  string result ;

  istringstream iss(s) ;
  int h, m ;
  char c ;
  iss >> h >> c >> m ;
#ifdef debug
  cout << "S = " << s << ": " ;
  cout << h << " " << m << endl ;
#endif
  m += time ;
  if ( m >= 60 ){
    ++h ;
    m -= 60 ;
  }
  if ( h >= 24 ) 
    result = "77:77" ;
  else {
    ostringstream oss ;
    if ( h < 10 )  oss << "0" ;
    oss << h ;
    oss << ":" ;
    if ( m < 10 )  oss << "0" ;
    oss << m ;
    result = oss.str() ;
  }

  return result ;
}

int main( void )
{
#ifdef FILEIO
  freopen( "B-large.in", "r", stdin ) ;
  freopen( "B-l.out", "w", stdout ) ;
#endif

  int N, T, NA, NB ;
  int case_counter = 1 ;
  cin >> N ;
  TimeTable stationA[101], stationB[101] ;
  string temptime ;

  int resultA, resultB ;
  while ( N-- ){
    cin >> T >> NA >> NB ;
    if ( NA == 0 ){  
      cout << "Case #" << case_counter++ << ": " << 0 << " " << NA << endl ;
      continue ;
    }
    if ( NB == 0 ){
      cout << "Case #" << case_counter++ << ": " << NA << " " << 0 << endl ;      
      continue ;
    }
    for ( int i = 0 ; i < NA ; ++i ){
      cin >> temptime ;
      stationA[i].s = temptime ;
      cin >> temptime ;
      stationA[i].e = temptime ;
    }
    for ( int i = 0 ; i < NB ; ++i ){
      cin >> temptime ;
      stationB[i].s = temptime ;
      cin >> temptime ;
      stationB[i].e = temptime ;
    }
    sort( stationA, stationA+NA, Comp() ) ;
    sort( stationB, stationB+NB, Comp() ) ;
#ifdef debug
    cout << stationB[0].s << " " << stationB[1].s << endl ;
#endif
    resultA = resultB = 0 ;
    int trainInA = 0, trainInB = 0 ;
    vector<string> trainToB, trainToA ;
    int ptrA, ptrB ;
    ptrA = ptrB = 0 ;
    string startTimeA, startTimeB, arriveTimeA = "", arriveTimeB = "" ;
    // initialize
    startTimeA = stationA[0].s ;
    startTimeB = stationB[0].s ;
    trainToB.push_back(stationA[0].e) ;
    trainToA.push_back(stationB[0].e) ;
    arriveTimeA = MakeTime(stationB[0].e, T) ;
    arriveTimeB = MakeTime(stationA[0].e, T) ;
    while ( true ){
      if ( arriveTimeA <= arriveTimeB && arriveTimeA <= startTimeA &&
	   arriveTimeA <= startTimeB ) // Train arrive at A first
      {
	++trainInA ;
	pop_heap(trainToA.begin(), trainToA.end(), greater<string>() ) ;
	trainToA.pop_back() ; 
	if ( !trainToA.empty() )
	  arriveTimeA = MakeTime(trainToA[0], T) ;
	else
	  arriveTimeA = "77:77" ;
#ifdef debug
	cout << arriveTimeA << endl ;
#endif
      }
      else if ( arriveTimeB <= arriveTimeA && arriveTimeB <= startTimeA &&
		arriveTimeB <= startTimeB ){
	++trainInB ;
	pop_heap(trainToB.begin(), trainToB.end(), greater<string>() ) ;
	trainToB.pop_back() ;
	if ( !trainToB.empty() ){
	  arriveTimeB = MakeTime(trainToB[0], T) ;
	}
	else
	  arriveTimeB = "77:77" ;
#ifdef debug
	cout << arriveTimeB << endl ;
#endif
      }
      else if ( startTimeA <= arriveTimeA && startTimeA <= arriveTimeB &&
		startTimeA <= startTimeB ){
	if ( trainInA == 0 ){
	  ++resultA ;
	  //++trainInA ;
	}
	else
	  --trainInA ;
	++ptrA ;
	if ( ptrA < NA ){
	  trainToB.push_back(stationA[ptrA].e) ;
	  push_heap(trainToB.begin(), trainToB.end(), greater<string>() ) ;
	  arriveTimeB = MakeTime(trainToB[0], T) ;
	  startTimeA = stationA[ptrA].s ;
	  //++ptrA ;
	}
	else{
	  //arriveTimeA = "77:77" ;
	  startTimeA = "77:77" ;
	}
#ifdef debug
	cout << startTimeA << endl ;
#endif
      }
      else if ( startTimeB <= arriveTimeA && startTimeB <= arriveTimeB &&
		startTimeB <= startTimeA ){
	if ( trainInB == 0 ){
	  ++resultB ;
	  //++trainInB ;
	}
	else
	  --trainInB ;
	++ptrB ;
	if ( ptrB < NB ){
	  trainToA.push_back(stationB[ptrB].e) ;
	  push_heap(trainToA.begin(), trainToA.end(), greater<string>() ) ;
	  arriveTimeA = MakeTime(trainToA[0], T) ;	  
	  startTimeB = stationB[ptrB].s ;
	}
	else{
	  //arriveTimeB = "77:77" ;
	  startTimeB = "77:77" ;
	}
#ifdef debug
	cout << startTimeB << endl ;
#endif
      }

      if ( ptrA >= NA && ptrB >= NB )   break ;
      /*
      startTimeA = stationA[ptrA].s ;
      statTimeB = stationB[ptrB].s ;
      if ( !trainToA.empty() ){
	arriveTimeA = MakeTiem(trainToA[0], T) ;
      }
      if ( !trainToB.empty() ){
	arriveTimeB = MakeTime(trainToB[0], T) ;
      }

      if ( arr

      // train arrive at A before the next start time.
      if ( startTimeA >= arriveTimeA ){
	pop_heap( trainToA.start(), trainToA.end(), greater<string>() ) ;
	trainToA.pop_back() ;
	// put this train in trainToB ;
	trainToB.push_back(stationA[ptrA].e) ;
	push_heap( trainToB.begin(), trainToB.end(), greater<string>() ) ;
      }

      */
    }
    cout << "Case #" << case_counter++ << ": " << resultA << " " << resultB << endl ;
  }

  return 0 ;
}
