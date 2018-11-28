#include<stdio.h>
#include<string.h>
#include<stdlib.h>

#define L 16
#define D 5001

int l, d, n;
char dict[D][L];
char check[D*D+1];

int docheck()
{
    int i,j, k;
    int sum=0;

    // check for all words in dict
    for(i=0; i<d; i++)
    {
        bool res=true;
        for(j=0, k=0; j<l; j++)
        {
            // get char j
            char tocheck=dict[i][j];

            if(check[k]=='(')
            {
                // start of range
                bool contains=false;
                for(k=k+1; check[k]!=')'; k++)
                {
                    if(tocheck==check[k])
                        contains=true;
                }

                if(!contains)
                    res=false;
                ++k;
            }
            else
            {
                // normal char so match
                if(tocheck!=check[k])
                    res=false;
                ++k;
            }

            if(!res)
                break;
        }

        if(res)
        {
            ++sum;
        }
    }

    return sum;
}

int main()
{
    int i;

    scanf("%d%d%d%d", &l, &d, &n);

    for(i=0; i<d; i++)
    {
        scanf("%s", dict[i]);
    }

    for(i=0; i<n; i++)
    {
        scanf("%s", check);
        printf("Case #%d: %d\n", i+1, docheck());
    }

    return 0;
}
