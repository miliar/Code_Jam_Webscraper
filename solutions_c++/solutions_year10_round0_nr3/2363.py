#include<iostream>
#include<fstream>
#include<cstring>
#include<queue>
using namespace std;

#define xin fin
#define xout fout
#define f(i,a,b) for (i=a;i<=b;i++)
#define MAXINT 1000000000 //10^9

class bigNum
{
public:
	int a0,a1;
	bigNum();
	void add(int n);
	void output();
	void clear();
};
ifstream fin("c.in");
ofstream fout("c.out");
int main()
{
	
	register int i,z;
	int sum,c,r,k,n,p,b;
	int q[1002];
	bigNum ss;
	xin >> c;
	f(z,1,c)
	{
		xin >> r >> k >> n;
		f(i,0,n-1)
		{
			xin >> q[i];
		}
		p = 0;
		sum = 0;
		ss.clear();
		b = 0;
		f(i,1,r)
		{
			sum += q[p];
			p++;
			p %= n;
			while ((k - sum >= q[p]) && (p != b))
			{
				sum += q[p];
				p++;
				p %= n;
			}
			ss.add(sum);
			sum = 0;
			b = p;
		}
		xout << "Case #" << z << ": ";
		ss.output();
		xout << endl;
	}
	return 0;
}
bigNum::bigNum()
{
	clear();
}
void bigNum::clear()
{
	a0 = 0;
	a1 = 0;
}
void bigNum::add(int n)
{
	a0 += n;
	a1 += a0 / MAXINT;
	a0 %= MAXINT;
}
void bigNum::output()
{
	if (a1 > 0)
	{
		xout << a1;
		int t = (MAXINT / 10);
		while(a0 < t)
		{
			xout << 0;
			t /= 10;
		}
		if (a0 != 0)
			xout << a0;
	}
	else
	{
		xout << a0;
	}
}