#include<cstdio>
#include<vector>

#define FILE_IN "A-large.in"
#define FILE_OUT "out.txt"

using namespace std;

struct Pair
{
    int head;
    int tail;
};


int main(void)
{
    FILE *in = fopen(FILE_IN, "r");
    FILE *out = fopen(FILE_OUT, "w");
    int cases;
    fscanf(in,"%d", &cases);
    for(int i = 1; i <= cases; i++)
    {
        int nPairs;
        fscanf(in, "%d", &nPairs);
        vector<Pair> pairs;
        pairs.reserve(nPairs);
        int intersects = 0;
        for(int j = 0; j < nPairs; j++)
        {
            Pair newPair;
            fscanf(in,"%d %d", &newPair.head, &newPair.tail);
            for(int k = 0; k < j; k++)
            {
                if(pairs[k].head < newPair.head)
                {
                    if(pairs[k].tail > newPair.tail)
                        intersects++;
                }
                else
                    if(pairs[k].tail < newPair.tail)
                        intersects++;
            }
            pairs.push_back(newPair);
        }
        fprintf(out, "Case #%d: %d\n", i, intersects);
    }
    fclose(in);
    fclose(out);
}