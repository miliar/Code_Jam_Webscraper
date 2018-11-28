#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <vector>

using namespace std;

typedef struct
{
    int n;
    int m;
}DUP;

int dif (int ,int ,int ,vector <DUP>);

int main ()
{
    ios_base::sync_with_stdio (false);

    int t;
    int a,b;
    int sum;
    vector <DUP> dup;

    cin >> t;
   
    for (int i = 0 ; i < t ; i++)
    {
        sum = 0;

        cin >> a >> b;

        for (int j = a ; j <= b ; j++)
            sum += dif (j,a,b,dup);

        dup.clear ();
        cout << "Case #" << i+1 << ": " << sum << endl;
    }

    exit (EXIT_SUCCESS);
}

int dif (int key,int a, int b ,vector <DUP> dup)
{
    char str[20];
    char tmp[7],tmp2[7];
    char out[7];
    int sum = 0;

    sprintf (tmp , "%d" , key);
    strcpy (str,tmp);
    strcat (str,tmp);

    int len = strlen (tmp);

    for (int i = len  ; i > 1 ; i--)
    {
        strncpy (out,str+i-1,len);
        out[len] = '\0';
        sprintf (tmp2,"%d",a);

        int m = atoi(out);
        if (m >= a && strlen (out) == strlen (tmp2) && m <= b && m > key)
        {
            int size = dup.size();
            bool cdup = false;
            for (int j = 0 ; j < size ; j++)  
            {
                if (dup.at(j).n == key && dup.at(j).m == m)
                {
                    cdup = true;
                    break;
                }
            }
            if (!cdup)
            {
                sum++;
                DUP d;
                d.n = key;
                d.m = m;
                dup.push_back (d);
            }
        }
    }

    return sum;
}
