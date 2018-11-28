#include <iostream>
#include <string>
#include <map>

using namespace std;


typedef struct TreeNodeStruct
{
    map<string, struct TreeNodeStruct* > SubDirs;
} TreeNode;

string GetNextDir(string* path)
{
    size_t slash = path->find_first_of('/');
    string res = path->substr(0, slash);
    if (slash != string::npos)
    {
        *path = path->substr(slash+1);
    }
    else
    {
        *path = string("");
    }
    return res;
}

int main()
{
    int t, n, m;
    cin >> t;

    for (int i=1;i<=t;i++)
    {
        TreeNode* FileTree = new TreeNode;
        TreeNode* CurrTree;

        string Temp;
        string CurrPath;
        string CurrDir;

        int res = 0;
        cin >> n;
        cin >> m;

        for (int j=0;j<n;j++)
        {
            CurrTree = FileTree;
            cin >> Temp;
            CurrPath = Temp.substr(1);

            while (CurrPath.size() != 0)
            {
                CurrDir = GetNextDir(&CurrPath);
                if (CurrTree->SubDirs.count(CurrDir))
                {
                    CurrTree = CurrTree->SubDirs[CurrDir];
                }
                else
                {
                    TreeNode* NewNode = new TreeNode;
                    CurrTree->SubDirs[CurrDir] = NewNode;
                    CurrTree = NewNode;
                }
            }
        }
        for (int j=0;j<m;j++)
        {
            CurrTree = FileTree;
            cin >> Temp;
            CurrPath = Temp.substr(1);

            while (CurrPath.size() != 0)
            {
                CurrDir = GetNextDir(&CurrPath);
                if (CurrTree->SubDirs.count(CurrDir))
                {
                    CurrTree = CurrTree->SubDirs[CurrDir];
                }
                else
                {
                    res++;
                    TreeNode* NewNode = new TreeNode;
                    CurrTree->SubDirs[CurrDir] = NewNode;
                    CurrTree = NewNode;
                }
            }
        }

        cout << "Case #" << i << ": " << res << endl;
    }

    return 1;
}
