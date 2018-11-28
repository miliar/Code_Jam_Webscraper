#include <cstdio>
#include <map>
using namespace std;

#define NUM_MAX 505
typedef map<int,int>::iterator MapInterator;

void Solve(int iCase)
{    
    int nNumbers;
    int numbers[NUM_MAX];
    map<int, int> m;
    pair<MapInterator, bool> p;

    scanf("%d", &nNumbers);

    for(int i = 0; i<nNumbers; i++)
    {
        scanf("%d", numbers + i);
    }
    int num = 1 << nNumbers;
    for(int i = 0; i < num; i++)
    {
        int sum = 0;
        for(int j = 0; j < nNumbers;j++)
        {
            if((1 << j) & i) sum += numbers[j];
        }
        p = m.insert(make_pair(sum, i));
        if(!p.second)
        {
            int t = m[sum];            
            bool set1[NUM_MAX], set2[NUM_MAX];
            memset(set1, false, sizeof(set1));
            memset(set2, false, sizeof(set2));

            int j;
            for(j = 0; j < nNumbers; j++)
            {
                int k = 1 << j;
                set1[j] = k & i;
                set2[j] = k & t;
            }

            printf("Case #%d:\n", iCase);

            for( j = 0; j < nNumbers; j++)
            {
                if(set1[j])
                {
                    printf("%d ", numbers[j]);
                }
            }
            printf("\n");

            for(j=0; j < nNumbers; j++)
            {
                if(set2[j] && !set1[j])
                {
                    printf("%d ", numbers[j]);
                }
            }
            printf("\n");
            break;
        }
    }
}

int main()
{
    freopen("C-small-attempt1.in","r", stdin);
    freopen("C-small-attempt1.out","w", stdout);
    int nCase;
    scanf("%d", &nCase);
    for(int iCase = 1; iCase <= nCase; iCase++)
    {
        Solve(iCase);
    }
    return 0;
}