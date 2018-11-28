#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <utility>
#include <map>
#include <set>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <functional>
#include <algorithm>

//#define  INFILE  "A-small.in"
//#define OUTFILE  "A-small.out"

#define  INFILE  "A-small-attempt0.in"
#define OUTFILE  "A-small-attempt0.out"

//#define  INFILE  "A-large.in"
//#define OUTFILE  "A-large.out"


#define print0(A) T::fprint0(#A,A)
#define print1(A) T::fprint1(#A, A.begin(),A.end())
#define Print2(A) T::fPrint2(#A,A)

using namespace std;

class T
{
	public:
		template<typename T> static void fprint0(const string name, const T value)
		{
			cout << name<<": " <<value<<endl;
		}
		
		template<typename iter> static void fprint1(const string name,iter beg,iter end)
		{
			cout<<name<<": ";	
			for(iter it=beg;it!=end;++it)
			{
				cout<<(it==beg ? "":" ")<<*it;
			}
			cout<<endl;
		}		
		
		template<typename T> static void 
		fprint2(const string name, const vector<vector<T> > v)
		{
			cout<<name<<":"<<endl;
			for(int i=0;i<v.size();++i)
			{
				for(int j=0;j<v[i].size();++j)
				{
					cout<<v[i][j]<<(j==v[i].size()-1 ? "\n":" ");
				}
			}		
		}		
};







int main()
{
	ifstream fin(INFILE);
	ofstream fout(OUTFILE);
	if(!fin)cout << "can't open input file!"<<endl;
	if(!fout)cout<< "can't creat output file!"<<endl;
{
	int T;
	fin>>T;
	for(int i=1;i<=T;++i)
	{
		int n;
		fin>>n;
		vector<long> x(n);
		vector<long> y(n);
		for(int j=0;j<n;++j)
		{
			fin >> x[j];
		}
		for(int j=0;j<n;++j)
		{
			fin >> y[j];
		}
		sort(x.begin(),x.end());
		sort(y.rbegin(),y.rend());
		
		long sum=0;
		for(int j=0;j<n;++j)
		{
			sum+=x[j]*y[j];
		}
		fout<<"Case #"<<i<<": "<<sum<<endl;
			
	}


	
		

	
}	
	fin.close();
	fout.close();
	system("pause");
	
	return 0;
}
