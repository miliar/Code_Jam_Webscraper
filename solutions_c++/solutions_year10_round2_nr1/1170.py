#include <stdio.h>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

string GetParent(string path)
{
    int index = path.rfind('/');
    if (0 == index)
    {
        return string("/");
    }
    
    return path.substr(0, index);
}

int main()
{
    int t;
    int m;
    int n;
    cin >> t;
    vector<string> existing(400);
    vector<string> toCreate (101);

    existing.clear();
    toCreate.clear();

    for (int w = 0; w < t; w++)
    {
        cin >> n >> m;
        for (int k = 0; k < n; k++)
        {
            string path;
            cin >> path;
            existing.push_back(path);
        }

        for (int l = 0; l < m; l++)
        {
            string path2;
            cin >> path2;
            toCreate.push_back(path2);
        }

        int result = 0;
        existing.push_back(string("/"));
        
        for (int k = 0; k < toCreate.size(); k++)
        {
            int existingCnt = existing.size();
            string current = toCreate[k];
            bool found = false;
            for (int p = 0; p < existingCnt;  p++)
            {
                if (existing[p] == current)
                {
                    found = true;
                    break;
                }
            }
            if (!found)
            {
                string parent = GetParent(current);
                bool foundParent = false;
                int localRes = 1;
                while (!foundParent)
                {
                    for (int p = 0; p < existingCnt;  p++)
                    {
                        if (existing[p] == parent)
                        {
                            foundParent = true;
                            break;
                        }
                    }
                    if (!foundParent)
                    {
                        parent = GetParent(parent);
                        localRes++;
                    }
                }
                result += localRes;
                for (int p = 0; p < localRes; p++)
                {
                    existing.push_back(current);
                    current = GetParent(current);
                }
            }

        }

        toCreate.clear();
        existing.clear();
        cout << "Case #" << w + 1 << ": " << result << "\n";
    }
    return 0;
}