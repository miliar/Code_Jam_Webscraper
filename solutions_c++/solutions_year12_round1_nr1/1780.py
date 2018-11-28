#include <cstdio>

#define LEN 5
double p[LEN];

double cp[10];

//calculate 2^i
int ca(int i)
{
    int j;
    int ret = 1;
    for(j=0;j<i;j++)
        ret *= 2;
    return ret;
}

int cal(int n)
{
    int ret = 0;
    int i;
    for(i=0;i<n;++i)
        ret += ca(i);
    return ret;
}
int main()
{
    int T, A, B;
    FILE *fin = fopen("A-small-attempt0.in", "r");
    FILE *fout = fopen("A-small-attempt0.out", "w");
    fscanf(fin,"%d", &T);
    int i;
    for(i=1;i<=T;++i)
    {
        fscanf(fin,"%d%d", &A, &B);
        int j;
        for(j=0;j<A;++j)
            fscanf(fin, "%lf", &p[j]);

        int cases = ca(A);

        for(j=0;j<cases;++j)
        {
            //计算每一种情况的概率
            int k;
            int a = j;
            double prob = 1.0;
            for(k=0;k<A;++k)
            {
                if((a&1) == 1)
                    prob *= p[A-1-k];
                else
                    prob *= (1-p[A-1-k]);
                a >>= 1;
            }

            cp[j] = prob;
            //printf("cp[%d]=%lf\n", j, prob);
        }

        //先计算keep typing
        int m = cal(A);
        double e0 = 0.0;
        double a1 = cp[m] * (B-A+1);
        e0 += a1;
        double a2 = (1-cp[m])*(B-A+1+B+1);
        e0 += a2;

        //printf("e0 is: %lf\n", e0);

        //calculate enter anyway
        double en = 1 + B + 1;

        //printf("en is: %lf\n", en);

        double mine = 1 + B + 1;
        //calculate from 1 to A
        for(j=1;j<=A;++j)
        {
            double expect = 0.0;

            int k;
            for(k=0;k<cases;++k)
            {
                //高A-j位是否都为1
                int q = k;
                int p = j;
                while(p>0)
                {
                    q>>=1;
                    p--;
                }
                int c = cal(A-j);
                //printf("c is %d\n", c);
                if(q == c)
                {
                    double t1 = cp[k] * (j + j + B - A + 1);
                    expect += t1;

                    //printf("t1 is %lf \n", t1);
                }
                else
                {
                    double t2 = cp[k] * (j + j + B - A + 1 + B + 1);
                    expect += t2;
                    //printf("q is :%d", q);
                    //printf("t2 is %lf \n", t2);
                }
            }
            //printf("e%d is: %lf\n", j, expect);
            if(expect <= mine)
            {
                mine = expect;
            }
        }

        if(mine >= en)
            mine = en;
        if(mine >= e0)
            mine = e0;

        fprintf(fout, "Case #%d: %.6lf\n", i, mine);
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
