#include <fstream>

/*
Google Code Jam 2001 

gopher@geomys.com


solved using MSVC++ Express 2008

add to empty console project to compile

*/

using namespace std;

#define BASENAME "A-large"


int IsPossible(__int64 N, int Pd, int Pg)
{
	//quick exclusion of some edge cases
	//if we've won ANY today, we MUST'VE won some all-time
	if (Pd>0 && Pg==0)
		return false;

	//if we've never lost a game, we can't have lost one today
	if (Pg==100)
		return Pd==100;

	//if we won none today, then anything's possible, except that we've never lost.
	if (Pd==0)
		return Pg<100;

	//if we lost none today, " " ", except that we've never won
	if (Pd==100)
		return Pg>0;

	//ok, it can't possibly be a whole number unless the number of games played has some 
	//common factor with 100.
	//factors of 100, which are the same as the factors of 10...
	int primeFactorsOf100[] = { 2, 5, };

	//our N must be evenly divisible by one of those values or it's just not possible 
	//(except in the 0/100 cases tested above)
	
	for (int i=2; i<=N; ++i)
	{
		//check divisibility by 2 and 5
		if (i&0x1!=0 && i%5!=0)
			//neither, can't be me
			continue;
		
		/* This was a wild goose chase, I think...
		double base=1.0;
		if ((i&0x1)==0)
		{
			if ((i&0x2)==0)
				base*=4;
			else
				base*=2;
		}
		
		if (i%5==0)
		{
			if (i%25==0)
				base*=25;
			else
				base*=5;
		}

		if (base==1)
			continue; //it's not this one, move along
		*/

		double tempD=Pd*i/100.0;
		//we found it. Success!
		if (((int)tempD)==tempD)
			return true; 
		
	}

	return false;
}


int main(int argc, char* argv[])
{
	
	
	ifstream inFile(BASENAME ".in");
	ofstream outFile(BASENAME ".out");

	int numCases;
	inFile>>numCases;


		
	for (int caseNum=1; caseNum<=numCases; ++caseNum)
	{
		
		__int64 N;
		int Pd, Pg;
		inFile>>N>>Pd>>Pg;
		
		
		bool possible=IsPossible(N,Pd,Pg);
		
		
		
		outFile<<"Case #"<<caseNum<<": "<<(possible?"Possible":"Broken")<<endl;
	}

	/*comment terminator*/

	return 0;
}