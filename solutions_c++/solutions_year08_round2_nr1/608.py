#include<iostream>
#include<sstream>
#include<fstream>
#include<math.h>
#include<iomanip>
#include<list>
#include<vector>
#include<map>

using namespace std;

typedef long long int64;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;

#define LARGE 1000000
#define PI 3.14159265358979323846

struct Coor{
    int x;
int y;
};

bool sortStruct (Coor first, Coor second)
{
	if (first.x < second.x)
		return true;
	if (first.x == second.x && first.y < second.y)
		return true;
	return false;
}

int main(int argc, char *argv[])
{
	
	int nCase;
	cin >> nCase;

	for (int numCases = 0; numCases < nCase; numCases++)
	{
		int n, A, B, C, D, x0, y0, M;
		cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

// 		list<Coor> _myList;
// 		Coor* CC =  new Coor[n];
// CC[0].x = x0;
// CC[0].y = y0;
// 
// _myList.push_back(CC[0]);

int ** points = new int * [n];
for (int i = 0; i<n; i++)
points[i] = new int[2];

		double X,Y;
points[0][0] = x0;
points[0][1] = y0;
X = x0;
Y = y0;
		for (int i = 1; i<n; i++)
		{
			X = fmod((A * X + B),M);
  			Y = fmod((C * Y + D),M);
			//cout << X << " " << Y << endl;
points[i][0]= X;
points[i][1] = Y;
//_myList.push_back(CC[i]);
  		}
//_myList.sort(sortStruct);


// list<Coor>::iterator iter1;
// int d=0;
// for (iter1 = _myList.begin(); iter1 != _myList.end(); ++iter1)
// {
// points[d][0] = (*iter1).x;
// points[d][1] = (*iter1).y;
// d++;
// }

int nCenter = 0;
		for (int i = 0; i<n-2; i++)
		{
//			cout << points[i][0] << " " << points[i][1] << endl;
			for (int j = i+1; j<n-1; j++)
			{
				for (int k = j+1; k<n; k++)
				{
					double cx  = (points[i][0] + points[j][0] +points[k][0]) / 3.0; 
					double cy  = (points[i][1] + points[j][1] +points[k][1]) / 3.0; 
					if (floor(cy) == cy && floor(cx) == cx ) nCenter++;
//					cout << cx << " " << floor(cy) << endl;
				}
			}
		}
//		cout << nCenter << endl;
		for (int i = 1; i<n; i++)
			delete points[i];
		delete points;
		cout << "Case #" << numCases+1 << ": " << nCenter << endl;
	}
	return 0;
}

