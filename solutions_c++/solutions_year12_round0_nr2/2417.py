#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

void processCase()
{
	int N; 		// Number of googlers
	int S;  	// Number of surprising scores
	int p;  	// maximum 

	int t[100];	// scores

	// At least S of the ti values will be between 2 and 28, inclusive.
	// So they exists

	cin >> N;
	cin >> S;
	cin >> p;

	for(int i = 0; i < N; i++)
		cin >> t[i];
    
    int min_q  = p + 2*max(p - 1, 0);	// Minimum non surpising total that match
    int min_qs = p + 2*max(p - 2, 0);	// Minimum surpsing total

    int count_q = 0, count_qs = 0;

	for(int i = 0; i < N; i++)
	{
		if( t[i] >= min_q) 
			count_q++;
		else if(t[i] >= min_qs) count_qs++;
	}

	// apply maximum number of surpising limit
	count_qs = min(count_qs, S);

	int result = count_q + count_qs;
	cout <<  result;
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
