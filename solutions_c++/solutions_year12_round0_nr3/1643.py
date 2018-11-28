#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <algorithm>

using namespace std;

static const long power10[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int numdigits(long num)
{
	if(num==0)
		return 1;
	int ret=0;
	while( num ) { num/=10; ret++; }
	return ret;
};

bool shiftnum(long& m, int numd)
{
	short lowest = m%10;
	m/=10;
	m+=lowest*power10[numd-1];
	return (lowest!=0);
};

unsigned long computeRecycled(long A, long B)
{
	unsigned long pairs = 0;
	int numd = 0;
	long m = -1;
	int valid = 0;
	for(long n = A; n <= B; n++)
	{
		numd = numdigits(n);
		m = n;
		do {
			valid = shiftnum(m, numd);
			if ( valid && (m > n) && (m<=B) )
				pairs++;
		} while( m != n );
	}
	return pairs;
};

int main() {
	ifstream is("C-large.in");
	ofstream os("C-large.out");
	if(!is)
		return -1;
	int N = 0; is >> N;
	long A,B;
	for(int cnt=1; cnt<=N; cnt++)
	{
		is >> A; is >> B;
		cout << "Case #" << cnt << ": " << computeRecycled(A, B) << endl;
		os << "Case #" << cnt << ": " <<  computeRecycled(A, B) << endl;
	}
	is.close();
	os.close();
}

