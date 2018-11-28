#include <iostream>
#include <algorithm>
#include <fstream>

using namespace std;

	int m[2000];

int Calc(int a, int b)
{
	int ret=1;
	for(int i=a; i<b; i++)
		m[i]--;
	int mid=(a+b)/2;
	if(*max_element(m+a,m+mid)>0)
		ret+=Calc(a,mid);
	if(*max_element(m+mid,m+b)>0)
		ret+=Calc(mid,b);
	return ret;
}

void main()
{
	ifstream ifs("B-small-attempt0.in");
	ofstream ofs("B-small-attempt0.out");


	int t,p;
	int ii,i,j;
	ifs>>t;
	for(ii=0; ii<t; ii++)
	{
		ifs>>p;
		int nn=1<<p;
		for(i=0; i<nn; i++)
		{
			ifs>>m[i];
			m[i]=p-m[i];
		}

		int a;
		for(i=0; i<nn-1; i++)
			ifs>>a;

		int ret=0;
		if(*max_element(m+0,m+nn)>0)
			ret=Calc(0,nn);

		ofs<<"Case #"<<ii+1<<": "<<ret<<endl;
	}
}
