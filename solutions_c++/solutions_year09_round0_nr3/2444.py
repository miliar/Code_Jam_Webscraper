#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

const char test[] = {'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m'};

FILE * fout = fopen ("C.out", "w");

int num;

void count (char c[], int a, int t)
{
    for (int i = t; c[i] != 0; i ++)
    {
        if (c[i] == test[a])
        {
                 if (a == 18)
                 {
                       num ++;
                 }
                 else
                 {
                     count (c, a + 1, i + 1);
                 }
        }
    }
    return;
}

void work (int n)
{
     char api[500];
     char c;
     scanf ("%c", &c);
     int t = 0;
     while (c != '\n')
     {
           api[t] = c;
           scanf ("%c", &c);
           t ++;
     }
     api[t] = 0;
     num = 0;
     count (api, 0, 0);
     fprintf (fout, "Case #%d: %04d\n", n + 1, num);
}

int main (){
    int n;
    cin >> n;
    char c;
    scanf ("%c", &c);
    for (int i = 0; i < n; i ++)
    {
        work (i);
    }
    return 0;
}
