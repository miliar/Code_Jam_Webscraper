#include <cstring>
#include <cstdio>
#include <map>

using namespace std;

const int MaxN = 100;
const int MaxChar = 26;
int list[MaxN];


int combine[MaxChar];
int oposite[MaxChar];
map<int, int> combinations;

inline int toInt(char c)
{
    return c - 'A';
}

inline char toChar(int i)
{
    return i + 'A';
}

void printSolution( int testCase, int solutionLength)
{
    printf("Case #%d: [", testCase);

    if(solutionLength > 0)
        printf("%c", toChar(list[0]));

    for(int i = 1; i < solutionLength; i++)
        printf(", %c", toChar(list[i]));

    printf("]\n");
}

int invoke(char invocations[], int elements)
{
    int listLenght = 0;
    char* offset = invocations;
    int insertedElements = 0;
    int intValue;
    int elementCount[MaxChar];
    memset(elementCount, 0, sizeof(elementCount));

    map<int, int>::iterator value;

    for(int index =0; index < elements; index++)
    {
        intValue = toInt(*offset);
        if(listLenght)
        {
            //check combine
            if( combine[intValue] & (1<<list[listLenght-1]) )
            {
                value = combinations.find( 1<<intValue | (1<<list[listLenght-1]));

                // release previouselement
                elementCount[list[listLenght-1]]--;
                if(!elementCount[list[listLenght-1]])
                {
                    insertedElements = 0;
                    for(int i = 0; i < MaxChar; i++)
                        if(elementCount[i])
                            insertedElements |= 1 << i;
                }

                // add combined element
                insertedElements |= 1<<(value->second);
                list[listLenght-1] = value->second;
            }
            else // Check opposed
            {
                if( oposite[intValue] & insertedElements)
                {
                    // clean up the list
                    insertedElements = 0;
                    listLenght = 0;
                    memset(elementCount, 0, sizeof(elementCount));
                }
                else // insert element
                {
                    insertedElements |= 1 << intValue;
                    elementCount[intValue]++;
                    list[listLenght++] = intValue;
                }

            }
        }
        else
        {
            insertedElements = 1 << intValue;
            list[listLenght++] = intValue;
            elementCount[intValue]++;
        }
        *offset++;
    }

    return listLenght;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
#endif
    int index = 1;
    int T;

    int N;
    int C;
    int D;

    char invocations[MaxN+1];

    scanf("%d", &T);
    while(T--)
    {
        // clear data structures
        combinations.clear();
        memset(combine, 0, sizeof(combine));
        memset(oposite, 0, sizeof(oposite));

        // Read Data
        // read combinations
        scanf("%d", &C);
        while(C--)
        {
            scanf("%s",  invocations);

            int a = toInt(invocations[0]);
            int b = toInt(invocations[1]);
            int c = toInt(invocations[2]);

            combine[a] |= 1<< b;
            combine[b] |= 1<< a;
            int key = 1<<a | 1<<b;
            combinations.insert(pair<int,char>(key, c));
        }

        // read oposites
        scanf("%d", &D);
        while(D--)
        {
            scanf("%s", invocations);
            int a = toInt(invocations[0]);
            int b = toInt(invocations[1]);
            oposite[a] |= 1<<b;
            oposite[b] |= 1<<a;
        }

        scanf("%d %s", &N, invocations);

        printSolution(index++, invoke(invocations, N));
    }

    return 0;
}
