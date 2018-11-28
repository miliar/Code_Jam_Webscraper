#include <iostream.h>

#define DEBUG

struct time24
{
	int h, m;
	char hh_mm[6];
	bool arrDep;	// set to true for arrival times
	// methods
	void convertToInteger()
	{
		h = ( hh_mm[0] - '0' ) * 10 + ( hh_mm[1] - '0' );
		m = ( hh_mm[3] - '0' ) * 10 + ( hh_mm[4] - '0' );
	}
	void addMinutes( int mins ) // works well subject to a maximum of 60 minutes
	{
		if( ( m + mins ) >= 60 )
			h++;
		if( h == 24 )
			h = 0;
		m = ( m + mins ) % 60;
	}
	// compares if time is before rhs time. if times are equal but one of them is arr and the other dep, arr is considered to be earlier
	bool isBefore( time24 rhs )
	{
		if( ( h < rhs.h ) || ( h == rhs.h && m < rhs.m ) )
			return true;
		if( ( h > rhs.h ) || ( h == rhs.h && m > rhs.m ) )
			return false;
		if( arrDep )	// check this case?!?
			return true;
		return false;
	}
};

// the last parameter is the return value
int getNumStartingTrains( time24 arrTimes[], int numArr, time24 depTimes[], int numDep, int turnaroundTime )
{
	time24 arrDepTimes[200], temp;
	int i, j;
	int numTrains = 0;
	int maxReq = 0;

#ifdef DEBUG
	cout << "Arrival Times" << endl;
	for( i = 0; i < numArr; i++ )
		cout << arrTimes[i].hh_mm << endl;
	cout << "Departure Times" << endl;
	for( i = 0; i < numDep; i++ )
		cout << depTimes[i].hh_mm << endl;
#endif

	for( i = 0; i < numArr; i++ )
	{
		arrTimes[i].convertToInteger();
		// do we have to consider trains arriving previous day and "turning around" the next day in the equation??
		// currently this is the case
		arrTimes[i].addMinutes( turnaroundTime );
		arrDepTimes[i] = arrTimes[i];
		arrDepTimes[i].arrDep = true;
	}
	for( i = 0; i < numDep; i++ )
	{
		depTimes[i].convertToInteger();
		arrDepTimes[numArr + i] = depTimes[i];
		arrDepTimes[numArr + i].arrDep = false;
	}

#ifdef DEBUG
	cout << "Arrival Times" << endl;
	for( i = 0; i < numArr; i++ )
		cout << arrTimes[i].h << " " << arrTimes[i].m << endl;
	cout << "Departure Times" << endl;
	for( i = 0; i < numDep; i++ )
		cout << depTimes[i].h << " " << depTimes[i].m << endl;
#endif

	// sort the values - make sure to put an arriving train b4 a departing one (or) simply do a stable sort on h, m values
	for( i = 0; i < ( numArr + numDep ) - 1; i++ )
		for( j = i + 1; j < ( numArr + numDep ); j++ )
		{
			if( arrDepTimes[j].isBefore( arrDepTimes[i] ) )
			{
				temp = arrDepTimes[i];
				arrDepTimes[i] = arrDepTimes[j];
				arrDepTimes[j] = temp;
			}
		}

#ifdef DEBUG
	cout << "Sorted arrival(+T)/departure values" << endl;
	for( i = 0; i < ( numArr + numDep ); i++ )
		cout << arrDepTimes[i].hh_mm << endl;
#endif

	// find out num starting trains
	for( i = 0; i < ( numArr + numDep ); i++ )
	{
		if( arrDepTimes[i].arrDep ) // wow! a train that's arrived and raring to go - what a dumb thing to be excited about :D
			numTrains--;
		else
		{
			numTrains++;
			if( numTrains > maxReq )
				maxReq = numTrains;
		}
	}

	return maxReq;
}

int main( int argc, char *argv[] )
{
	FILE *fpIn, *fpOut;
	int numTestCases, caseNum = 1;
	int turnaroundTime, na, nb, a, b, i;
	char strTime[12];

	time24 arr_A[100], dep_A[100], arr_B[100], dep_B[100];

	if( ( fpIn = fopen( argv[1], "r" ) ) == 0 )
	{
		cout << "Problem opening input file" << endl;
		return 1;
	}

	if( ( fpOut = fopen( argv[2], "w" ) ) == 0 )
	{
		cout << "Problem opening output file" << endl;
		return 1;
	}

	fscanf( fpIn, "%d", &numTestCases );

#ifdef DEBUG
	cout << "Num Test Cases : " << numTestCases << endl;
#endif

	while( caseNum <= numTestCases )
	{
		fscanf( fpIn, "%d%d%d", &turnaroundTime, &na, &nb );
		for( i = 0; i < na; i++ )
		{
			fgets( strTime, 12, fpIn ); // skip over newline?!?
			fgets( strTime, 12, fpIn );
			strncpy( dep_A[i].hh_mm, strTime, 5 );
			dep_A[i].hh_mm[5] = '\0';
			strncpy( arr_B[i].hh_mm, strTime + 6, 5 );
			arr_B[i].hh_mm[5] = '\0';
		}
		for( i = 0; i < nb; i++ )
		{
			fgets( strTime, 12, fpIn ); // skip over newline?!?
			fgets( strTime, 12, fpIn );
			strncpy( dep_B[i].hh_mm, strTime, 5 );
			dep_B[i].hh_mm[5] = '\0';
			strncpy( arr_A[i].hh_mm, strTime + 6, 5 );
			arr_A[i].hh_mm[5] = '\0';
		}

#ifdef DEBUG
		cout << na << " trains departing from A : " << endl;
		for( i = 0; i < na; i++ )
			cout << dep_A[i].hh_mm << endl;
		cout << nb << " trains departing from B : " << endl;
		for( i = 0; i < nb; i++ )
			cout << dep_B[i].hh_mm << endl;
		cout << nb << " trains arriving at A : " << endl;
		for( i = 0; i < nb; i++ )
			cout << arr_A[i].hh_mm << endl;
		cout << na << " trains arriving at B : " << endl;
		for( i = 0; i < na; i++ )
			cout << arr_B[i].hh_mm << endl;
#endif

		a = getNumStartingTrains( arr_A, nb, dep_A, na, turnaroundTime );
		b = getNumStartingTrains( arr_B, na, dep_B, nb, turnaroundTime );

#ifdef DEBUG
		printf( "Case #%d: %d %d\n", caseNum, a, b );
#endif
		fprintf( fpOut, "Case #%d: %d %d\n", caseNum, a, b );

		caseNum++;
	}
}
