#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef long long type;


class Solver
{
	vector<type> X_Coord;
	vector<type> Y_Coord;

	type n,A,B,C,D,x0,y0,M;
public:

	Solver (type _n,type _A,type _B,type _C,type _D,type _x0,type _y0,type _M) : 
		n (_n),A(_A),B(_B),C(_C),D(_D),x0(_x0),y0(_y0),M(_M) {}

	void fullVec ();
	bool checkVec (int x1,int x2,int x3);
	int solve ();
};

void Solver::fullVec ()
{
	type X,Y;
	X = x0;
	Y = y0;
	X_Coord.push_back(X);
	Y_Coord.push_back(Y);
	for (int i=1;i < n;i++)
	{
		X = (A*X+B)%M;
		Y = (C*Y+D)%M;
		X_Coord.push_back(X);
		Y_Coord.push_back(Y);
	}
}

bool Solver::checkVec (int x1,int x2,int x3)
{
//	cout << "Check:" << X_Coord[x1] << " " << Y_Coord[x1] << endl;
//	cout << X_Coord[x2]<< " " << Y_Coord[x2] << endl;
//	cout << X_Coord[x3] << " " << Y_Coord[x3] << endl;
	if ((X_Coord[x1]+X_Coord[x2]+X_Coord[x3])%3 == 0 && (Y_Coord[x1]+Y_Coord[x2]+Y_Coord[x3])%3 == 0)
	{
//		cout << "Ret true!!\n";
		return true;
	}
//	cout << "Ret False!!\n";
	return false;
}

int Solver::solve ()
{
	int counter = 0;
	int controlli = 0;
	for (int i=0;i < n;i++)
	{
		for (int a=i+1;a < n;a++)
		{
			for (int b=a+1;b< n;b++)
			{
				if (checkVec (i,a,b) == true)
					counter++;
				controlli++;
			}
		}
	}
	//cout <<"controlli: " <<  controlli << endl;

	return counter;
}

int main (int argc,char * argv[])
{
	ifstream infile (argv[1]);

	int ncount = 0;
	infile >> ncount;

	for (int i=0;i < ncount;i++)
	{
		type n,A,B,C,D,x0,y0,M;
		infile >> n;
		infile >> A;
		infile >> B;
		infile >> C;
		infile >> D;
		infile >> x0;
		infile >> y0;
		infile >> M;
		Solver c1 (n,A,B,C,D,x0,y0,M);
		c1.fullVec ();
		cout << "Case #" << i+1 << ": " << c1.solve () << endl;

	}
	
//	Solver puppa1 (4,10,7,1,2,0,1,20);
//	Solver puppa2 (6,2,0,2,1,1,2,11);
//	puppa1.fullVec ();
//	puppa2.fullVec ();
//	cout << "Vivo1\n";
//	cout << puppa1.solve () << endl;
	return 0;
}
