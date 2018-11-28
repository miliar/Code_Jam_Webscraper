#include <set>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>

using namespace std;

vector<string> split(const string& path)
{
    vector<string> result;
    string dir;
    for (int i = 0; i < path.size(); i++)
    {
        if (path[i] == '/')
        {
            if (dir != "")
                result.push_back(dir);
            dir = "";
        }
        dir += path[i];
    }
    if (dir != "")
        result.push_back(dir);
    return result;
}

int maxequal(const vector<string>& path1, const vector<string>& path2)
{
    for (int i = 0; i < min(path1.size(), path2.size()); i++)
    {
        if (path1[i] != path2[i])
            return i;
    }
    return min(path1.size(), path2.size());
}

int main()
{
    fstream fin("input.txt");    
    fstream fout("output.txt", ios_base::out);
    int tests, n, m;
    fin >> tests;
    for (int test = 0; test < tests; test++)
    {
        int answer = 0;
        fin >> n >> m;
        vector<string> paths;
        for (int i = 0; i < n; i++)
        {
            string path;
            fin >> path;
            paths.push_back(path);
        }
        vector<string> newpaths;
        for (int i = 0; i < m; i++)
        {
            string path;
            fin >> path;
            newpaths.push_back(path);
        }
        sort(newpaths.begin(), newpaths.end());
        for (int i = 0; i < newpaths.size(); i++)
        {
            vector<string> parts = split(newpaths[i]);
            int maxe = 0;
            for (int j = 0; j < paths.size(); j++)
            {
                maxe = max(maxe, maxequal(parts, split(paths[j])));
            }
            answer += (int)parts.size() - maxe;
            paths.push_back(newpaths[i]);
        }   
        fout << "Case #" << test + 1 << ": " << answer << endl;
    }
    fin.close();
    fout.close();
    return 0;
}