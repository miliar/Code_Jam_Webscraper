#include <fstream>
#include <math.h>
using namespace std;

struct checked
{
	int x,y;
};
checked c[1000];
int filled = 0;
bool isChecked(int a, int b)
{
	for(int i = 0; i < filled; i++)
	{
		if((c[i].x == a && c[i].y == b)|| 
			(c[i].y == a && c[i].x == b))
		{
			return true;
		}
	}
	return false;
}
void makeChecked(int a, int b)
{
	c[filled].x = a;
	c[filled].y = b;
	filled++;
}
void recycleNfill(int x, int la, int lb,int n)
{
	int h = x;
	int n2 = n;
	int dig ;
	for(int i = 0; i < n - 1; i++)
	{
		
		x = h;
		for(int j = 0; j <= i; j++)
		{
			dig = x%10;
			x = x/10;
			dig = dig * (int)pow((float)10,(int)n-1);
			x = dig + x;
		}
		if(x < la || x > lb || h == x)
		{
			continue;
		}
		if(!isChecked(h,x))
			makeChecked(h,x);	
	}
}
int main()
{
	int t,a,b,n,tempa;
	ifstream ifile("small.in");
	ofstream ofile("output");
	ifile.seekg(0,ios::beg);
	ofile.seekp(0,ios::beg);
	ifile>>t;
	for(int i = 0; i < t ; i++)
	{
		ifile>>a;
		ifile>>b;
		filled = 0;
		tempa = a;
		n = 0;
		while(tempa > 0)
		{
			tempa /= 10;
			n++;
		}
		for(int j = a; j <= b; j++)
		{
			recycleNfill(j,a,b,n);
		}
		ofile<<"Case #"<<i+1<<": "<<filled<<endl;
	}
	ifile.close();

	ofile.close();
}
