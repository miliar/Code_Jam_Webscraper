using namespace std;

#include <iostream>
#include <string.h>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>


int N;
int n;

// There may be up to 1000 cases
int results[1000];

long x[800];
long y[800];

long minimum;
long score;

int main() {

  bool done=false;

  int i, j, k, l;

  cin >> N; cin.ignore();

  for (i=0; i<N; i++) {

    cin >> n; // cin.ignore();

    for (j=0; j<n; j++) {
      cin >> x[j];
    }

    for (j=0; j<n; j++) {
      cin >> y[j];
    }

    /*
    for (j=0; j<n; j++) {
      // read in search engine names for this case
      cout << x[j] << " ";
    }
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
  }

  for (i=0; i<N; i++) {
    cout << "Case #" << i+1 << ": " << results[i] << endl;
  }

}
