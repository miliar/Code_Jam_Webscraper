#include <iostream>
#include <list>


using namespace std;

int main (int argc, char ** argv)
{
    int N, S, Q, i, j, switches;
    list<string> engines;
    list<string> unused;
    string str, lstr;
    //
    cin >> N;
    for(i = 0; i < N; i++)
    {
        engines.clear();
        lstr="";
        switches=0;

        cin >> S;
        getline(cin, str);//eat the endl

        for(j = 0; j < S; j++)
        {
            getline(cin, str);
            engines.push_back(str);
        }

        unused = list<string>(engines);

        cin >> Q;
        getline(cin, str);//eat the endl

        for(j = 0; j < Q; j++)
        {
            getline(cin, str);
            if(str.compare(lstr)!=0)
                unused.remove(str);
            lstr=str;

            if(unused.empty())
            {
                switches++;
                unused = list<string>(engines);
                unused.remove(str);
            }
        }

        cout << "Case #" << i+1 << ": " << switches << endl;
    }

    return 0;
}
