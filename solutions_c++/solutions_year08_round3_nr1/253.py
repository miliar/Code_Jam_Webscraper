#include<fstream>
#include<iostream>
#include<algorithm>
using namespace std;

int t[10000];
int main()
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int tests,p,k,l,x,x1;
	long long w;
	bool b;
	in>>tests;
	for(int c = 0; c < tests; c++)
	{
		in>>p>>k>>l; b = false; w = 0;
		for(int c = 0; c < l; c++)
			in>>t[c];
		sort(t,t+l);
		x = 0; x1 = 0;
		for(int c = l; c > 0; c--)
		{
			if(x1 == 0)
				x++;
			if(x > p)
			{
				b = 1;
				break;
			}
			x1++; x1%=k;
			w+= t[c-1]*x;
		}
		out <<"Case #"<<c+1<<": "<< w<< '\n';
	}
	in.close();
	out.close();
	return 0;
}