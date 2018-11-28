#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <cmath>

using namespace std; 

class Point
{
public:
	Point():x(0.0),y(0.0),z(0.0){}

	double x;
	double y;
	double z;

	void div(int n)
	{
		x /= n;
		y /= n;
		z /= n;
	}
};

inline double distance( const Point &a)
{
	return sqrt(pow(a.x,(int)2) + pow(a.y,(int)2) + pow(a.z,(int)2));
}



int main()
{
	fstream infile("B-large.in");
	ofstream outfile("Result.txt");


	int t,testCase(1);
	infile >> t;

	for(;testCase <= t ; testCase ++)
	{
		int flyCount(0);
		infile >> flyCount;
		Point center,speed;
		for(int i = 0 ; i < flyCount ; i ++)
		{
			int p1,p2,p3;
			infile >> p1 >> p2 >> p3;
			center.x += p1;
			center.y += p2;
			center.z += p3;

			infile >> p1 >> p2 >> p3;
			speed.x += p1;
			speed.y += p2;
			speed.z += p3;
		}

		center.div(flyCount);
		speed.div(flyCount);

		
		outfile.precision(8);
		outfile.setf(ios::fixed); 

		if(abs(center.x) < 0.00001 && abs(center.y) < 0.00001 && abs(center.z) < 0.00001)
		{
			outfile << "Case #" << testCase  << ": 0.00000000 0.00000000" << endl;
			continue;
		}

		if(abs(speed.x) < 0.00001 && abs(speed.y) < 0.00001 && abs(speed.z) < 0.00001)
		{
			outfile << "Case #" << testCase  << ": " << distance(center)<< " 0.00000000" << endl;
			continue;
		}

		double nearestTime = ( 0 - center.x * speed.x -center.y * speed.y -center.z * speed.z )/(speed.x * speed.x + speed.y * speed.y + speed.z * speed.z);

		if(nearestTime < 0)
		{
			outfile << "Case #" << testCase  << ": " << distance(center)<< " 0.00000000" << endl;
		}

		else
		{
			center.x += speed.x * nearestTime;
			center.y += speed.y * nearestTime;
			center.z += speed.z * nearestTime;
			outfile << "Case #" << testCase  << ": " << distance(center)<< " " << nearestTime << endl;
		}

	}

	return 0;
}