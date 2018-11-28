#include<iostream>
#include<fstream>
#include<vector>
#include<set>
#include<string>
#include<map>
#include<valarray>
#include<iterator>
#include<algorithm>
using namespace std;
int main()
{
	ifstream gin("A-small-attempt3.in");
	ofstream gout("gypAsmall.out");
	int T;
	long long int A,B;
	gin>>T;
	for(int i=0;i<T;i++)
	{
		gin>>A>>B;
		vector<long double> probs;
		for(int j=0;j<A;j++)
		{
			long double temp;gin>>temp;
			probs.push_back(temp);
		}
		long double graphpr[101];
		for(int j=0;j<=A;j++)
		{
			graphpr[j]=1;
			for(int k=0;k<A-j;k++)graphpr[j]*=probs[k];
		}
		long double min=1000;
		for(int j=0;j<=A;j++)
		{
			double ex=(B-A+1+2*j)*graphpr[j]+(2*B-A+2+2*j)*(1-graphpr[j]);
			if(ex<min)min=ex;
		}
		if(min>B+2)min=B+2;
		gout.precision(6);
		gout.setf(ios::fixed,ios::floatfield);
		gout<<"Case #"<<i+1<<": "<<min<<endl;
	}
	gin.close();
	gout.close();
	return 0;
}
