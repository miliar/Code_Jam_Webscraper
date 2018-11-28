#include <iostream>
#include <vector>
#include <map>
using namespace std;



int main()
{
    int TESTCOUNT;
    cin >> TESTCOUNT;
    #define MAXPATH 10000
    char dummy[MAXPATH];
    for(int testcount = 1; testcount<=TESTCOUNT; testcount++)
    {
        int result = 0;
        int N,M;
        cin >> N >> M;
        cin.getline( dummy, MAXPATH );
        // cout << "Dummy:"<<dummy << "]" <<endl; 
        // cout << "N:" << N << "M:" << M << endl;

        map<string,bool> tree;
        tree[""]=true;
        for(int i = 0;i<N; i++)
        {
            char str_path[MAXPATH];
            cin.getline( str_path, MAXPATH );
            string path( str_path );
            // cout << path <<endl;

            if (!path.empty() && *path.rbegin() != '/')
                path += "/";

            for(int pos = 0; path[pos]!=0; pos++)
            {
                if (path[pos]=='/')
                {
                    string subdir = path.substr( 0, pos );
                    tree[ subdir ] = true;
                    // cout << "Existing: [" << subdir << "]" << endl;
                    // cout << pos << ":" << subdir << endl;
                }
            }
        }
        for(int i = 0; i<M; i++)
        {
            char str_path[MAXPATH];
            cin.getline( str_path, MAXPATH );
            string path( str_path );
            // cout << path <<endl;

            if (!path.empty() && *path.rbegin() != '/')
                path += "/";

            for(int pos = 0; path[pos]!=0; pos++)
            {
                if (path[pos]=='/' || path[pos]=='\n')
                {
                    string subdir = path.substr( 0, pos );
                    if (tree.find( subdir ) == tree.end())
                    {
                        result++;
                        // cout << "Must create: [" << subdir << "]" << endl;
                    }
                    tree[ subdir ] = true;
                    // cout << pos << ":" << subdir << endl;
                }
            }
        }
        cout << "Case #" << testcount << ": " << result << endl;
    }
    return 0;
}
