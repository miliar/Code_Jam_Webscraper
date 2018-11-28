
#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N;

    cin >> N;
    
    for( int CASE = 1; CASE <= N; CASE++ )
    {
        int S, Q;

        cin >> S;

        map<string, int> codes;

        char str[150]; 
        cin.getline(str, 101);

        //cout << "search engines" << endl;
        for( int i = 0; i < S; i++ )
        {
            cin.getline(str, 101);
            string s(str);

            //cout << i << ": " << s << endl;
            codes[s] = i;
        }

        vector<int> count(S, 0);

        cin >> Q;
        cin.getline(str, 101);

        vector<int> queries(Q, 0);

        //cout << "queries" << endl;
        for( int i = 0; i < Q; i++ )
        {
            cin.getline(str, 101);
            string s(str);

            //cout << i << ": " << s << " code: " << codes[s] << endl;
            
            queries[i] = codes[s];
            (count[codes[s]])++;
        }

        /*int min = count[0];
        int i_min = 0;
        for( int i = 1; i < S; i++ )
        {
            if( count[i] < min )
            {
                min = count[i];
                i_min = i;
            }
        }*/

        int t = -1;
        int switches = 0;
        int cur = -1;
        while( t < Q )
        {
            int ss = 0;
            vector<int> se_found(S, 0);
            int i, ncur = -1;
            for(i=t+1; ss < S-(cur>=0?1:0) && i < Q; i++)
            {
                //cout << "i " << i << " ";
                //cout << "q " << queries[i] << endl;
                if( queries[i] != cur && !(se_found[queries[i]]) )
                {
                    se_found[queries[i]] = 1;
                    ncur = queries[i];
                    ss++;
                }
            }
            if( i>=Q && ss < S-(cur>=0?1:0) ) break;

            cur = ncur;
            t = i-1;
            switches++;
        }

        cout << "Case #" << CASE << ": " << switches << endl;
    }

    return 0;
}


