#include <cstdlib>
#include <cstdio>

using namespace std;

int data[1000];
int dataCount = 0;
int maxValue;
int maxsumSean;


void check(int index, int sumSean, int sumPP, int sumPS)
{
    //we give this item to someone..
    if (index < dataCount)
    {
        //if sean get this
        check(index+1, sumSean+data[index], sumPP, sumPS^(data[index]));
        //if patric get this
        check(index+1, sumSean, sumPP^(data[index]), sumPS);
    } else {
        //we at end lets compare
        if ((sumPP == sumPS) && (sumSean>maxsumSean) && (sumPP != 0))
        {
            maxValue = sumPP;
            maxsumSean = sumSean;
        }
    }
}

int main()
{
    int i;
    scanf("%d", &i);
    for(int j=1; j<=i; ++j)
    {
        maxValue = 0;
        maxsumSean = 0;
        scanf("%d", &dataCount);
        for(int g=0;g<dataCount;++g)
        {
            scanf("%d", &data[g]);
        }
        check(0, 0, 0, 0);
        if (maxsumSean == 0)
            printf("Case #%d: NO\n", j);
        else
            printf("Case #%d: %d\n", j, maxsumSean);
    }

    return 0;
}

