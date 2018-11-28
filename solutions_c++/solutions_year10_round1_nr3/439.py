// ag.cpp : Defines the entry point for the console application.
//

#include <fstream>
using namespace std;
int t,a1,a2,b1,b2;
long long int g;
int ng (int a,int b)
{
	int f=0;
	int x=0;
	if (a<b) swap(a,b);
	if (a==b) return 0;
	else
	{
		if (b==0) return 1;
		else 
		{
			if (a/b>1) x=a/b-1;
			else x=1;
			for (int i=x;i<=a/b;i++)
			{
				if (ng(a-i*b,b)==0) f=1;
			}
		}
		return f;
	}
}
int main()
{
	ifstream in("C-small-attempt1.in");
	ofstream out("output.txt");
	in >> t;
	for (int i=0;i<t;i++)
	{
		in >> a1 >> a2 >> b1 >> b2;
		g=0;
		for (int j=a1;j<=a2;j++) for (int k=b1;k<=b2;k++)
		{
			g=g+ng(j,k);
		}
		out << "Case #" << i+1 << ": " << g << '\n';
	}
	return 0;
}

