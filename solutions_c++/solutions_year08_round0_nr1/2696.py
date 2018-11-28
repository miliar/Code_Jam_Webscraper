#include <iostream>
#include <vector>
#include <string>



using namespace std;


int main() {
  int N;
  int S;
  int Q;
  string tmp;
  getline( cin, tmp );
  N = atoi( tmp.c_str() );
  //cerr << N << endl;
  
  for(int n = 1; n <= N; n++) {
    getline( cin, tmp );
    S = atoi( tmp.c_str() );
    //cerr << S << endl;
    vector<string> ss;
    for(int i = 0; i < S; i++) {
      getline( cin, tmp );
      ss.push_back(tmp);
      //cerr << tmp << endl;
    }

    getline( cin, tmp );
    Q = atoi( tmp.c_str() );
    //cerr << Q << endl;
    vector<string> qs;
    for(int i = 0; i < Q; i++) {
      getline( cin, tmp );
      qs.push_back(tmp);
      //cerr << tmp << endl;
    }

    vector< vector<int> > a = vector< vector<int> >( Q + 1, 
						     vector<int>( S, 0 ) );
    for(int i = 0; i < Q; i++) {
      for(int j = 0; j < S; j++) {
	if( qs[i] == ss[j] ) {
	  a[i+1][j] = Q + 1;
	}
	else {
	  int min = Q + 1;
	  for(int k = 0; k < S; k++) {
	    if( j != k && a[i][k] + 1 < min ) {
	      min = a[i][k] + 1;	      
	    }
	    else if( j == k && a[i][k] < min ) {
	      min = a[i][k];
	    }
	  }
	  a[i+1][j] = min;
	}
      }
    }

    int min = Q + 1;
    for(int k = 0; k < S; k++)
      if( a[Q][k] < min ) min = a[Q][k];

    cout << "Case #" << n << ": " << min << endl;
  }


  return 0;
}

