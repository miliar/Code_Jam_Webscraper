#include <iostream>
#include <cassert>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;

//1 0 5 1

int main()
{
	int n,i,j;
	vector <int> v1;
	string x;
	v1.push_back(0);
	v1.push_back(5);
	v1.push_back(1);
	v1.push_back(1);

	fstream file_op("inp.in",ios::in);
 	ofstream myfile;
  	myfile.open ("out.txt");

        file_op>>n; 
        
	for(i=0;i<n;i++)
	{
		file_op>>x;
		v1.resize(0);
		v1.push_back(0);
		for(j=0;j<x.size();j++)
		{
			v1.push_back(x[j]-'0');
		}

		next_permutation(v1.begin(), v1.end());
	  	
		myfile<<"Case #"<<i+1<<": ";
		for(j=0;j<v1.size();j++)
		{
			if(j==0 && v1[j]==0) continue;
			myfile<<v1[j];
		}
		myfile<<endl;
	}
	file_op.close();
	myfile.close();

	return 0;
}
