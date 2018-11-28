#include <iostream>
#include <string>
#include <fstream>
#include <cmath>

using namespace std;

ofstream outs ("output.txt");
#define cout outs

ifstream ins ("input.txt");
#define cin ins
#define FOR(i,n) for(int i = 0; i<n; i++)

char arr[40];
int size;

int find (char in)
{
    FOR (i, size)
        if (arr[i] == in)
            return i;

    //cout << in << endl;
    arr[size] = in;
    size++;
    return size-1;
}

int Solve (int *in, int l)
{
    int a = 0;
    if (size == 1)
        size++;
    FOR (i, l)
    {
        a += in[i] * pow(size, l-i-1);
    }
    return a;
}

int ans (string in)
{
    if (in.length() == 1)
        return 1;
    int a[65];

    if (in[0] != in[1])
    {
        a[0] = 0;
        a[1] = 1;
        arr[0] = in[0];
        arr[1] = in[1];
        size = 2;
    }else{
        a[0] = a[1] = 0;
        arr[0] = in[0];
        size = 1;
    }

    for (int n = 2; n < in.length(); n++)
    {
        a[n] = find(in[n]);
    }

    FOR (i, in.length())
    {
        if (a[i] == 0)
            a[i] = 1;
        else if (a[i] == 1)
            a[i] = 0;
    }

    //cout << size << arr[0] << ";" << arr[1] << ";" << arr[2] << ";" << endl;

    return Solve(a, in.length());
}

int main()
{
    int n;
    string input;
    cin >> n;
    getline(cin, input);
    FOR(z, n)
    {
        size = 0;
        getline(cin, input);

        //cout << input << endl;

        cout << "Case #" << z+1 << ": " << ans(input) << endl;
    }

    return 0;
}
