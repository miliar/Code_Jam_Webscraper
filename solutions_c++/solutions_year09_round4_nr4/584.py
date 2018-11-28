#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;

int C,n;
int X[3],Y[3],R[3];

inline double d(int x1, int y1, int x2, int y2)
{
	return sqrt((double)((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)));
}

int main()
{
    fstream fin("D.in",ifstream::in);
    fstream fout("D.out",ofstream::out);
    fin >> C;
    for(int j=1;j<=C;j++)
    {	
        double R1,R2,R3;
		fin >> n;
		rep(i,n) fin >> X[i] >> Y[i] >> R[i];
		if (n==1) fout << "Case #" << j << ": " << (double)(R[0]) << "\n";
		else if (n==2) fout << "Case #" << j << ": " << (double)(max(R[0],R[1])) << "\n";
		else {
			R1 = max ( 0.5*(d(X[0],Y[0],X[1],Y[1])+R[0]+R[1]),(double)(R[2]));
			R2 = max ( 0.5*(d(X[1],Y[1],X[2],Y[2])+R[1]+R[2]),(double)(R[0]));
			R3 = max ( 0.5*(d(X[0],Y[0],X[2],Y[2])+R[0]+R[2]),(double)(R[1]));
			R1 = min(R1,R2);
			R1 = min(R1,R3);
			fout << "Case #" << j << ": " << R1 << "\n";
		}
    }
    fin.close();
    fout.close();
    cout << "running time=" << clock()/(double)CLOCKS_PER_SEC;
    system("PAUSE");
    return 0;
}
