#include <fstream>
using namespace std;
ifstream fin("a-small.in");
ofstream fout("a-small.out");
bool proverka(long A1, long B1, long A2, long B2)
{
	if(A1<A2 && B1>B2)
		return true;
	if(A1>A2 && B1<B2)
		return true;
	return false;
}
int main()
{
	long T, i, e, j, R;
	fin>>T;
	for(i=0;i<T;++i)
	{
		R = 0;
		long N;
		fin>>N;
		long* A = new long[N];
		long* B = new long[N];
		for(e = 0;e<N;++e)
			fin>>A[e]>>B[e];
		for(e=0;e<N-1;++e)
			for(j=e+1;j<N;++j)
				if(proverka(A[e], B[e], A[j], B[j]))
					R++;
		delete[] A;
		delete[] B;
		fout<<"Case #"<<i+1<<": "<<R<<endl;
	}
	return 0;
}