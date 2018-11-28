using namespace std;

#include <iostream>
#include <string.h>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>


int N;
int n;

// There may be up to 10 cases
int results[10];

long long x[100000];
long long y[100000];

int main() {

  bool done=false;

  long long A, B, C, D, M;

  long long a, b, c;

  int i, j, k, l;

  cin >> N; cin.ignore();

  for (i=0; i<N; i++) {
    results[i] = 0;
  }

  for (i=0; i<N; i++) {

    cin >> n; // cin.ignore();

    cin >> A; // cin.ignore();

    cin >> B; // cin.ignore();

    cin >> C; // cin.ignore();

    cin >> D; // cin.ignore();

    cin >> x[0]; // cin.ignore();

    cin >> y[0]; // cin.ignore();

    cin >> M; // cin.ignore();

    for (j=1; j<n; j++) {
      x[j] =(A * x[j-1] + B) % M;
      y[j] =(C * y[j-1] + D) % M;
    }
    /*
    for (j=0; j<n; j++) {
      // read in search engine names for this case
      cout << "(" << x[j] << ", " << y[j] << ") ";
    }
    cout << endl;
    */

    for (j=0; j<n; j++) {
      a = j;
      for (k=j+1; k<n; k++) {
	b = k;
	for (l=k+1; l<n; l++) {
	  c = l;
	  if ( (x[a] + x[b] + x[c]) % 3 == 0 
	       && (y[a] + y[b] + y[c]) % 3 == 0 ) {
	    results[i]++;
	  }
	}
      }
    }

    /*
    cout << endl;
    for (j=0; j<n; j++) {
      // read in search engine names for this case
      cout << y[j] << " ";
    }
    cout << endl;

    minimum = 0;
    for (j=0; j<n; j++) {
      minimum = minimum + x[j]*y[j];
    }
    cout << "min " << minimum << endl;
    */

    /*
    cout << "start permuting test:\n";
    vector<int> the_vector;
    vector<int>::iterator the_iterator;

    for( int i=0; i < n; i++ )
      the_vector.push_back(i);

    the_iterator = the_vector.begin();
    while ( the_iterator != the_vector.end() ) {
      cout << *the_iterator << " ";
      the_iterator++;
    }
    cout << endl;
    while ( next_permutation( the_vector.begin(), the_vector.end() ) ) {
      the_iterator = the_vector.begin();
      while ( the_iterator != the_vector.end() ) {
	cout << *the_iterator << " ";
	the_iterator++;
      }
      cout << endl;
    }
    cout << "end permuting test:\n";
    */
    /*
    vector<int> the_vector;
    vector<int>::iterator the_iterator;

    for( j=0; j < n; j++ )
      the_vector.push_back(j);

    minimum = 0;
    j = 0;
    the_iterator = the_vector.begin();
    while ( the_iterator != the_vector.end() ) {
      minimum = minimum + x[j]*y[*the_iterator];
      the_iterator++;
      j++;
    }

    while ( next_permutation( the_vector.begin(), the_vector.end() ) ) {
      score = 0;
      j = 0;
      the_iterator = the_vector.begin();
      while ( the_iterator != the_vector.end() ) {
	score = score + x[j]*y[*the_iterator];
	the_iterator++;
	j++;
      }
      if ( score < minimum ) {
	minimum = score;
      }
    }

    results[i] = minimum;
    */
  }

  for (i=0; i<N; i++) {
    cout << "Case #" << i+1 << ": " << results[i] << endl;
  }

}
