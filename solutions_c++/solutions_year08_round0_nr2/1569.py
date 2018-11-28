using namespace std;

#include <iostream>
#include <string.h>
#include <cstdlib>
#include <fstream>

#define MINUTES_IN_DAY 24*60
int N;
int NA, NB;
int TOTAL; // Total number of trips
int T;

// There may be up to 100 cases, each with a pair of results
int results[100][2];

// There may be up to 100 train trips each way: A to B, and  B to A
int * trips[200];

// Trips sorted based on start times
int * start_sorted_trips[200];

// To keep track of how many trains there are at A and B
int trains_at_A[MINUTES_IN_DAY];
int trains_at_B[MINUTES_IN_DAY];

int main() {

  int i, j, k, l;

  int hh, mm;

  int temp1, temp2, temp3;

  int min, min_index;

  int previous_time; // The time of the last trip handled so far
  
  // Data about current trip
  int current_time;
  int current_trip_end_time;
  int current_direction;


  // Each trip has a direction, start time and end time
  for (i=0; i< 200; i++) {
    trips[i] = (int * ) malloc(sizeof(int) * 3);
    start_sorted_trips[i] = (int * ) malloc(sizeof(int) * 3);
  }
  
  cin >> N; cin.ignore();
  
  for (i=0; i<N; i++) {
    
    // To begin, assume no trains are needed at either station
    results[i][0] = results[i][1] = 0;

    cin >> T; cin.ignore();
    
    cin >> NA; cin >> NB; cin.ignore();
    
    TOTAL = NA + NB;

    for (j=0; j< NA ; j++) {
      // set direction
      trips[j][2] = 0;
      // read in trip start and end times
      cin >> hh ; cin.ignore(); cin >> mm;
      trips[j][0] = 60*hh + mm;
      cin >> hh ; cin.ignore(); cin >> mm; cin.ignore();
      trips[j][1] = 60*hh + mm;
    }
    
    for (j=NA; j<TOTAL; j++) {
      // set direction
      trips[j][2] = 1;
      // read in trip start and end times
      cin >> hh ; cin.ignore(); cin >> mm;
      trips[j][0] = 60*hh + mm;
      cin >> hh ; cin.ignore(); cin >> mm; cin.ignore();
      trips[j][1] = 60*hh + mm;
    }

    /* To test that the input was read in and processed correctly:    
    cout << "Trips:" << endl;
    for (j=0; j<TOTAL; j++) {
      // read in trip start and end times
      cout << trips[j][0] << " " << trips[j][1] << " direction " << trips[j][2] << endl ;
    }
    */

    // If there are no trips from a station, 
    // then no trains are needed from there, 
    // and all trips from the other station need their own train
    if ( NA == 0 || NB == 0) {
      results[i][0] = NA;
      results[i][1] = NB;
      continue;
    }

    // Now sort trips based on start times
    
    // First make a copy
    for (j=0; j<TOTAL; j++) {
      start_sorted_trips[j][0] = trips[j][0];
      start_sorted_trips[j][1] = trips[j][1];
      start_sorted_trips[j][2] = trips[j][2];
    }
    // Now sort
    for (j=0; j<TOTAL; j++) {
      min = start_sorted_trips[j][0];
      min_index = j;
      for (k=j; k<TOTAL; k++) {
	if ( start_sorted_trips[k][0] < min ) {
	  min = start_sorted_trips[k][0];
	  min_index = k;
	}
      }
      if (min_index != j) {
	  temp1 = start_sorted_trips[j][0];
	  temp2 = start_sorted_trips[j][1];
	  temp3 = start_sorted_trips[j][2];
	  start_sorted_trips[j][0] = start_sorted_trips[min_index][0];
	  start_sorted_trips[j][1] = start_sorted_trips[min_index][1];
	  start_sorted_trips[j][2] = start_sorted_trips[min_index][2];
	  start_sorted_trips[min_index][0] = temp1;
	  start_sorted_trips[min_index][1] = temp2;
	  start_sorted_trips[min_index][2] = temp3;
      }
    }

    /* To test that the trips were sorted correctly
    cout << "Sorted Trips:" << endl;
    for (j=0; j<TOTAL; j++) {
      // read in trip start and end times
      cout << start_sorted_trips[j][0] << " " 
           << start_sorted_trips[j][1] << " direction " 
           << start_sorted_trips[j][2] << endl ;
    }
    */

    // Now go down the list of trips and check if there's
    // a train at the beginning of each trip.  
    // If not, allocate a new train
    // Each trip makes a new train available at the other station at the end time + turnaround

    previous_time = 0;  // The time of the last trip handled so far

    // No trains at either station initially
    for (j=0; j< MINUTES_IN_DAY; j++) {
      trains_at_A[j] = 0;
      trains_at_B[j] = 0;
    }

    for (j=0; j<TOTAL; j++) {

      current_time = start_sorted_trips[j][0];
      current_trip_end_time = start_sorted_trips[j][1];
      current_direction = start_sorted_trips[j][2];

      // Any trains already at stations are still there: common sense law of inertia!
      for (k=previous_time; k < current_time; k++) {
	trains_at_A[current_time] = trains_at_A[current_time] + trains_at_A[k];
	trains_at_B[current_time] = trains_at_B[current_time] + trains_at_B[k];
      }

      /* To test that the train numbers are calculated correctly
      cout << "Trip: " << start_sorted_trips[j][0] << " " 
	   << start_sorted_trips[j][1] << " direction " 
	   << start_sorted_trips[j][2] << ".  Trains at A:"
	   << trains_at_A[current_time] << "  Trains at B:"
	   << trains_at_B[current_time]
	   << endl ;
      */

      previous_time = current_time;

      if ( current_direction == 0 ) {
	if ( trains_at_A[current_time] > 0 ) {
	  // Use one of the trains
	  trains_at_A[current_time]--;
	}
	else {
	  // Add a train to A
	  results[i][0]++;
	}
	// Increase number of trains at B at the arrival time + turnaround
	if ( (current_trip_end_time + T) < MINUTES_IN_DAY ) {
	  trains_at_B[current_trip_end_time + T]++;
	}
	else {
	  // The train won't be available any more today
	}
      }
      else {
	if ( trains_at_B[current_time] > 0 ) {
	  // Use one of the trains
	  trains_at_B[current_time]--;
	}
	else {
	  // Add a train to A
	  results[i][1]++;
	}
	// Increase number of trains at B at the arrival time + turnaround
	if ( (current_trip_end_time + T) < MINUTES_IN_DAY ) {
	  trains_at_A[current_trip_end_time + T]++;
	}
	else {
	  // The train won't be available any more today
	}
      }
    }

  }   

  for (i=0; i<N; i++) {
    cout << "Case #" << i+1 << ": " 
	 << results[i][0] << " " 
	 << results[i][1] << endl;
  }

}
