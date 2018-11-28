#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

long numPlayers;
int lowest;
int highest;
int* freqs;
int lowestPossible;

bool processing() 
{

    lowestPossible = 0;
    for(int j = lowest; j <= highest; j++)
    {
        int possible = 0;
        for(long i = 0; i < numPlayers; i++)
        {
            if(j == freqs[i])
            {
                possible = 1;
            }
            else if(j > freqs[i])
            {
                possible = ((j%freqs[i])==0) ? 1 : 0;
            }
            else if(j < freqs[i])
            {
                possible = ((freqs[i]%j)==0) ? 1 : 0;
            }
            if(possible == 0) break;
            if(i == (numPlayers-1) && possible == 1) {
                lowestPossible = j;
                return true;
            }    
        }
        if(j == highest && possible == 0) return false;
    }
    
    return true;
    
}

int main ()
{
	int T, TC = 1;

    for(scanf("%d", &T); TC <= T; TC++)
    {
        scanf("%ld %d %d", &numPlayers, &lowest, &highest);
        freqs = new int[numPlayers];
        for(int i = 0; i < numPlayers; i++) 
        {
            scanf("%d", &freqs[i]);
        }
        if(processing()) {
            printf("Case #%d: %d\n", TC, lowestPossible);   
        } else {
            printf("Case #%d: NO\n", TC);   
        }
    }

    return 0;
}
