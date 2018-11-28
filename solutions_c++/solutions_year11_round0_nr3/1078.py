#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
	int T,N;
	ifstream in("input.txt");
	ofstream out("output.txt");		
	in>>T;
	for(int k=0; k<T; k++)
	{
		in>>N;
		vector<int> c(N);
		for(int i=0; i<N; i++)
			in>>c[i];
		bool flag=true;
		int s=0;
		sort(c.begin(),c.end());
		for(int i=0; (flag)&&(i<N-1); i++)
		{
			int c1=c[0], c2=c[i+1];
			for(int j=1; j<=i; j++)
				c1^=c[j];
			for(int j=i+2; j<N; j++)
				c2^=c[j];
			if (c1==c2)
			{
				for(int j=i+1; j<N; j++)
					s+=c[j];
				flag=false;
			}
		}
		if (flag) out<<"Case #"<<(k+1)<<": NO"<<endl;
		else out<<"Case #"<<(k+1)<<": "<<s<<endl;
	}
	return 0;
}



