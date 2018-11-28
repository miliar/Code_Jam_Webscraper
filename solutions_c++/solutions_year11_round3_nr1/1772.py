#include <fstream>
using namespace std;

#define IDX(i, j, N) ((i)*(N) + (j))

bool check_square(char *a, const long i, const long j, const long x) {
    if (a[IDX(i, j, x)] == '#' &&
        a[IDX(i, j + 1, x)] == '#' &&
        a[IDX(i + 1, j, x)] == '#' &&
        a[IDX(i + 1, j + 1, x)] == '#')
    {
        return true;
    }
    else
    {
        return false;
    }
}

void update_square(char *a, const long i, const long j, const long x)
{
    a[IDX(i, j, x)] = '/';
    a[IDX(i, j + 1, x)] = '\\';
    a[IDX(i + 1, j, x)] = '\\';
    a[IDX(i + 1, j + 1, x)] = '/';
}

int main()
{
    const char ifname[] = "input.txt";
    const char ofname[] = "output.txt";
    const char impossible[] = "Impossible";
    const int MAX = 50;

    ifstream inf(ifname);
    ofstream ouf(ofname);

    long T,t,i,j,x,y;
    char tmp;
    char *a = new char[MAX * MAX];

    inf >> T;

    for (t = 0; t < T; t++)
    {
        inf >> y >> x;
        for (i = 0; i < y; i++)
        {
            for (j = 0; j < x; j++)
                inf >> a[IDX(i, j, x)];
            inf.getline(&tmp, 1);
        }

        bool ok = true;
        for (i = 0; i < y - 1 && ok; i++)
        {
            for (j = 0; j < x - 1 && ok; j++)
            {
                if (check_square(a, i, j, x))
                {
                    update_square(a, i, j, x);
                    j++;
                }
                else
                {
                    if (a[IDX(i,j,x)] == '#') ok = false;
                }
            }
            if (a[IDX(i,x - 1, x)] == '#') ok = false;
        }
        for (j = 0; j < x; j++)
        {
            if (a[IDX(y - 1, j, x)] == '#') ok = false;
        }

        ouf << "Case #" << t + 1 << ":" << endl;
        if (!ok) 
        {
            ouf << impossible << endl;
        }
        else
        {
            for (i = 0; i < y; i++)
            {
                for (j = 0; j < x; j++)
                {
                    ouf << a[IDX(i,j,x)];
                }
                ouf << endl;
            }
        }
    }
    
    inf.close();
    ouf.close();
    return 0;
}