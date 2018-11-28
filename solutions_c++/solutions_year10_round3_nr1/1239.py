#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <list>

using namespace std;

struct wire_t
{
    long start;
    long end;
};

int main(int argc, char *argv[])
{
    ifstream ifs(argv[1]);
    ofstream ofs(argv[2]);

    int TC;

    ifs >> TC;

    for (int t = 1; t <= TC; t++)
    {
        vector<wire_t> wires;
        int N;
        int res = 0;

        ifs >> N;

        for (int i = 0; i < N; i++)
        {
            int start, end;
            ifs >> start >> end;

            for (int w = 0; w < wires.size(); w++)
            {
                if ((start < wires[w].start and end < wires[w].end) or (start > wires[w].start and end > wires[w].end))
                {
                }
                else
                {
                    res++;
                }
            }
            wire_t wire;
            wire.start = start;
            wire.end = end;
            wires.push_back(wire);
        }
        ofs << "Case #" << t << ": " << res << endl;
    }

    ifs.close();
    ofs.close();

    return (0);
}
