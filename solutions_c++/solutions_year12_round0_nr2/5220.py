#include<cstdio>

int numbers[104];

int main()
{

    int t;
    int n;
    int surprises;
    int p;
    int cases = 0;
    scanf("%d",&t);
    int cs = 1;
    while(t--)
    {
        cases  = 0;
        scanf("%d %d %d",&n,&surprises, &p);

        for(int i = 0; i < n ; i++ )
        {
            scanf("%d",&numbers[i]);
        }

        for(int i = 0; i < n; i++)
        {
            int score = numbers[i];
            int base = score/3;

            switch(score%3)
            {
                case 0:
                {
                    // base base base or base-1 base base+1
                    //regular case
                    if(base >=p)
                    {
                        cases++;
                    }
                    else if(surprises > 0 && base > 0 && base+1 >= p)
                    {
                        cases++;
                        surprises--;
                    }

                    break;
                }

                case 1:
                {
                    //base base base+1
                    //base-1 base+1 base + 1

                    if(base + 1 >= p or base>= p) cases++;

                    else
                    {
                        if(surprises >0 and base+1 >= p)
                        {
                            cases++;
                            surprises--;
                        }
                    }

                    break;
                }

                case 2:
                {
                    //base base base + 2
                    // base base+1 base + 1

                    if(base + 1 >= p or base >= p) cases++;
                    else
                    {
                        if(surprises > 0 and base+2 >= p)
                        {
                            cases++;
                            surprises--;
                        }
                    }

                    break;
                }
            }

        }

        printf("Case #%d: %d\n",cs++,cases);




    }

    return 0;
}
