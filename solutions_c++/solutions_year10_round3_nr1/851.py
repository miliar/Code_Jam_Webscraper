#include <iostream>
#include <string>
#include <cmath>
#include <fstream>
#include <algorithm>

using namespace std;

#define cin fin
#define cout fout

int h[1000][2];

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("b.out");
	int casenum,n;
	cin>>casenum;

	for(int c=0; c<casenum; c++)
	{
		cin>>n;
		for(int i=0; i<n; i++)
			cin>>h[i][0]>>h[i][1];
		int node=0;
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
			{
				if((h[i][0]-h[j][0])*(h[i][1]-h[j][1])<0)
					node++;
			}
		cout<<"Case #"<<c+1<<": "<<node/2<<endl;
	}
}
