#include <iostream>
#include <fstream>
#include <cmath>
#include <functional>
#include <vector>
#include <cstring>

using namespace std;



int main()
{
	ifstream fin ("D-small-attempt0.in");
	ofstream fout ("test.out");

	int i,j;
	
	int n,cases;
	
	fin>>n;
	
	int k;
	vector<int> t;
	char s[2000],ss[2000];
	int res;
	for(cases = 1; cases <= n; cases++)
	{
		t.clear();
		fin>>k;
		for(i=0;i<k;i++)
			t.push_back( i);
		fin>>s;
		int len = strlen(s);
		res = 100000;
		do
		{			
			for(i=0;i<len;i++)
			{
				
				ss[i] = s[ i/k*k +t[ i%k] ];
			}
			//cout<<ss<<endl;
			char c ='A';
			int re=0;
			for(i=0;i<len;i++)
				if(c!=ss[i])
			{
				c = ss[i];
				re++;
			}
			if(res>re)
				res = re;
			//cout<<re<<endl;
			//cout << endl ;
		}while ( next_permutation(t.begin(), t.end() ) );

		
		fout<<"Case #"<<cases<<": "<< res <<endl;
	}

}