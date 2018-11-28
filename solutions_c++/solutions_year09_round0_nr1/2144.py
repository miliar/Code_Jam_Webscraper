#include<stdio.h>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

int main()
{
    int ccase;
    vector<string> A;
    vector<int> flag;
    string s,t;
    int L,D,N;
    int x,y,z;
    
    cin >> L >> D >> N;
    A.clear();
    flag.clear();
    for(x = 0;x < D;x++)
    {
        cin >> s;
        A.push_back(s);
        flag.push_back(0);
    }
    
    for(ccase = 1;ccase <= N;ccase++)
    {
        for(x = 0;x < D;x++)
            flag[x] = 0;
        
        cin >> s;
        z = 0;
        while(z < L)
        {
            if(s[0] == '(')
            {
                t = s.substr(0,s.find(")") + 1);
                s.erase(0,t.size());
            }
            else
            {
                t = s[0];
                s.erase(0,1);
            }
            //cout << t << " " << s << endl;
            
            if(t.size() > 1)
            {
                t.erase(0,1);
                t.erase(t.size() - 1,1);
            }
            
            for(x = 0;x < D;x++)
            {
                if(flag[x] == 0)
                {
                    flag[x] = 1;
                    for(y = 0;y < t.size();y++)
                    {
                        if(t[y] == A[x][z])
                        {
                            flag[x] = 0;
                            break;
                        }
                    }
                }
            }
            z++;
        }
        
        y = 0;
        for(x = 0;x < D;x++)
        {
            if(flag[x] == 0)
                y++;
        }
        
        cout << "Case #" << ccase << ": " << y << endl;
    }

    while(getchar()!=EOF);
    return 0;
}
