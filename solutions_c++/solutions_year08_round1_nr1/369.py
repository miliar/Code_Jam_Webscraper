#include<vector>
#include<string>
#include<iostream>
#include<sstream>
#include<algorithm>
#include<math.h>
#include<complex>
#include <fstream>

using namespace std;

void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,x,c,nn;
	vector<int> v1,v2;
	ff>>c;
	for(nn=0;nn<c;nn++)
	{
		v1.clear();v2.clear();
		ff>>n;
		for(i=0;i<n;i++) {ff>>x;v1.push_back(x);}
		for(i=0;i<n;i++) {ff>>x;v2.push_back(x);}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		x=0;
		for(i=0;i<n;i++) x+=v1[i]*v2[n-i-1];
		re <<"Case #"<<nn+1<<": "<< x<<endl;
	}
}
