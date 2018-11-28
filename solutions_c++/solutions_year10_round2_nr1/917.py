#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <string>
#include <iostream>

using namespace std;

int main()
{
    int T;
    scanf("%d", &T);

    for (int test=1; test<=T; test++)
    {
        int N, M, Pjg, Ans=0;
        scanf("%d%d", &N, &M);
        vector<string> vecDir;
        while (N--)
        {
            char dir[105] = {};
            scanf("%s", dir);
            string temp="";
            
            Pjg = strlen(dir);
            for (int i=1; i<Pjg; i++)
            {
                if (dir[i]!='/')
                    temp+=dir[i];
                else
                {
                    if (vecDir.empty() || find(vecDir.begin(), vecDir.end(), temp)==vecDir.end())
                    {
                        //cout << temp << endl;
                        vecDir.push_back(temp);
                        temp = "";
                        i=0;
                    }
                    else
                        temp+=dir[i];
                }
            }
            if (vecDir.empty() || find(vecDir.begin(), vecDir.end(), temp)==vecDir.end())
                vecDir.push_back(temp);
        }

        while (M--)
        {
            char dir[105] = {};
            scanf("%s", dir);
            string temp="";
            
            Pjg = strlen(dir);
            for (int i=1; i<Pjg; i++)
            {
                if (dir[i]!='/')
                    temp+=dir[i];
                else
                {
                    if (vecDir.empty() || find(vecDir.begin(), vecDir.end(), temp)==vecDir.end())
                    {
                        //cout << temp << endl;
                        Ans++;
                        vecDir.push_back(temp);
                        temp = "";
                        i=0;
                    }
                    else
                        temp+=dir[i];
                }
            }
            if (vecDir.empty() || find(vecDir.begin(), vecDir.end(), temp)==vecDir.end())
            {
                Ans++;
                vecDir.push_back(temp);
            }
        }
        
        printf("Case #%d: %d\n", test, Ans);
    }
    
    return 0;
}
