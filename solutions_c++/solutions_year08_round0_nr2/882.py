# include <string>
# include <cstdio>
# include <cstdlib>
# include <algorithm>
# include <fstream>
# include <queue>

using namespace std;

int gettime (const string & time)
{
    int h, m ;
    sscanf (time.c_str(), "%d:%d", &h, &m);
    return h * 60 + m;
}

struct tour
{
    int part;
    int time ;
    int len ;

    tour () {}
    tour (int _part, int _time)
    {
        part = _part;
        time = _time;
    }

    bool operator < (const tour & other) const 
    {
        if (time != other.time) return time < other.time;
        return part < other.part;
    }
    
    bool operator > (const tour & other) const 
    {
        if (time != other.time) return time > other.time;
        return part > other.part;
    }
};

const int MAXN  = 1024;
tour tours [MAXN];

int main ()
{   
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");

    int tests;
    fin >> tests;
    while (tests -- > 0)
    {
        int t ;
        int n, m ;
        fin >> t >> n >> m ;
        int k = 0;
 
        for (int i = 0; i < n; ++ i)
        {
            string time;
            fin >> time;
            int _time = gettime(time);
            fin >> time;
            tours [k].len = gettime(time) - _time;
            tours [k].part = 0;
            tours [k].time = _time;
            ++ k;
        }
        
        for (int i = 0; i < m; ++ i)
        {
            string time;
            fin >> time;
            int _time = gettime(time);
            fin >> time;
            tours [k].len = gettime(time) - _time;
            tours [k].part = 1;
            tours [k].time = _time;
            ++ k;
        }

        sort (tours, tours + k);

        int res = 1000000;
        int ra, rb;

        if (n + m == 0)
        {
            res = 0;
            ra = rb = 0;
        }

        for (int aa = 0; aa <= n && aa < res; ++ aa)
            for (int bb = 0; bb <= m && aa + bb < res ; ++ bb)
            {
                priority_queue<tour, vector<tour>, greater<tour> > all [2];
                bool ok = false;

                for (int i = 0; i < aa; ++ i) all[0].push(tour(0, 0));
                for (int i = 0; i < bb; ++ i) all[1].push(tour(0, 0));

                for (int i = 0; i < k; ++ i)
                {
                    int part = tours [i].part;

                    if (all[part].empty() || all[part].top().time > tours [i].time )
                    {
                        ok = false;
                        break;
                    }
                    else 
                    {
                        all [part].pop();
                        all[1 - part].push(tour(1 -part, tours[i].time + tours[i].len + t));
                    }

                    if (i == k - 1) ok = true;
                }

                if (ok)
                {
                    if (res > aa + bb)
                    {
                        res = aa + bb;
                        ra = aa;
                        rb = bb;
                    }
                    break;
                }
            }

            static int caseNum = 0;
            ++ caseNum;
            fout << "Case #" << caseNum << ": " << ra << " " << rb << endl;
    }

    return 0;
}