#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <algorithm>
#include <math.h>

using namespace std;

//const char* INPUT_FILE_NAME  = "D-large.in";
//const char* OUTPUT_FILE_NAME = "D-large.out";
const char* INPUT_FILE_NAME  = "D-small-attempt0.in";
const char* OUTPUT_FILE_NAME = "D-small-attempt0.out";
//const char* INPUT_FILE_NAME  = "D-small.in";
//const char* OUTPUT_FILE_NAME = "D-small.out";

struct PLANT
{
	int x;
	int y;
	int radius;
};

float GetRadius( const PLANT& plant1, const PLANT& plant2 )
{
	int xDiff = plant1.x - plant2.x;
	int yDiff = plant1.y - plant2.y;
	float distBetweenPlants = sqrtf( xDiff*xDiff + yDiff*yDiff );
	return (plant1.radius + distBetweenPlants + plant2.radius) * 0.5f;
}

float GetOutput( fstream& inputFileStream )
{
	int N;

	inputFileStream >> N;

	PLANT plant[3];

	for( int i = 0 ; i < N ; ++i )
	{
		inputFileStream >> plant[ i ].x >> plant[ i ].y >> plant[ i ].radius;
	}

	if( N == 1 )
		return plant[ 0 ].radius;
	else if( N == 2 )
	{
		return plant[ 0 ].radius > plant[ 1 ].radius ? plant[ 0 ].radius : plant[ 1 ].radius;
	}
	else // 3
	{
		float minRadius = 10000000000.f;
		for( int j = 0 ; j < 3 ; ++j )
		{
			float singleRadius = plant[ j ].radius;
			float radiusOfTwo = GetRadius( plant[ (j+1)%3 ], plant[ (j+2)%3 ] );

			float maxRad = singleRadius > radiusOfTwo ? singleRadius : radiusOfTwo;

			if( maxRad < minRadius )
				minRadius = maxRad;
		}
		return minRadius;
	}

	return 0;
}
int main()
{
	int C;
	string strOutput;
	string strInput;

	fstream inputFileStream(INPUT_FILE_NAME, ios_base::in);
	fstream outputFileStream(OUTPUT_FILE_NAME, ios_base::out|ios_base::trunc);
	outputFileStream.setf(ios_base::floatfield, ios_base::fixed);
	outputFileStream.precision(7);
	cout.setf(ios_base::floatfield, ios_base::fixed);
	cout.precision(7);

	inputFileStream >> C;

	char buffer[8192];
	inputFileStream.getline(buffer, 8192);

	for( int i = 0; i < C; ++i )
	{
		float count = GetOutput( inputFileStream );

		outputFileStream << "Case #" << i+1 << ": " << count << endl;
		cout << "Case #" << i+1 << ": " << count << endl;
	}

	inputFileStream.close();
	outputFileStream.flush();
	outputFileStream.close();

	return 0;
}
