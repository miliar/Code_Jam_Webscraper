#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct S
{
	double s[6];
	void clear()
	{
		for(int i = 0; i < 6; i++)
			s[i] = 0;
	}
	S()
	{
		for(int i = 0; i < 6; i++)
			s[i] = 0;
	}
};

vector <S> arr;
S b, e;

struct Vector
{
	double x, y, z;
	void Get(S s1, S s2)
	{
		x = s2.s[0] - s1.s[0];
		y = s2.s[1] - s1.s[1];
		z = s2.s[2] - s1.s[2];
	}
};

double VectMul(Vector v1, Vector v2)
{
	double x = v1.y*v2.z-v1.z*v2.y;
	double y = v1.z*v2.x-v1.x*v2.z;
	double z = v1.x*v2.y-v1.y*v2.x;
	return sqrt(x*x+y*y+z*z);
}

double Dist(S a, S b)
{
	return sqrt((a.s[0]-b.s[0])*(a.s[0]-b.s[0]) + (a.s[1]-b.s[1])*(a.s[1]-b.s[1]) + (a.s[2]-b.s[2])*(a.s[2]-b.s[2]));
}

double Scalar(Vector a, Vector b)
{
	return a.x * b.x + a.y * b.y + a.z * b.z;
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		int n;
		cin >> n;
		arr.clear();
		arr.resize(n);
		for(int j = 0; j < n; j++)
			for(int k = 0; k < 6; k++)
				cin >> arr[j].s[k];
		b.clear();
		for(int j = 0; j < n; j++)
			for(int k = 0; k < 3; k++)
				b.s[k] += arr[j].s[k];
		for(int j = 0; j < 3; j++)
			b.s[j] /= n;
		e.clear();
		for(int j = 0; j < n; j++)
			for(int k = 0; k < 3; k++)
				e.s[k] += arr[j].s[k] + arr[j].s[k + 3];
		for(int j = 0; j < 3; j++)
			e.s[j] /= n;
		Vector x, y;
		x.Get(b, e);
		y.Get(b, S());
		double c = Scalar(x, y);
		if(c <= 0)
		{
			printf("Case #%d: %.6lf %.6lf\n", i + 1, Dist(b, S()), 0);
			continue;
		}
		double dist = VectMul(x, y);
		dist /= Dist(e, b);
		c /= Dist(e, b);
		c /= Dist(e, b);
		printf("Case #%d: %.6lf %.6lf\n", i + 1, dist, c);
	}
	return 0;
}