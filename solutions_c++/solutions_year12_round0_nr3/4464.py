#include <fstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

#ifdef DEBUG
    ifstream cin("input.in");
    ofstream cout("output.out");
#else
    #include <iostream>
#endif

#define MAXN 1500
#define MAXLEN 15

int n;

int isRec(int n, int m)
{
    int count=0;
    char sM[2*MAXLEN], sN[2*MAXLEN], tmp[MAXLEN];
    sprintf(sM, "%d", m);
    sprintf(sN, "%d", n);
    int lenM=strlen(sM);
    strcpy(tmp, sM);
    strcat(sM, tmp);

    for(int i=0; i < lenM; i++)
    {
        strncpy(tmp, sM+i, lenM);
        int t=atoi(tmp);
        if(t==n) return 1;
    }
    return count;
}

int solve(int a, int b)
{
    int count=0;
    for(int i=a; i <b; i++)
        for(int j=i+1; j<=b; j++)
            count+=isRec(i, j);
    return count;
}

int main()
{
    cin >> n;
    for(int i=0; i < n; i++)
    {
        int a, b;
        cin >> a >> b;
        cout << "Case #" << (i+1) << ": " << solve(a, b) << endl;
    }
    return 0;
}
