#include <iostream>
#include <fstream>

using namespace std;

int ascendent(const void *long1, const void *long2)
{
	long v1 = *(long *)long1;
	long v2 = *(long *)long2;

	return v1 - v2;
}

int descendent(const void *long1, const void *long2)
{
	long v1 = *(long *)long1;
	long v2 = *(long *)long2;

	return v2 - v1;
}

void solve(long index, istream& is, ostream& os)
{
	long i, dimensions = 0, sum = 0;
	long *vector1 = NULL, *vector2 = NULL;

	is >> dimensions;
	vector1 = new long[dimensions];
	vector2 = new long[dimensions];
	for(i = 0;i < dimensions;++i)
		is >> vector1[i];
	for(i = 0;i < dimensions;++i)
		is >> vector2[i];
	qsort(vector1, dimensions, sizeof(long), &ascendent);
	qsort(vector2, dimensions, sizeof(long), &descendent);
	for(i = 0;i < dimensions;++i)
		sum += vector1[i] * vector2[i];
	os << "Case #" << index << ": " << sum << endl;
	delete [] vector1;
	delete [] vector2;
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
