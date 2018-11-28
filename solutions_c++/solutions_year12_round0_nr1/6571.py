#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int N;
    string A;
    cin >> N;
    getline (cin, A);
    for (int i=1; i<=N; i++)
    {
        string R="";
        getline (cin, A);
        for (int j=0; j<A.length(); j++)
        {
            if (A[j] == 'a')
            {
                R += 'y';
            }
            if (A[j] == 'b')
            {
                R += 'h';
            }
            if (A[j] == 'c')
            {
                R += 'e';
            }
            if (A[j] == 'd')
            {
                R += 's';
            }
            if (A[j] == 'e')
            {
                R += 'o';
            }
            if (A[j] == 'f')
            {
                R += 'c';
            }
            if (A[j] == 'g')
            {
                R += 'v';
            }
            if (A[j] == 'h')
            {
                R += 'x';
            }
            if (A[j] == 'i')
            {
                R += 'd';
            }
            if (A[j] == 'j')
            {
                R += 'u';
            }
            if (A[j] == 'k')
            {
                R += 'i';
            }
            if (A[j] == 'l')
            {
                R += 'g';
            }
            if (A[j] == 'm')
            {
                R += 'l';
            }
            if (A[j] == 'n')
            {
                R += 'b';
            }
            if (A[j] == 'o')
            {
                R += 'k';
            }
            if (A[j] == 'p')
            {
                R += 'r';
            }
            if (A[j] == 'q')
            {
                R += 'z';
            }
            if (A[j] == 'r')
            {
                R += 't';
            }
            if (A[j] == 's')
            {
                R += 'n';
            }
            if (A[j] == 't')
            {
                R += 'w';
            }
            if (A[j] == 'u')
            {
                R += 'j';
            }
            if (A[j] == 'v')
            {
                R += 'p';
            }
            if (A[j] == 'w')
            {
                R += 'f';
            }
            if (A[j] == 'x')
            {
                R += 'm';
            }
            if (A[j] == 'y')
            {
                R += 'a';
            }
            if (A[j] == 'z')
            {
                R += 'q';
            }
            if (A[j] == ' ')
            {
                R += ' ';
            }
        }
        cout << "Case #" << i << ": " << R << endl;
    }
    return 0;
}
