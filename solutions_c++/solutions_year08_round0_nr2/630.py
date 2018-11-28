#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>

using namespace std;

typedef char searchName_t[101];
searchName_t input;
searchName_t searchEngines[103];
searchName_t queries[1003];
int queryAsInt[1003];
bool queriedEngine[103];

struct schedule {
  int depart;
  int arrive;
  bool handled;
};

int  numberCases;

int  turnaroundTime;
int  numberABTimes;
int  numberABLeft;
schedule  ABTimes[100];
int  numberBATimes;
int  numberBALeft;
schedule  BATimes[100];
int  numAB;
int  numBA;

int  numABReady;
int  numBAReady;
struct clockSchedule {
  int canGoAB;
  int canGoBA;
};
clockSchedule clockSched[60 * 24 + 300];


ifstream inFile;
ofstream outFile;


bool allTrainsDone(void){
  int counter;

  for(counter = 0; counter < numberABTimes; counter++) {
    if (ABTimes[counter].handled == false)
      return false;
  }
  for(counter = 0; counter < numberBATimes; counter++) {
    if (BATimes[counter].handled == false)
      return false;
  }
  return true;

}

int translateTimeToInt(int hour, int minute) {
  int timeAsInt;
  timeAsInt = (hour * 60) + minute;
  return timeAsInt;
}

void runSchedule(void) {
  numABReady = numBAReady = 0;
  memset(clockSched, 0, sizeof(clockSched));
  int timenow = 0;
  int arrivalTime;

  for (timenow = 0; timenow < 60*24; timenow++) {
    // Increment # trains by ones newly ready.
    numABReady += clockSched[timenow].canGoAB;
    numBAReady += clockSched[timenow].canGoBA;

    // Find all trains that have to leave now and mark them
    for (int traincounter = 0; traincounter < numberABTimes; traincounter++) {
      if (ABTimes[traincounter].depart == timenow) {
        if (numABReady == 0) {
          numAB++;
        } else {
          numABReady--;
        }
        // Figure out arrival time.
        arrivalTime = ABTimes[traincounter].arrive + turnaroundTime;
        if (arrivalTime > (60 * 24)) {
          arrivalTime = 60 * 24;
        }
        clockSched[arrivalTime].canGoBA++;
        ABTimes[traincounter].handled = true;
      }
    }
    for (int traincounter = 0; traincounter < numberBATimes; traincounter++) {
      if (BATimes[traincounter].depart == timenow) {
        if (numBAReady == 0) {
          numBA++;
        } else {
          numBAReady--;
        }
        // Figure out arrival time.
        arrivalTime = BATimes[traincounter].arrive + turnaroundTime;
        if (arrivalTime > (60 * 24)) {
          arrivalTime = 60 * 24;
        }
        clockSched[arrivalTime].canGoAB++;
        BATimes[traincounter].handled = true;
      }
    }
  }
}

void runCase(void) {
  int hour;
  int minute;
  char colon;
  int count; 
  int currentSearch;
  turnaroundTime = 0;
  numAB = numBA = 0;
  numberABTimes = numberBATimes = 0;
  memset (ABTimes, 0, sizeof( ABTimes ));
  memset (BATimes, 0, sizeof( BATimes ));

  inFile >> turnaroundTime;
  inFile.getline(input, sizeof(input));
  inFile >> numberABTimes;
  inFile >> numberBATimes;
  inFile.getline(input, sizeof(input));
  cout << numberABTimes << "," << numberBATimes << endl;

  for (count = 0; count < numberABTimes; count++) {
    ABTimes[count].handled = 0;
    inFile >> hour >> colon >> minute;
    ABTimes[count].depart = translateTimeToInt(hour, minute);
    inFile >> hour >> colon >> minute;
    ABTimes[count].arrive = translateTimeToInt(hour, minute);
    cout << ABTimes[count].depart << "->" << ABTimes[count].arrive << endl;
  }
  for (count = 0; count < numberBATimes; count++) {
    inFile >> hour >> colon >> minute;
    BATimes[count].depart = translateTimeToInt(hour, minute);
    inFile >> hour >> colon >> minute;
    BATimes[count].arrive = translateTimeToInt(hour, minute);
    cout << BATimes[count].depart << "->" << BATimes[count].arrive << endl;
  }

  runSchedule();

}

int main(int argc, char **argv) {
  inFile.open(argv[1]);
  outFile.open("output");

  // First line N
  inFile >> numberCases;

  for (int i = 0; i < numberCases; i++) {
    runCase();
    cout << "Case #" << i+1 << ": " << numAB << " " << numBA << endl;
    outFile << "Case #" << i+1 << ": " << numAB << " " << numBA << endl;
  }

  inFile.close();
  outFile.close();
}
