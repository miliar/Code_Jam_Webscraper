#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;

bool cycles[2000001];
int modDiv[10000000];
int nextNumber[10000000];

char buf[20];

int main(int argc, char** argv)
{
    modDiv[0] = 0;
    for(int i = 1; i < 10; ++i)
        modDiv[i] = 1;
    for(int i = 10; i < 10000000; ++i)
        modDiv[i] = 10*modDiv[i/10];
    
    for(int i = 1; i < 10000000; ++i)
    {
        sprintf(buf, "%d", i);
        
        int zeroPos = 1;
        int lim = strlen(buf);
        
        if(lim > 1 && buf[1] == '0')
            while(zeroPos < lim && buf[zeroPos] == '0')
                ++zeroPos;
        else
            zeroPos = 0;
        
        int mult = 10;
        int divVal = modDiv[i];
        
        if(zeroPos == lim)
        {
            nextNumber[i] = i;
        }
        else
        {   
            for(int j = 0; j < zeroPos - 1; ++j)
            {
                mult *= 10;
                divVal /= 10;
            }
            
            int leadingNumber = i/divVal;
            int next = (i % divVal)*mult + leadingNumber;
            nextNumber[i] = next;
        }
    }
    
    int T;
    scanf("%d", &T);
    
    fprintf(stderr, "Preprocessing done\n");
    
    for(int t = 1; t <= T; ++t)
    {
        int A, B;
        scanf("%d %d", &A, &B);
        
        fill(cycles + A, cycles + B + 1, false);
        long long answer = 0;
        
        for(int i = A; i <= B; ++i)
        {
            if(cycles[i])
                continue;
            
            int c = i;
            int numInCycle = 0;
            
            do
            {
                cycles[c] = true;
                int next = nextNumber[c];
                if(A <= next && next <= B)
                    ++numInCycle;
                c = next;
                
                
            }
            while(c != i);
            
            long long pairs = numInCycle;
            answer += pairs*(pairs - 1)/2;
        }
        
        printf("Case #%d: %lld\n", t, answer);
    }
    
    return 0;
}