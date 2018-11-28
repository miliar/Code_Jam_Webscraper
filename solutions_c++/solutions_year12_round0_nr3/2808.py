#include<stdio.h>
#include<string.h>
#include <sstream>
#include<algorithm>
#include<map>
#include<iostream>
#include<vector>

using namespace std;

map<pair<int,int>, int> mp;

vector<pair<int, int> > v;

int main(void){

    for(int i = 1; i<=2000000; i++)
    {
            string str;
            stringstream s;

            s << i;
            str = s.str();
        //cout << str << endl;
            int sz = str.size();
            string tmp = "";

            for(int k = 0; k<sz - 1; k++)
            {
                tmp += str[k];

                string tmp1 = "";
                for(int j = k + 1; j<sz; j++)
                {
                    tmp1 += str[j];
                }

                string ans = tmp1 + tmp;
                stringstream ss;
                ss.str(ans);
                int a;
                ss >> a;

                if(a<=2000000 && a>i)
                {

                    pair<int, int > p = make_pair(i,a);
                    if(mp[p] != 1)
                    {
                        mp[p] = 1;
                        v.push_back(p);
                        //cout << a << endl;
                    }
                }
            }
    }
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    //printf("%d\n", v.size());
    int x, y;
    int T;
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int cnt = 0;
        scanf("%d%d",&x,&y);
        for(int i = 0; i<v.size(); i++)
        {
            if(v[i].first >= x && v[i].first <= y && v[i].second >= x && v[i].second <= y)
            {
                cnt++;
            }
            else if(v[i].first > y)
                break;
        }
        printf("Case #%d: %d\n",t + 1, cnt);
    }
    return 0;
}
