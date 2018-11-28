#include <cstring>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>

using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;
using std::vector;

class R1CC
{
private:

    string append(const char * a, const char * b)
    {
        string c(a);
        c += b;
        return c;
    }
public:

    R1CC(const char* naam) : sc(append(naam, ".in").c_str()), ps(append(naam, ".out").c_str())
    {
        if (!sc.is_open() || !ps.is_open())
            throw "foutje";
        index = 0;
        sc >> size;
        //init
        next();
    }

    virtual ~R1CC()
    {
    }

    void print()
    {
        ps << "Case #" << index << ": " << ss.str() << std::endl;
        ss.str("");
    }

    bool hasMore()const
    {
        return index < size;
    }

    void close()
    {
        sc.close();
        ps.close();
    }

private:
    ifstream sc;
    ofstream ps;
    stringstream ss;
    int index;
    int size;

public:

    void next()
    {
        //data
        int n;
        sc >> n;
        sc >> l;
        sc >> h;
        v.resize(n);
        for (int i = 0; i < n; i++)
            sc >> v[i];
        index++;
    }

    bool isgoede(int j)
    {
        for (int i = 0; i < v.size(); i++)
        {
            int min;
            int max;
            if (v[i] < j)
            {
                min = v[i];
                max = j;
            }
            else
            {
                min = j;
                max = v[i];
            }
            if (max % min != 0)
                return false;
        }
        return true;
    }

    void solve()
    {
        //calc
        int j = l;
        bool nietgoed = true;
        while (j <= h && nietgoed)
        {
            nietgoed = !isgoede(j);
            j++;
        }
        if (nietgoed)
            ss << "NO";
        else
            ss << (j - 1);
        print();
    }
private:
    //data
    int l;
    int h;
    vector<int> v;
};

using namespace std;

int main()
{
    R1CC cd("C-small-attempt0");
    cd.solve();
    while (cd.hasMore())
    {
        cd.next();
        cd.solve();
    }
    cd.close();
    return 0;
}
