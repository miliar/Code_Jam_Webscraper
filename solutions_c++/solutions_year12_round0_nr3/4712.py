#include <iostream>
#include <string>

using namespace std;

const string zs = string("0");

int countRecycled(int a, int b)
{
    int rc = 0;
    for(int m = a; m <= b; m++)
    {
        char sc[7];
        itoa(m, sc, 10);
        string s = string(sc);
        for(int i = 1; i < s.length(); i++)
        {
            string part1 = s.substr(0, i);
            string part2 = s.substr(i, s.length() - i);
            if(part2.substr(0, 1) == zs) continue;
            string recyc = part2 + part1;
            int z = atoi(recyc.c_str());
            if((z >= a) && (z <= b) && (z > m)) rc++;
//            cout << a << b << " " << m << " strings " << part1 << " " << part2 << " " << recyc << " z=" << z << " yrc=" << rc << endl;
        }
    }
    return rc;
}

int main (int argc, char *argv[])
{
    int n;
    cin >> n;
    
    int a[50], b[50];
    for(int i = 0; i < 50; i ++)
        for(int j = 0; j < 50; j++)
            a[i]=b[i]=0;

    for(int i = 0; i < n; i++)
    {
        cin >> a[i] >> b[i];
    }

    for(int i = 0; i < n; i++)
    {
        cout << "Case #" << i+1 << ": " << countRecycled(a[i],b[i]) << endl;
    }
    return 0;
}
