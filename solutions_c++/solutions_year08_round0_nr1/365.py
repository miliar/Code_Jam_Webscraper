#include <iostream>
#include <fstream>

using namespace std;

typedef char searchengine[110];

void solve(long index, istream& is, ostream& os)
{
	long i, j, ecount = 0, qcount = 0;
	searchengine *engines = NULL, *queries = NULL;
	long *equal = NULL;

	is >> ecount;
	engines = new searchengine[ecount];
	equal = new long[ecount];
	for(i = 0;i < ecount;++i)
	{
		is.getline(engines[i], 110);
		equal[i] = -1;
		if(strlen(engines[i]) == 0)
			--i;
	}
	is >> qcount;
	queries = new searchengine[qcount];
	for(j = 0;j < qcount;++j)
	{
		is.getline(queries[j], 110);
		if(strlen(queries[j]) == 0)
			--j;
	}

	long currentserver = -1;
	long currentquery = 0;
	long shift = 0;

	while(true)
	{
		for(i = 0;i < ecount;++i)
		{
			if(i == currentserver)
				continue;
			equal[i] = -1;
			for(j = currentquery;j < qcount;++j)
			{
				if(strcmp(engines[i], queries[j]) == 0)
				{
					equal[i] = j;
					break;
				}
			}
		}

		long candidate;
		long biggest = -1;

		for(i = 0;i < ecount;++i)
		{
			if(i == currentserver)
				continue;
			if(equal[i] == -1)
			{
				biggest = -1;
				break;
			}
			if(equal[i] > biggest)
			{
				biggest = equal[i];
				candidate = i;
			}
		}
		if(biggest == -1)
			break;
		++shift;
		currentserver = candidate;
		currentquery = biggest + 1;
	}
	delete [] engines;
	delete [] equal;
	delete [] queries;
	os << "Case #" << index << ": " << shift << endl;
}

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cerr << "Usage: " << argv[0] << " inputfile outputfile" << endl;
		return 0;
	}

	filebuf ib, ob;

	if(ib.open(argv[1], ios::in) && ob.open(argv[2], ios::out))
	{
		long i, count = 0;
		istream is(&ib);
		ostream os(&ob);

		is >> count;
		for(i = 0;i < count;++i)
			solve(i + 1, is, os);
		return 0;
	}
	return 1;
}
