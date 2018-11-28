#include<iostream>
#include<vector>
#include<cstdio>
#include<map>

#define sz(c) (int)c.size()

using namespace std;

int main()
{
    freopen("B-small.in","r",stdin);
    freopen("B-small.out","w",stdout);
    int T;
    cin>>T;
    for(int t = 0; t < T; t++)
    {
        map<string,char> combine; 
        map<char,char> opposed;
        vector<char> list;
        int C,D,N;

        cin>>C;
        for(int i = 0; i < C; i++)
        {
            char b1, b2, b3;
            cin>>b1>>b2>>b3;
            string s;
            s = ""; s += b1; s += b2; combine[s] = b3;
            s = ""; s += b2; s += b1; combine[s] = b3;
        }
        cin>>D;
        for(int i = 0; i < D; i++)
        {
            char b1, b2;
            cin>>b1>>b2;
            opposed[b1] = b2;
            opposed[b2] = b1;
        }
        cin>>N;
        for(int i = 0; i < N; i++)
        {
            char c;
            cin>>c;
            int size = sz(list);
            if(size == 0)
            {
                list.push_back(c);
                continue;
            }
            char c2 = list[size - 1];
            string s = ""; s += c; s += c2;
            map<string,char>::iterator itr = combine.find(s);
            if(itr != combine.end())
            {
                list[size - 1] = itr->second;
                continue;
            }
            map<char,char>::iterator itr2 = opposed.find(c);
            if(itr2 != opposed.end())
            {
                bool found = false;
                for(int j = 0; j < size; j++)
                {
                   if(list[j] == itr2->second) 
                   {
                       found = true;
                       list.clear();
                       break;
                   }
                }
                if(found)
                    continue;
            }
            list.push_back(c);
        }
        cout<<"Case #"<<(t+1)<<": [";
        for(int i = 0; i < sz(list); i++)
        {
            cout<<list[i];
            if(i < sz(list) - 1)
                cout<<", ";
        }
        cout<<"]\n";
    }
}

