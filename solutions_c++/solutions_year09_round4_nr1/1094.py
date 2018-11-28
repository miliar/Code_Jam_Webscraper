#include <cstdio>
#include <string>

using namespace std;

string gl()
{
    char chGl [1024*1024];
    gets (chGl);
    string gl = chGl;
    return gl;
}
// get line as integer
int gli()
{
    string gli = gl();
    return atoi(gli.c_str());
}

// how many zeroes to right?
int zer (string s, int n)
{int i;
    for (i=0; i<n; i++)
    {
        if (s[n-1-i] == '1') break;
    }
    return i;
}



int main ()
{
    //freopen ("input.txt", "r", stdin);
    freopen ("A-large.in", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int T;
    T=gli();
    for (int cas=1; cas<=T; cas++)
    {
        int n;
        n=gli();
        string a[100];
        for (int i=0; i<n; i++)
        {
            string x;
            x=gl();
            a[i] =x;
            //printf ("%s\n", a[i].c_str());
        }

        int rep = n;
        // while (rep--){
        int count =0;

        for (int i=0; i<n; i++) //row
        {
            int j;
            for (j=i; j<n; j++) //one that fits
            {
                if (zer(a[j], n) >= n-i-1)
                {
                    break;
                }
            }
           // printf ("i %d j %d\n", i, j);
            //j
            // swap to pos it
            if (j>i)
            {
                int ptr =j;
                while (ptr > i) // ou tof position
                {
                    count++;
                    string tmp = a[ptr];
                    a[ptr] = a[ptr-1];
                    a[ptr-1] = tmp;
                    ptr--;
                }
            }
        //for (int i=0; i<n; i++) printf ("%s\n", a[i].c_str());
        }

        printf ("Case #%d: %d\n", cas, count);
    }
    return 0;
}
