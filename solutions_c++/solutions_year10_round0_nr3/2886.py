// Google CodeJam 2010 Entry
// By Steven Duda (duda69@gmail.com)
// C++ Source code; compile using gcc 4.2.2 -O2;

#include <iostream>
#include <fstream>
using namespace std;

struct skip
{
	long totalCount;
	long skip;
};

skip* skipTab;

void buildSkipTab(ifstream& ifs, long long k, long N)
{
	//delete if it already exists
	if(skipTab != NULL)
        delete[] skipTab;
	
	//allocate and read in data
	skipTab = new skip[N];
	long* group = new long[N];
	for(long i=0; i<N; ++i)
		ifs >> group[i];

	long skip, count, pos = 0, next;
	//build the table
	for(long i=0; i<N; ++i)
	{
		skip = 0, count = 0, pos = i;
		next = group[pos];
		do{
			count += next;
			pos = (pos+1) % N;	
			next = group[pos];
		} while(++skip < N && (count + next) <= k);
	
		skipTab[i].totalCount = count;
		skipTab[i].skip = skip;	
	}
	delete [] group;
}

int main(int argc, char* argv[])
{
	long T, N;
	long long R, k, euro, pos;
    
    ofstream output("output.txt");
	ifstream ifs("C-small-attempt0.in");
	ifs >> T;

	for(long i=0; i<T; ++i)
	{
		euro = 0;
		pos = 0;
		
		ifs >> R >> k >> N;
		buildSkipTab(ifs, k, N); // Calculate Skip Pattern
		
		for(long j=0; j<R; ++j)
		{
			euro += skipTab[pos].totalCount;
			pos = ((pos + skipTab[pos].skip) % N);
		}	
		
		output << "Case #" << (i+1) << ": " << euro << endl;	
	}
    
	ifs.close();
    output.close();

	return (0);	
}

