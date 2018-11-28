#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>

using namespace std;

void correct (int *a, int *b, int *c, int ti)
{
    int cr = ti - *a- *b- *c;

    while (cr>0)
    {
        if (cr>0)
        {
            *a=*a+1;
            cr--;
        }
        if (cr>0)
        {
            *b=*b+1;
            cr--;
        }
        if (cr>0)
        {
            *c=*c+1;
            cr--;
        }
    }
}

bool hasP (int a, int b, int c, int p)
{
    if (a>=p)
    {
        return true;
    }

    if (b>=p)
    {
        return true;
    }
    if (c>=p)
    {
        return true;
    }

    return false;
}

void correctWithSuprise (int *a, int *b, int *c, int p, int *s)
{
    int m,n,l;
    m = *a;
    n = *b;
    l = *c;

    m--;
    if (m>=0)
    {
        n++;
        if (abs(m-n)<2 && abs (m-l)<2)
        {
            if (n>=p)
            {
                *a=*a-1;
                *b=*b+1;
                return;
            }
        }
        else if (abs(m-n)==2 || abs (m-l)==2)
        {
             if (n>=p)
            {
                *a=*a-1;
                *b=*b+1;
                *s=*s-1;
                return;
            }
        }

        n--;
        l++;

        if (abs(m-n)<2 && abs (m-l)<2)
        {
            if (l>=p)
            {
                *a=*a-1;
                *c=*c+1;
                return;
            }
        }
        else if (abs(m-n)==2 || abs (m-l)==2)
        {
            if (l>=p)
            {
                *a=*a-1;
                *c=*c+1;
                *s=*s-1;
                return;
            }
        }
        l--;
    }

    m++;

    n--;
    if (n>=0)
    {
        m++;

        if (abs(n-m)<2 && abs (n-l)<2)
        {
            if (m>=p)
            {
                *b=*b-1;
                *a=*a+1;
                return;
            }
        }

        else if (abs(n-m)==2 || abs (n-l)==2)
        {
            if (m>=p)
            {
                *b=*b-1;
                *a=*a+1;
                *s=*s-1;
                return;
            }
        }

        m--;
        l++;

        if (abs(n-m)<2 && abs (n-l)<2)
        {
            if (l>=p)
            {
                *b=*b-1;
                *c=*c+1;
                return;
            }
        }

        if (abs(n-m)==2 || abs (n-l)==2)
        {
            if (l>=p)
            {
                *b=*b-1;
                *c=*c+1;
                *s=*s-1;
                return;
            }
        }

        l--;
    }
    n++;

    l--;
    if (l>=0)
    {
        m++;

        if (abs(l-m)<2 && abs (n-l)<2)
        {
            if (m>=p)
            {
                *c=*c-1;
                *a=*a+1;
                return;
            }
        }
        else if (abs(l-m)==2 || abs (n-l)==2)
        {
            if (m>=p)
            {
                *c=*c-1;
                *a=*a+1;
                *s=*s-1;
                return;
            }
        }

        m--;
        n++;


        if (abs(l-m)<2 && abs (n-l)<2)
        {
            if (n>=p)
            {
                *c=*c-1;
                *b=*b+1;
                return;
            }
        }

        else if (abs(l-m)==2 || abs (n-l)==2)
        {
            if (n>=p)
            {
                *c=*c-1;
                *b=*b+1;
                *s=*s-1;
                return;
            }
        }
    }
    l++;
}
bool canBe (int *s, int p, int ti)
{
    int a,b,c;

    a = ti/3;
    b = ti/3;
    c = ti/3;

    correct(&a, &b, &c, ti);

    if (hasP (a,b,c,p))
    {
        return true;
    }
    correctWithSuprise(&a,&b,&c,p,*&s);

    if (*s<0)
    {
        return false;
    }

    if (hasP (a,b,c,p))
    {
        return true;
    }

    return false;

}

int main()
{
    ifstream input;
    ofstream output;
    input.open ("input.txt");
    output.open ("output.txt");

    //FILE *in = fopen("input1.in", "r");
    //FILE *out = fopen("output1.out", "w");


    int t, n, i, s, p, ti;
    input >> t;
    //fscanf(in, "%d", &t);
    int ok = 0;

    for (i = 0; i < t; i++)
    {
        input >> n >> s >> p;
        //fscanf(in, "%d %d %d", &n, &s, &p);
        for (int j = 0; j < n; j++)
        {
            input >> ti;
            //fscanf(in, "%d", &ti);

            if (canBe (&s, p, ti))
            {
                ok++;
            }
        }

        output << "Case #" << i+1 << ": " << ok << endl;
        //fprintf(out, "Case #%d: %d\n", i+1, ok);
        ok= 0;
    }

    input.close ();
    output.close ();
    //fclose(in);
    //fclose(out);

    return 0;
}
