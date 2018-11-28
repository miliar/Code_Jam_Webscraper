#include <iostream>
#include <set>
#include <map>
#include <vector>

using namespace std;

typedef vector<int> VI;

void process(void)
{
    set<char> used;
    map<char,int> mapp;
    set<int> usenum;
    string str;
    cin >> str;
    for(int i=0;i<(int)str.size();i++) used.insert(str[i]);

    int siz = used.size();
    if(siz == 1) siz=2;

    long long ret = 0;
    for(int i=0;i<(int)str.size();i++)
    {
        ret *= (long long)siz;
        if(mapp.count(str[i]))
        {
            ret += mapp[str[i]];
        }
        else
        {
            if(i==0) 
            {
                mapp[str[i]] = 1;
                usenum.insert(1);
            }
            else
            {
                for(int j=0;j<siz;j++)
                {
                    if(usenum.count(j)) continue;
                    usenum.insert(j);
                    mapp[str[i]] = j;
                    break;
                }
            }
            ret += mapp[str[i]];
        }
    }
    cout << ret << endl;
}

int main(void)
{
    int N;
    cin >> N;
    for(int i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        process();
    }
}
