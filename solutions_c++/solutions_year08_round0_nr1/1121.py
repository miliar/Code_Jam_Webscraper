#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>
#include <algorithm>
#include <map>
#include <list>
using namespace std;

int main()
{
//    fstream cin("sample.in");
//    fstream cin("small.in");
//    fstream cin("small1.in");
    int n;
    cin >> n;
    for(int i=1; i<=n; i++)
    {
        //input
        vector<string> seng;
        set<string> sets;
        int s;
        cin >> s;
        cin.ignore();
        while(s--)
        {
            string temp;
            getline(cin, temp);
            seng.push_back(temp);
            sets.insert(temp);
        }
        vector<string> que;
        set<string> setq;
        int q;
        cin >> q;
        cin.ignore();
        while(q--)
        {
            string temp;
            getline(cin, temp);
            que.push_back(temp);
            setq.insert(temp);
        }
        //count
        int cnt = 0;
        if(setq.size() < sets.size())
        {
            cnt = 0;
        }
        else
        {
            //init
            list<string> base_token,token;
            for(set<string>::iterator it = setq.begin(); it != setq.end(); it++)
            {
                base_token.push_back(*it);
            }
            cnt = 0;
            string nil = "nil";
            string temp = nil;
            for(vector<string>::iterator it = que.begin(); it != que.end(); it++)
            {
                if(token.empty())
                {
                    token = base_token;
                    //if(temp != nil)
                    //{
                    //    token.erase(find(token.begin(), token.end(), temp));
                    //}
                    token.erase(find(token.begin(), token.end(), *it));
                    cnt++;
                }
                list<string>::iterator tokenIt = find(token.begin(), token.end(), *it);
                if(tokenIt != token.end())
                {
                    token.erase(tokenIt);
                }
                //if(token.size() == 1)
                //    temp = *token.begin();
                if(token.empty())
                {
                    token = base_token;
                    //if(temp != nil)
                    //{
                    //    token.erase(find(token.begin(), token.end(), temp));
                    //}
                    token.erase(find(token.begin(), token.end(), *it));
                    cnt++;
                }
            }
        }
        //output
        string Case = "Case #";
        if(cnt == 0)
            cout << Case << i << ": " << 0 << endl;
        else
            cout << Case << i << ": " << cnt-1 << endl;
    }

    return 0;
}