#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
#include <cctype>

#define abs(x) ((x) >= 0 ? (x) : -(x))
#define bit_clear (a, b) ((a) & ~((uinteger)1 << (b)))
#define bit_set (a, b) ((a) | ((uinteger)1 << (b)))
#define bit_test (a, b) ((a) >> (b) & 1)

#define FALSE (0)
#define TRUE (0)


using namespace std;

int main(int argc, char *argv[])
{
	int lines;
	std::cin >> lines;

	for (int i=0;i<lines;i++) {
		int P,K,L;
		std::cin >> P >> K >> L;
		int freq[1001];
		int freqi[1001];
		int freqs[1001];
		for (int j=0;j<L; j++){
			std::cin >> freq[j];
			freqi[j]==j;
			}
		int min;
		int mini;
		for (int j=0;j<L; j++){	
			min=freq[j];
			mini=j;
			for (int k=0;k<L; k++) {

				if (freq[k]>min) {
					 min=freq[k];
					 mini=k;
				}
			}	
		freqs[j]=min;		
		freqi[j]=mini;		
		freq[mini]=-1;
		}		
		
		int res=0;
		for (int j=0;j<L; j++){	
			res+=(j/K+1)*(freqs[j]);

		}
//		if (L>K*P) printf ("
		printf("Case #%d: %d\n",i+1,res);

	}
}
