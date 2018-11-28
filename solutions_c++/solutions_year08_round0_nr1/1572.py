using namespace std;

#include <iostream>
#include <string.h>
#include <cstdlib>
#include <fstream>

int N;
int S;
int Q;

// There may be up to 20 cases
int results[20];

// There may be up to 100 search engines in each case
char * engines[100];
// There may be up to 1000 queries in each case
char * queries[1000];

// Each engine choice leads to a minimum number of
// switches at each query point
int min_switch[100][1000];

int main() {

  bool done=false;

  int i, j, k, l;

  // Each search engine name may be up to 100 characters
  for (i=0; i< 100; i++) {
    engines[i] = (char * ) malloc(sizeof(char) * 100);
  }
  for (i=0; i< 1000; i++) {
    queries[i] = (char * ) malloc(sizeof(char) * 100);
  }

  cin >> N; cin.ignore();

  for (i=0; i<N; i++) {

    cin >> S; cin.ignore();
    for (j=0; j<S; j++) {
      // read in search engine names for this case
      cin.getline(engines[j], 100);
    }

    cin >> Q; cin.ignore();
    for (j=0; j<Q; j++) {
      // read in queries for this case
      cin.getline(queries[j], 100);
    }

    // If there are no queries, then this case needs 0 switches!
    if ( Q == 0 ) {
      results[i] = 0;
      continue;
    }

    k = Q-1;
    // At the last query, the engine that matches the query
    // has to switch, the others don't have any more switches
    for (j=0; j<S; j++) {
      if ( strcmp( engines[j], queries[k] ) != 0 ) {
	min_switch[j][k] = 0;
      }
      else {
	min_switch[j][k] = 1;
      }
    }

    for ( k=Q-2 ; k >= 0 ; k-- ) {
      for (j=0; j<S; j++) {
	if ( strcmp( engines[j], queries[k] ) != 0 ) {
	  min_switch[j][k] = min_switch[j][k+1];
	}
	else {
	  // if we have to switch, we switch to the engine
	  // that has the minimum switches from this point
	  // onwards
	  min_switch[j][k] = Q;
	  for (l=0; l<S; l++) {
	    if ( l != j && (min_switch[l][k+1] < min_switch[j][k]) ) {
	      min_switch[j][k] = min_switch[l][k+1];
	    }
	  }
	  // We need to add a switch
	  min_switch[j][k] = min_switch[j][k] + 1;
	}
      }
    }

    // Now find the engine with the minimum switches before the initial
    // query
    results[i] = min_switch[0][0];
    for (j=0; j<S; j++) {
      if ( min_switch[j][0] < results[i] ) {
	results[i] = min_switch[j][0];
      }
    }
  }

  for (i=0; i<N; i++) {
    cout << "Case #" << i+1 << ": " << results[i] << endl;
  }
  
}
