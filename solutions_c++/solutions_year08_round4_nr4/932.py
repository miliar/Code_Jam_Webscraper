#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <cmath>
using namespace std;
string res;

int group(string s)
{
    int count = 1;
    for(int i=1; i<s.length(); i++) if(s[i] != s[i-1]) count ++;
    return count;
}

int calc(string s, string query)
{
    int k = query.length();
    int left, right;
    left = 0, right = k-1;
    for(int left = 0, right = k-1; right < s.length(); left = right+1, right = left + (k-1))
    {
        string backup = "";
        for(int i=left; i<=right; i++) backup += s[i];
        for(int i=0, j=left; i<k; i++, j++) s[j] = backup[query[i]-'0'-1];
    }    
    res = s;
    return group(s);
}

int main()
{
    freopen("D.in","r",stdin); freopen("out.txt","w",stdout);
    int test;
    scanf("%d", &test);
    for(int t=1; t<=test; t++)
    {
        int k;
        cin >> k;
        string s;
        cin >> s;
        
        string query = "";
        for(int i=1; i<=k; i++) query += i+'0';
        
        int min = -1;
        string result, perm;
        do
        {
            int r = calc(s,query);
            if(min == -1 || min > r) min = r, result = res, perm = query;
            //cout << query << endl;
        }
        while(next_permutation(query.begin(), query.end()));
        
        
        printf("Case #%d: %d\n", t, min);
        //cout << result << endl;
        //cout << perm << endl;
    }
}
