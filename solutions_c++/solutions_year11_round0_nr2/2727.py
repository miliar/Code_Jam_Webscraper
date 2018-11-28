#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
string check_comb(string str,string arr)
{
    int len=str.size();
    if((str[len-1]==arr[0] && str[len-2]==arr[1])||(str[len-1]==arr[1] && str[len-2]==arr[0]))
    {
        str.erase(len-2,2);
        str.push_back(arr[2]);
    }
    return str;
}
string check_opp(string str,string arr)
{
    bool status[2]={false,false};
    for(int i=0;i<str.size();i++)
    {
        if(str[i]==arr[0] && !status[0]){status[0]=true;continue;}
        if(str[i]==arr[1] && !status[1]){status[1]=true;}
    }
    if(status[0]&&status[1]) str.erase();
    return str;
}
string combine(string str,vector<string>arr)
{
    if(str.size()<2 || arr.size()==0) return str;
    for(int i=0;i<arr.size();i++)
    {
        string tmp=check_comb(str,arr[i]);
        if(tmp!=str) return tmp;
    }
    return str;
}
string oppose(string str,vector<string>arr)
{
    if(str.size()<2 || arr.size()==0) return str;
    for(int i=0;i<arr.size();i++)
    {
        string tmp=check_opp(str,arr[i]);
        if(tmp!=str) return tmp;
    }
    return str;
}
int main()
{
    //freopen("Prob_B_Small2.in","r",stdin);
    //freopen("Prob_B_Small2.out","w",stdout);
    freopen("Prob_B_Large.in","r",stdin);
    freopen("Prob_B_Large.out","w",stdout);
    int times,count=0;
    cin>>times;getchar();
    while(times--)
    {
        int cnt1,cnt2,cnt3;
        vector<string> comb,opp;
        string str,ans="[",tmp;
        cin>>cnt1;
        for(int i=0;i<cnt1;i++){cin>>tmp;comb.push_back(tmp);}
        cin>>cnt2;
        for(int i=0;i<cnt2;i++){cin>>tmp;opp.push_back(tmp);}
        cin>>cnt3;cin>>str;tmp.clear();
        for(int i=0;i<cnt3;i++)
        {
            tmp+=str[i];
            tmp=combine(tmp,comb);
            tmp=oppose(tmp,opp);
        }
        for(int i=0;i<tmp.size();i++) ans=ans+tmp[i]+", ";
        if(ans.size()>3)ans.erase(ans.size()-2);ans+="]";
        cout<<"Case #"<<++count<<": "<<ans<<endl;
    }
    return 0;
}
