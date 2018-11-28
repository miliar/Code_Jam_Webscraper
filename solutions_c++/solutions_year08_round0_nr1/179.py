#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <sstream>
#include <cmath>
#include <iostream>
#include <cstdlib>

//#define  INFILE  "A-small-attempt0.in"
//#define OUTFILE  "A-small-attempt0.out"

#define  INFILE  "A-large.in"
#define OUTFILE  "A-large.out"

using namespace std;

int main()
{
	ifstream fin(INFILE);
	ofstream fout(OUTFILE);
	if(!fin)cout << "can't open input file!"<<endl;
	if(!fout)cout<< "can't creat output file!"<<endl;
{
	int N;
	fin>>N;
	for(int i=1;i<=N;++i)
	{
		int S,Q;
		fin>>S;	
		
		string line;
		getline(fin,line);
		
		vector<string> se(S);
		for(int j=0;j<S;++j)
		{
			getline(fin,line);
			se[j]=line;
		}
		
		fin>>Q;
		getline(fin,line);
		
		vector<string> query(Q);
		for(int j=0;j<Q;++j)
		{
			getline(fin,line);
			query[j]=line;
		}			
		
		set<string> ss;
		int cnt=0;
		
		for(int j=0;j<Q;++j)
		{
			ss.insert(query[j]);
			if(ss.size()==se.size())
			{
				++cnt;
				ss.clear();
				ss.insert(query[j]);
			}
		}
		
		fout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	
}	
	fin.close();
	fout.close();
	system("pause");
	
	return 0;
}
