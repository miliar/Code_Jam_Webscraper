//---------------------------------------------------------------------------

#pragma hdrstop

//---------------------------------------------------------------------------

#pragma argsused
#include <iostream>
#include <fstream>

using namespace std;

int croos(int i, int j) {
}

int IsLinesCross(int x11, int y11, int x12, int y12, int x21, int y21, int x22, int y22)
{
	double x,y;
	// знаменатель
	double Z  = (y12-y11)*(x21-x22)-(y21-y22)*(x12-x11);
	// числитель 1
	double Ca = (y12-y11)*(x21-x11)-(y21-y11)*(x12-x11);
	// числитель 2
	double Cb = (y21-y11)*(x21-x22)-(y21-y22)*(x21-x11);
	// если числители и знаменатель = 0, прямые совпадают
	if( (Z == 0)&&(Ca == 0)&&(Cb == 0) )
	{



	}
	// если знаменатель = 0, прямые параллельны
	if( Z == 0 )
	{

		return 0;
	}
	double Ua = Ca/Z;
	double Ub = Cb/Z;
	x = x11 + (x12 - x11) * Ub;
	y = y11 + (y12 - y11) * Ub;
	// если 0<=Ua<=1 и 0<=Ub<=1, точка пересечения в пределах отрезков
	if( (0 <= Ua)&&(Ua <= 1)&&(0 <= Ub)&&(Ub <= 1) )
	{
		//cout << fixed << setprecision(10)  << (double)x << endl << (double)y << endl;

		return 1;
	}
	// иначе точка пересечения за пределами отрезков
	else
	{

		return 0;
	}

		return 0;
}
int main()
{
	long l,n,count,a[100],b[100];

	//ree.find()
	ifstream in("A.in");
	ofstream out("A.out");
	in >> l;
	for (long p=0;p<l;p++)
	{
		count = 0;
		in >> n;
		for (int i=0;i<n;i++)
			in >> a[i] >> b[i];

		for (int i=0;i<n-1;i++)
			for (int j=i+1;j<n;j++)
				if (IsLinesCross(1,a[i],2,b[i],1,a[j],2,b[j])) count++;

		out << "Case #" << p+1 << ": " << count;

		
		out << endl ;
	}



	return 0;
}
//---------------------------------------------------------------------------
