#include<iostream>
#include<fstream>
#include<queue>
using namespace std;

int main (int argc, char * const argv[]) {
	ifstream myfile;
	myfile.open(argv[1]);
	
	long long T,R, k, N;
	myfile >> T;

	for(int counter=0; counter<T; counter++)
	{
		myfile >> R >> k >> N;
		
		queue<long long> rc;
		for(int i=0; i<N; i++)
		{
			long long tmp;
			myfile >> tmp;
			rc.push(tmp);
		}
		
		long long euro = 0;
		
		for(int i=0; i<R; i++)
		{
			
			long long space=0;
			int inside=0;
			
			while(space+rc.front() <= k && inside<N)
			{
				inside++;
				rc.push(rc.front());
				space += rc.front();
				rc.pop();
			}
			euro += space;
			
			
		}
		
		cout << "Case #" << counter+1 << ": " << euro << endl;
		while(!rc.empty())
			rc.pop();
		
	}
	
	
	return 0;
}
	