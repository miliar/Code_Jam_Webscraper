#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <vector>

using namespace std;

map<string, string> ma;
vector<int> ve[300];
set<char> se;

int main(void)
{
    freopen("D:/B-small-attempt2.in", "r", stdin);
    freopen("D:/testb.out", "w", stdout);
    int c, d, n, t;
    scanf("%d", &t);
    int ca = 0;
    while(t--)
    {
        scanf("%d", &c);
        ma.clear();
        string temp;
        for(int i = 0; i < 300; ++i)
        {
            ve[i].clear();
        }
        for(int i = 0; i < c; ++i)
        {
            cin >> temp;
            string now1, now2, now3;
            now1 = temp.substr(0, 2);
            now2 = temp.substr(2, 1);
            ma[now1] = now2;
            for(int j = now1.length() - 1; j >= 0; --j)
            {
                now3.push_back(now1[j]);
            }
            ma[now3] = now2;
        }
        se.clear();
        scanf("%d", &d);
        for(int i = 0; i < d; ++i)
        {
            cin >> temp;
            /*hash[temp[0]] = temp[1];
            hash[temp[1]] = temp[0];*/
            ve[temp[0]].push_back(temp[1]);
            ve[temp[1]].push_back(temp[0]);
            se.insert(temp[0]);
            se.insert(temp[1]);
        }
        scanf("%d", &n);
        string str;
        cin >> str;
        for(int i = 0; i < str.length(); )
        {
   //         printf("%d>>", i);
            string now = str.substr(i, 2);
    //        cout << now<< "]]";
            int flag = 0;
            if(se.find(str[i]) != se.end())
            {
                for(int j = i - 1; j >= 0; --j)
                {
                    vector<int>::iterator iter;
                    for(iter = ve[str[i]].begin(); iter != ve[str[i]].end(); ++iter)
                    {
           //             printf("-");
                        if(str[j] == *iter)
                        {
                            str.erase(0, i + 1);
               //             cout << str << "||";
                            i = 0;
                            flag = 1;
                            break;
                        }
                    }
                    if(flag)
                        break;
                }
            }
            if(flag)
            {
                continue;
            }
            if(i != str.length() -1)
            {
                if(ma.find(now) != ma.end())
                {
         //           printf("+");
                    str.replace(i, 2, ma[now]);
                }
                else
                {
                }
            }
      //      cout << str << ">>";
            i++;
        }
   //     cout << str << endl;
        printf("Case #%d: ", ++ca);
        if(str.length() == 0)
            printf("[]");
        else if(str.length() == 1)
        {
            printf("[%c]", str[0]);
        }
        else
        {
            for(int i = 0; i < str.length(); ++i)
            {
                if(i == 0)
                {
                    printf("[%c, ", str[i]);
                }
                else if(i == str.length() - 1)
                {
                    printf("%c]", str[i]);
                }
                else
                {
                    printf("%c, ", str[i]);
                }

            }
        }
        printf("\n");
    }
    return 0;
}