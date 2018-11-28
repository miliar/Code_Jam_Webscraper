#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <sstream>

using namespace std;

int main(int argc, char **argv)
{
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    int T;
    fin>>T;
    for(int t = 1; t <= T; t++)
    {
        int N,L,H;vector<int> list;
        fin>>N>>L>>H;
        for(int i = 0; i < N; i++)
        {
            int tmp; 
            fin>>tmp;
            list.push_back(tmp);
        }
        bool succ = false;
        fout<<"Case #"<<t<<": ";
        for(int i = L; i<=H; i++)
        {
            bool m = true;
            for(int j = 0; j< list.size(); j++)
            {
                if(list[j]%i != 0 && i%list[j]!=0)
                {m = false;break;}
            }
            if(m)
            {
                fout<<i<<endl;
                succ = true;
                break;
            }
        }
        if(!succ)fout<<"NO"<<endl;
    }

    return 0;
}
