 #include <fstream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

int main(void)
{
    ifstream fin("a-input.in");
    ofstream fout("a-output.out");
    int N;
    fin >> N;
    for(int i=1; i<=N; i++)
    {
        int S,Q;
        vector <string> searchEngines;
        vector <string> queries;
        string line="";
        fin >> S;
        getline(fin, line);
        for(int j=0; j<S; j++)
        {
            getline(fin, line);
            searchEngines.push_back(line);
        }
        fin >> Q;
        getline(fin, line);
        for(int j=0; j<Q; j++)
        {
            getline(fin, line);
            queries.push_back(line);
        }
        int ret=0;
        int j=0;
        while(j<Q)
        {
            int best=-1;
            for(int k=0; k<S; k++)
            {
                int m;
                for(m=j; m<Q; m++) if(searchEngines[k]==queries[m]) break;
                if(best<(m-j)) best=m-j;
            }
            if(j!=0) ret++;
            j+=best;
        }
        fout << "Case #" << i << ": " << ret << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
