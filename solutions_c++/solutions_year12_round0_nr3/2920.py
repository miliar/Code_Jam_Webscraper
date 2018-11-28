#include <iostream>
#include <fstream>
using namespace std;

int get_digits(int x)
{
    int i = 0;
    while(x = x/10)
        i++;
    return i+1;
}

int get_cycle(int x, int n, int i)
{
    int pow_i = 1;
    int pow_ni = 1;
    for(int j=0; j<i; j++)
        pow_i *= 10;
    for(int j=0; j<n-i; j++)
        pow_ni *= 10;

    return (x%pow_i)*pow_ni + (x/pow_i);
}

int main()
{
    int T, A, B;
    int count;
    ifstream in("C-small-attempt0.in");
    ofstream out("C-small-attempt0.out");

    in >> T;
    for(int m=1; m<=T; m++)
    {
        in >> A >> B;
        count = 0;
        for(int i=A; i<=B; i++)
        {
            int n = get_digits(i);
            for(int j=1; j<=n-1; j++)
            {
                int c = get_cycle(i, n, j);
                if(c>=A && c<=B && c != i)
                {
                    //cout << c << '\t';
                    count++;
                }
            }
        }
        count /= 2;
        out << "Case #" << m << ": " << count << endl;
        //cout << endl;
    }

    in.close();
    out.close();

    return 0;
}
