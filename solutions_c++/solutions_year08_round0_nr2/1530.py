#include <iostream>
#include <vector>
using namespace std;

int T, NA, NB;

int An, Bn;

int SA[101], EA[101];
int SB[101], EB[101];
//int Aaval[2000], Baval[2000];

int Convert(string s)
{
    int hr, mn;
    sscanf(s.c_str(), "%d:%d", &hr, &mn);
    return hr * 60 + mn;
}

    vector<int> List[2][1500];

void Greedy(int, int);

void Solve()
{
//    memset(Aval, 0, sizeof Aval);
//    memset(Bval, 0, sizeof Bval);
    
    string s, t;
    cin >> T >> NA >> NB;
    
    vector< pair< pair<int, int>, int > > schedule;
    
    for (int o = 0; o<=1; o++)
        for (int i = 0; i<1500; i++)
            List[o][i].clear();
    
    for (int i = 0; i<NA; i++)
    {
        cin >> s >> t;
        int st = Convert(s), ed = Convert(t) + T <? 1440;
        SA[i] = st;
        EA[i] = ed;
        schedule.push_back( make_pair( make_pair(st, ed), 0 ) );
        List[0][st].push_back(ed);
    }
    for (int i = 0; i<NB; i++)
    {
        cin >> s >> t;
        int st = Convert(s), ed = Convert(t) + T <? 1440;
        SB[i] = st;
        EB[i] = ed;
        schedule.push_back( make_pair( make_pair(st, ed), 1 ) );
        List[1][st].push_back(ed);
    }
    sort(schedule.begin(), schedule.end());
    
    An = Bn = 0;
/*    
    for (vector< pair< pair<int, int>, int > >::iterator p = schedule.begin();
        p != schedule.end(); p++)
        {
            if (
        }*/
    for (int t = 0; t<1440; t++)
        for (int o = 0; o<=1; o++)
        {
            sort(List[o][t].rbegin(), List[o][t].rend());
            /*
            if (List[o][t].size() > 0)
            {
            for (int i = 0; i<List[o][t].size(); i++) 
                cout << List[o][t][i] << ' ';
            cout << endl;
            }*/
        }

    for (int t = 0; t<1440; t++)
        for (int o = 0; o<=1; o++)
        {
            while (List[o][t].size() > 0)
            {
                int next = List[o][t].back();
                List[o][t].pop_back();
                if (o==0) ++An; else ++Bn;
                Greedy(1-o, next);
            }
        }
}

void Greedy(int o, int t)
{
    while (t < 1440)
    {
        if (List[o][t].size() > 0)
        {
            int next = List[o][t].back();
            List[o][t].pop_back();
            t = next;
            o = 1-o;
        }else
        ++t;
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int task, cn;
    cin >> task;
    for (cn = 1; cn<=task; cn++)
    {
        cout << "Case #" << cn << ": ";
        Solve();
        cout << An << ' ' << Bn << endl;
    }

}
