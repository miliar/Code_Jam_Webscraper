#include <cstdio>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
vector<string> directory;

void setDirectory(char* input)
{
    int len = strlen(input);
    if(len <= 1) return;

    bool find = false;
    for(int i = 0; i < directory.size(); i++)
    {
        if(directory[i].compare(input) == 0)
        {
            find = true;
            break;
        }
    }
    if(find == false)
    {
        directory.push_back(input);
    }
    for(int i = len-2; i >= 0; i--)
    {
        if(input[i] == '/')
        {
            input[i] = 0;
            break;
        }
    }
    setDirectory(input);
}

int main()
{
    int t, n, m, result;
    scanf("%d", &t);
    for(int i = 1; i <= t; i++)
    {
        scanf("%d %d", &n, &m);
        
        result = 0;
        directory.clear();

        char input[256];
        for(int i = 0; i < n; i++)
        {
            scanf("%s", input);
            setDirectory(input);
        }
        int initsize = directory.size();
        for(int i = 0; i < m; i++)
        {
            scanf("%s", input);
            setDirectory(input);
        }
        printf("Case #%d: %d\n", i, directory.size()-initsize);
    }
    return 0;
}
