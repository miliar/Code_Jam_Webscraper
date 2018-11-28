#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <iomanip>
#include <cmath>


using namespace std;
typedef long long int64;

inline int64 SQR(const int64& x)
	{ return x*x;}


int main (int argc, char * const argv[]) {
	
	fstream INP("input.txt",fstream::in);
	fstream OUT("output.txt",fstream::out);
	
	int T;
	
	INP>>T;
	
	for(int corr=0;corr<T;corr++)
	{
	int N;
	INP>>N;
	
	string S;
	vector<int> our(N,0);
	
	for(int i=0;i<N;i++)
		{
		INP>>S;
		for(int j=S.size()-1;j>=0;j--)
			if(S[j]=='1')
				{
				our[i]=j;
				break;
				}
		}
	int conta=0;
	
	for(int find=0;find<N;find++)
		{
		
		bool buono=1;
		
		for(int j=0;j<N;j++)
			buono and_eq (our[j]<=j);
		
		if(buono)
			goto here;
		
		if(our[find]<=find)
			continue;
			
		int dove=0;
		for(int j=0;j<N;j++)
			if(our[j]<=find and j>find)
				{
				dove=j;
				break;
				}
				
		for(int j=dove;j>find;j--)
			{
			swap(our[j],our[j-1]);
			conta++;
			}
			
		}
	here:
	
	
	
	OUT<<"Case #"<<corr+1<<": "<<conta<<endl;
	}
	
	
	
    return 0;
}
