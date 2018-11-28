#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

const int MAXN = 10001;
string str[MAXN];
int mset[26][MAXN], rank[26][MAXN];
int T, N, M;
bool element[26][MAXN];

int findU(int a, int c)
{
    if(a != mset[c][a]) return mset[c][a] = findU(mset[c][a], c);
    return a;
}

void mUnion(int a, int b, int c)
{
    int pa = findU(a, c), pb = findU(b, c);
    if(rank[c][pa] > rank[c][pb])
    {
        mset[c][pb] = pa;
        rank[c][pa] += rank[c][pb];
    }
    else
    {
        mset[c][pa] = pb;
        rank[c][pb] += rank[c][pa];
    }
}

void uInit()
{
    for(int i = 0; i < N; i++)
        for(int j = 0; j < 26; j++)
            mset[j][i] = i, rank[j][i] = 1;
}

inline bool check(int a, int b, char c)
{
    if(str[a].size() != str[b].size()) return false;
    
    for(int i = 0; i < str[a].size(); i++)
        if((str[a][i]==c || str[b][i]==c) && str[a][i] != str[b][i])
            return false;
    return true;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("outb_s.txt", "w", stdout);
    cin>>T;
    
    for(int t = 1; T--; ++t)
    {
        cout<<"Case #"<<t<<":";
        cin>>N>>M;
        memset(element, false, sizeof(element));
        for(int i = 0; i < N; i++)
        {
            cin>>str[i];
            for(int j = 0; j < str[i].size(); j++)
                element[str[i][j]-'a'][i] = true;
        }
        uInit();
        
        for(int i = 0; i < N; i++)
            for(int j = 0; j < N; j++)
                for(int k = 0; k < 26; k++)
                    if(check(i, j, k+'a'))
                        mUnion(i, j, k);
        for(int i = 0; i < M; i++)
        {            
            int theMax = -1;
            string ans, gus;
            cin>>gus;
            
            for(int j = 0; j < N; j++)
            {
                vector <int> plist;
                int cnt = 0, res = 0;
                for(int k = 0; k < N; k++)
                    if(str[k].size() == str[j].size())
                        plist.push_back(k);
                
                for(int k = 0; k < 26; k++)
                    if(element[k][j])
                        ++cnt;
                                        
                for(int k = 0; k < gus.size(); k++)
                    {
                        if(cnt == 0) break;
                        int cho = gus[k]-'a';
                        bool flag = false;
                        for(int a = 0; a < plist.size(); a++)
                            if(element[cho][plist[a]])
                            {
                                flag = true;
                                break;
                            }
                        
                        if(!flag) continue;
                        for(int a = 0; a < plist.size(); )
                        {
                            if(findU(j, cho) != findU(plist[a], cho))
                            //if(!check(j, plist[a], gus[k]))                    
                            {
                                plist[a] = plist.back();
                                plist.pop_back();
                            }
                            else
                                ++a;
                        }
                        if(!element[cho][j])
                            ++res;
                        else
                            --cnt;
                    }
                if(res > theMax)
                    theMax = res, ans = str[j];
            }
            cout<<" "<<ans;
        }
        cout<<endl;
    }
    return 0;
}
