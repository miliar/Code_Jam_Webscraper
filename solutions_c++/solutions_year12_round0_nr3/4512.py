#include <iostream>
#include <sstream>
#include <set>
using namespace std;

int is_tran(int n, int low, int high);
int main()
{
    int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        int low, high;
        cin>>low>>high;
        int cnt = 0;
        
        for (int j = low; j <= high; j++)
        {
            int k = is_tran(j, low, high);
            cnt += k;
        }
        cout<<"Case #"<<i + 1<<": "<<cnt<<endl;
    }
    return 0;
}

int is_tran(int n, int low, int high)
{
    int res = 0;
    ostringstream os;
    os<<n;
    string s = os.str();
    set<int> close;
    for (int i = 1; i < s.size(); i++)
    {
        string news = s.substr(0, i);
        string sub = s.substr(i);
        sub = sub + news;
        if (sub[0] == '0') continue;
        istringstream is(sub);
        int cur;
        is>>cur;
        if (close.count(cur) != 0) continue;
        close.insert(cur);
        if (cur > n && cur <=high) res += 1;
    }
    return res;
}
