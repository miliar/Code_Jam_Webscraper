#include <iostream>
#include <string>
#include <set>

using namespace std;


int main()
{
    int N = 0;
    cin >> N;
    
    int i;
    for(i = 0; i < N; i++)
    {
        int S = 0;
        cin >> S;
        
        cin >> ws; // skip newline

        int j;
        for(j = 0; j < S; j++)
        {
            char szEngine[101];
            cin.getline(szEngine, sizeof(szEngine));
            // ignore engine names
        }
        
        int Q = 0;
        cin >> Q;
        cin >> ws; // skip newline

        set<string> queries;
        int res = 0;
        for(j = 0; j < Q; j++)
        {
            char szQuery[101];
            cin.getline(szQuery, sizeof(szQuery));

            queries.insert(szQuery);

            if (queries.size() == S)
            {
                res++;
                queries.clear();
                queries.insert(szQuery);
            }
        }
            
        cout << "Case #" << (i + 1) << ": " << res << endl;
    }
    
    return 0;
}

