#include <cstdlib>
#include <iostream>

using namespace std;

//Number of snaps needed can be precalculated
//Only up to thirty, easy to store
//num_snaps = 0
//num_snaps[i] = 2^i - 1
int num_snaps[31] = {0,   
1,
3,
7,
15,
31,
63,
127,
255,
511,
1023,
2047,
4095,
8191,
16383,
32767,
65535,
131071,
262143,
524287,
1048575,
2097151,
4194303,
8388607,
16777215,
33554431,
67108863,
134217727,
268435455,
536870911,
1073741823};

int main()
{
    
    freopen("A-large.in", "r", stdin);
    freopen("Solution.txt", "w", stdout);
    
    
    int num_testcases;
    scanf("%d ", &num_testcases);
    
    //Precalculation: Closded formula: 2^n -1
    /*
    int num_snaps[31];
    //Only one snap needed
    num_snaps[1] = 1;
    
    for(int i = 2; i <= 30; i++)
    {
            //I need num_snaps[i-1] snaps to give power to the i-th snap
            // Then I turn this one on (and all others off --> + 1
            //After that, I again need num_snaps[i-1] to turn the first [i-1] snaps on.
            //Equals 1+ 2 * num_snaps[i-1]
            num_snaps[i] = 1 + 2 * num_snaps[i - 1]; 
    }
    
    printf("{");
    
    for(int i = 1; i <= 30; i++)
    {
            //Formatted for precalc
            printf("%d,\n", num_snaps[i]);
    }
    
    printf("}"); */
    
    int N; //number of snappers in the chain
    int K; //number of snaps made
    
    for(int i = 1; i <= num_testcases; i++)
    {
            
            scanf("%d %d ", &N, &K);        
            //Calculate whether correct
            
            //One Snap needed to turn all snaps off again
            //while(snaps_left > num_snaps[N]) snaps_left = snaps_left - num_snaps[N] - 1;
            
            //Equals the while statement abover
            int snaps_left = K % (num_snaps[N] + 1);
            
            //Remaining snaps bring current to the lightbulb
            if(snaps_left == num_snaps[N]) printf("Case #%d: ON\n", i);
            //In this case not
            else printf("Case #%d: OFF\n", i);
    }
    
    //Did it=)
    return 0;
}
