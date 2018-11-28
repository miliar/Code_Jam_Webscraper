#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;


template <typename  Container>
void readArray(Container& C, int numberOfEntries)
{
	for(int i = 0; i < numberOfEntries; i++)
	{
	    typename Container::value_type value;
		cin >> value;
		C.push_back(value);
	}
}

void processCase()
{
	vector<float> P;

	int A, B;

	cin >> A;
	cin >> B;

	readArray(P, A);


	int L = B - A;

	float r = 1.0;

	for(int i = 0; i < P.size(); i++)
	   r *= P[i];
	

	float case1 = r*( L + 1) + (1 - r) * (L + 1 + B + 1);
	float case2 = B + 2;

	float c;
	float c_min = min(case1, case2);


	for( int i = 0; i < A; i++)
	{
		float r = 1;

		for( int j = 0; j < A - i; j++)
			r *= P[j];

	    c =  (1 - r) * ( 2 * i + L + 1 + B + 1 )  + r * ( 2*i + L + 1);


	    c_min = min(c, c_min);
	}


	printf("%.6f", c_min);
	
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
			processCase();
		printf("\n");
	}
	
    return 0;
}
