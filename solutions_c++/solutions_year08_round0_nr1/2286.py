#include<stdint.h>
#include<iostream>

using namespace std;

#define MAX_ENGINE_NAME 100

#define MAX_ENGINES 100
#define MAX_QUERIES 1000

#define discardNewLine() cin.getline( buffer, MAX_ENGINE_NAME + 1 )

char engineNames[ MAX_ENGINES ][ MAX_ENGINE_NAME + 1 ];
bool engineFree[ MAX_ENGINES ];

int freeEnginesCount;
int enginesInCase;

char buffer[ MAX_ENGINE_NAME + 1 ];

/**
 *  @brief Marks all engines as unused.
 */
void freeAllEngines() {
  for ( int i = 0; i < enginesInCase; ++i ) {
    engineFree[ i ] = true;
  }
  freeEnginesCount = enginesInCase;
}

/**
 *  @brief returns number of engines that still can be used for a switch
 */
int getEngineNumber( const char * name ) {
  for ( int i = 0; i < enginesInCase; ++i ) {
    if ( 0 == strcmp( name, engineNames[ i ] ) )
      return i;
  }

  cerr << "Query not found in engine list!" << endl;
  exit( 1 );
}


/**
 *  @brief Checks number of switches for case starting on cin.
 */
int countSwitchesOfCurrentCase() {
  // read number of engines
  cin >> enginesInCase; discardNewLine();

  // fill list of engines names
  for ( int i = 0; i < enginesInCase; ++i ) {
    cin.getline( engineNames[ i ], MAX_ENGINE_NAME + 1 );
  }

  // read number of queries
  int queriesTotal;
  cin >> queriesTotal; discardNewLine();

  // read queries
  int switches = 0;
  int currentQueryEngine;
  freeAllEngines();
  while ( queriesTotal-- > 0 ) {
    cin.getline( buffer, MAX_ENGINE_NAME + 1 );
    currentQueryEngine = getEngineNumber( buffer );

    if ( engineFree[ currentQueryEngine ] ) {
      engineFree[ currentQueryEngine ] = false;
      --freeEnginesCount;

      if ( 0 == freeEnginesCount ) {
        ++switches;

        freeAllEngines();
        engineFree[ currentQueryEngine ] = false;
        --freeEnginesCount;
      }
    }
  }

  return switches;
}

int main () {
  // read number of cases
  int casesTotal, caseNumber = 1;
  cin >> casesTotal; discardNewLine();
  while ( caseNumber <= casesTotal ) {
    cout
      << "Case #" << caseNumber++ << ": "
      << countSwitchesOfCurrentCase() << endl;
  }
}


