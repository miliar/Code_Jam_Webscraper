#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

int freq[10];
int required_freq[10];

long long next_integer(long long N)
{
    memset(required_freq, 0, sizeof required_freq);

    long long decimal = N;
    while(decimal != 0) {
		int algarismo = decimal % 10;
		decimal = decimal / 10;
		required_freq[algarismo]++;
	}

    for(long long i = N + 9; ; i += 9) {
        memset(freq, 0, sizeof freq);

        decimal = i;
        while(decimal != 0) {
    		int algarismo = decimal % 10;
		    decimal = decimal / 10;
	    	if (algarismo != 0 && ++freq[algarismo] > required_freq[algarismo])
                goto next_iteration;
    	}
        for(int j = 1; j <= 9; j++) {
            if (required_freq[j] != freq[j])
                goto next_iteration;
        }
        return i;

        next_iteration:
            continue;
    }
}

int main()
{
    int T;
    scanf("%d", &T);
    for(int caso = 1; caso <= T; caso++) {
        long long N;
        scanf("%lld", &N);
        printf("Case #%d: %lld\n", caso, next_integer(N));
    }
    return 0;
}

