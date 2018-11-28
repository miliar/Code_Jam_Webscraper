#include <cstring>
#include <fstream>
#include <sstream>
#include <string>
#include <map>
#include <vector>
#include <iostream>
#include <iomanip>

using std::ifstream;
using std::ofstream;
using std::string;
using std::stringstream;
using std::map;
using std::vector;

class R1BA
{
private:

    string append(const char * a, const char * b)
    {
        string c(a);
        c += b;
        return c;
    }
public:

    R1BA(const char* naam) : sc(append(naam, ".in").c_str()), ps(append(naam, ".out").c_str())
    {
        if (!sc.is_open() || !ps.is_open())
            throw "foutje";
        index = 0;
        sc >> size;
        //init
        next();
    }

    virtual ~R1BA()
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
        int vs;
        sc >> vs;
        v.reserve(vs);
        v.resize(vs);
        for (int i = 0; i < vs; i++)
            v[i] = new Team(i);
        char c;
        for (int i = 0; i < vs; i++)
        {
            for (int j = 0; j < vs; j++)
            {
                sc >> c;
                if (c != '.')
                    (v[i]->a).insert(std::pair < Team*, bool>(v[j], (c == '1')));
            }
        }
        index++;
    }

    void solve()
    {
        //calc

        for (int i = v.size() - 1; i >= 0; i--)
            v[i]->calcWP();
        for (int i = v.size() - 1; i >= 0; i--)
            v[i]->calcOWP();
        for (int i = v.size() - 1; i >= 0; i--)
            v[i]->calcOOWP();

        for (int i = 0; i < v.size(); i++)
            ss << std::endl << std::setprecision(10) << v[i]->getRPI();

        for (int i = v.size() - 1; i >= 0; i--)
            delete v[i]; //reinit is better
        v.clear();
        print();
    }
private:
    //data

    class Team
    {
    public:

        Team(int n_) : n(n_)
        {
        }

        bool operator<(const Team& b) const
        {
            return n < b.n;
        }

        void calcWP()
        {
            int w = 0;
            int t = 0;
            map < Team*, bool>::iterator it = a.begin();
            while (it != a.end())
            {
                if ((*it).second)
                    w++;
                t++;
                it++;
            }
            wp = (double) w / (double) t;
        }

        void calcOWP()
        {
            double ow = 0.0;
            int t = 0;
            map < Team*, bool>::iterator it = a.begin();
            while (it != a.end())
            {
                int s = it->first->a.size();
                int n = it->first->wp * s;
                if (!(*it).second)
                    n--;
                s--;
                ow += ((double) n / (double) s);
                t++;
                ++it;
            }
            owp = ow / (double) t;
        }

        void calcOOWP()
        {
            double oow = 0.0;
            int t = 0;
            map < Team*, bool>::iterator it = a.begin();
            while (it != a.end())
            {
                oow += it->first->owp;
                t++;
                ++it;
            }
            oowp = oow / (double) t;
        }

        double getRPI()
        {//RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
            return 0.25 * wp + 0.5 * owp + 0.25 * oowp;
        }

        int n; //nummer
        double wp;
        double owp;
        double oowp;
        map<Team*, bool> a; //against
    };
    vector<Team*> v;
};

using namespace std;

int main()
{
    R1BA cd("A-small-attempt0");
    cd.solve();
    while (cd.hasMore())
    {
        cd.next();
        cd.solve();
    }
    cd.close();
    return 0;
}
