#include<cstdio>
#include<cstring>
#include<map>
#include<string>
#include<vector>

using namespace std;

vector< map<string,int>* > direc;

void addDirec(char* path)
{
    vector<string> dirs;
    char *dir;
    dir = strtok(path, "/");
    while (dir != NULL)
    {
        string dirstring(dir);
        dirs.push_back(dirstring);
        dir = strtok (NULL, "/");
    }
    int i;
    int pos = 0;
    for (i=0; i<dirs.size(); i++)
    {
        if (direc[pos]->count(dirs[i]) > 0)
        {
            pos = (*direc[pos])[dirs[i]];
        }
        else
        {
            int newIndex = direc.size();
            (*direc[pos])[dirs[i]] = newIndex;
            direc.push_back(new map<string,int>());
            pos = newIndex;
        }
    } 
}

int main()
{
    char buf[1000];
    int t, teste;
    int n, m;
    int i;
    scanf("%d", &teste);
    for (t=0; t<teste; t++)
    {
        for (i=0; i<direc.size(); i++)
        {
            delete direc[i];
        }
        direc.clear();
        direc.push_back(new map<string,int>());
        scanf("%d %d", &n, &m);
        for (i=0; i<n; i++)
        {
            scanf("%s", buf);
            addDirec(buf);
        }
        int resp = -direc.size();
        for (i=0; i<m; i++)
        {
            scanf("%s", buf);
            addDirec(buf);
        }
        resp += direc.size();
        printf("Case #%d: %d\n", t+1, resp);
    }
    return 0;
}
