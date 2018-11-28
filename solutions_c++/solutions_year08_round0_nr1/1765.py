#include <vector>
#include <fstream>
#include <sstream>
#include <iostream>
using namespace std;

int find_how_many_queries_can_go_with_this_engine(string engine, const vector<string>& queries, unsigned int i)
{
    int ret = 0;
    while(i < queries.size() && queries[i] != engine)
    {
        ret++;
        i++;
    }

    return ret;
}

int main()
{
    ifstream in ("A-large.in");
    ofstream out("A-large.out");

    int N,S,Q;
    int s,q;
    char buf[100];

    in >> N;

    for(int n = 0; n < N; n++)
    {
        in >> S;
        vector<string> engines;

        // go to the enxt line...
        in.getline(buf,100);

        for(s = 0; s < S; s++)
        {
            in.getline(buf,100);
            engines.push_back(buf);
        }

        in >> Q;
        vector<string> queries;

        // go to the enxt line...
        in.getline(buf,100);

        for(q = 0; q < Q; q++)
        {
            in.getline(buf,100);
            queries.push_back(buf);
        }

        out << "Case #" << n + 1 << ": ";
        if(Q == 0)
        {
            out << "0" << endl;
            continue;
        }

        int switches = -1;
        for(q = 0; q < Q;)
        {
            int max = 0;
            for(s = 0; s < S; s++)
            {
                int m = find_how_many_queries_can_go_with_this_engine(engines[s],queries,q);

                max = (m > max) ? (m) : (max);
            }

            q += max;
            switches++;
        }

        out << switches << endl;
    }

    return 0;
}
