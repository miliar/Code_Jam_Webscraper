#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <iterator>


using namespace std;

int g_NumEngines;
set<string> g_QuerySet;

void Clear()
{
    g_NumEngines = 0;
    g_QuerySet.clear();
}

void ReadEngines()
{
    cin >> g_NumEngines;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int i=0; i<g_NumEngines; i++)
    {
        // Ignore the engine names
        string engineName;
        getline(cin, engineName);
    }
}

void Run()
{
    ReadEngines();

    int Q;

    cin >> Q;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int numSwitches = 0;

    for (int i=0; i<Q; i++)
    {
        string query;
        getline(cin, query);

        g_QuerySet.insert(query);

        if (g_QuerySet.size() == g_NumEngines)
        {
            numSwitches++;
            g_QuerySet.clear();
            g_QuerySet.insert(query);
        }

        //copy(g_QuerySet.begin(),
             //g_QuerySet.end(),
             //ostream_iterator<string>(cout, " "));
        //cout << endl;
    }

    cout << numSwitches << endl;
    Clear();
}

int main(int argc, char *argv[])
{
    int N;
    cin >> N;

    for (int i=0; i<N; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        Run();
    }

    return 0;
}
