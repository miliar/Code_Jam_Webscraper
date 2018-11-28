#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int max_usual[50];
int max_surprise[50];

int tests;
int n;
int s;
int p;
int total;

int always;
int if_s;

int ans;
int main()
{
    for(int i = 0; i < 31; i++)
        max_usual[i] = max_surprise[i] = 0;
    for(int i = 0; i < 11; i++)
        for(int j = 0; j < 11; j++)
            for(int k = 0; k < 11; k++)
            {
                int best = max(i,max(j,k));
                int total = i+k+j;
                //usual
                if ((abs(i-j) < 2)&&(abs(i-k) < 2)&&(abs(j-k) < 2))
                {
                    if (best > max_usual[total])
                        max_usual[total] = best;
                }                
                //surprise
                if ((abs(i-j) <= 2)&&(abs(i-k) <= 2)&&(abs(j-k) <= 2))
                {
                    if ((abs(i-j) == 2)||(abs(i-k) == 2)||(abs(j-k) == 2))
                    {
                        if (best > max_surprise[total])
                            max_surprise[total] = best;
                    }
                }
            }
    freopen("input.txt","r",stdin);    
    freopen("output.txt","w",stdout);    
    scanf("%d\n",&tests);
    for(int t = 0; t < tests; t++)
    {
        scanf("%d%d%d",&n,&s,&p);
        always = 0;
        if_s = 0;
        for(int i = 0; i < n; i++)
        {
            scanf("%d",&total);
			if ((total == 30)||(total == 29))
			{
				always++;
			}
			else
			{
				if ((total == 1)&&(p <= 1))
				{
					always++;
				}
				else
				{
					if (max_surprise[total] >= p)
					{
						if(max_usual[total] >= p)
							always++;                
						else
							if_s++;                
					}
				}
			}
        }
        ans = always+min(s,if_s);
        printf("Case #%d: %d\n", (t+1), ans);
    }
    return(0);
}

