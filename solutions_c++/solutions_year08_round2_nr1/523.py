#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>
#include <math.h>


#define abs(x) ((x) >= 0 ? (x) : -(x))
#define bit_clear (a, b) ((a) & ~((uunsigned longeger)1 << (b)))
#define bit_set (a, b) ((a) | ((uunsigned longeger)1 << (b)))
#define bit_test (a, b) ((a) >> (b) & 1)

#define max (a, b) ((a) >= (b) ? (a) : (b))
#define min (a, b) ((a) <= (b) ? (a) : (b))

using namespace std;

 int main(unsigned long argc, char *argv[])
{
	unsigned long lines;
	std::cin >> lines;
	unsigned long long datax[100001];
	unsigned long long datay[100001];
	for (unsigned long m=0;m<lines;m++) {
		unsigned long n, A, B, C, D, x0, y0, M;
		std::cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M ;
		datax[0]=x0;		
		datay[0]=y0;
		unsigned long res=0;
		for (unsigned long i=1; i<n; i++) {
			datax[i]=(A*datax[i-1]+B) % M;
			datay[i]=(C*datay[i-1]+D) % M;
//			prunsigned longf("%d %d\n",datax[i],datay[i]);
			}
		for (unsigned long i=0; i<n; i++) 
			for (unsigned long j=i+1; j<n; j++) 
				for (unsigned long k=j+1; k<n; k++) 		
				if ((datax[i]+datax[j]+datax[k]) % 3 ==0)
					if ((datay[i]+datay[j]+datay[k]) % 3 ==0)
				res++;
				printf("Case #%d: %d\n",m+1,res);
	}
	return 0;
}
