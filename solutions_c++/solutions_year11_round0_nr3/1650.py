#include<iostream>
#include<string>
#include<vector>
#include<cstdlib>
#include<cmath>

using namespace std;

string Hex(long num)
{
    string result="";
    long temp=num, re;
    while (temp>0)
    {
        re=temp%2;
        temp=temp/2;
        result+=(char)(re+48);
    }
    return result;
}

string addStr(string s1, string s2)
{
    int len=max(s1.size(),s2.size());
    while (s1.size()<len) s1+='0';
    while (s2.size()<len) s2+='0';
    
    string str="";
    for (int i=0; i<len; i++)
    {
        if (s1[i]==s2[i])
            str+="0";
        else if (s1[i]!=s2[i])
            str+="1";
    }
    return str;
}

int main()
{
    int t, count, n;
    cin >> t;
    count=0;
    bool T;
    long sum;
    vector<long> num;
    string result;
    while (count<t)
    {
        count++;
        T=true;
        sum=0;
        cin >> n;
        result="";
        num.assign(n,0);
        for (int i=0;i<n;i++)
        {
            cin >> num[i];
            sum+=num[i];
            result=addStr(result, Hex(num[i]));
        }    
        for (int i=0; i<result.size(); i++)
            if (result[i]=='1') 
            {
                T=false;
                break;
            }
        if (!T)
            cout << "Case #" << count << ": NO" << endl;
        else
        {
            long Min=num[0];
            for (int i=1; i<n; i++)
                Min = min(num[i], Min);
            cout << "Case #" << count << ": " << sum-Min << endl;
        }
    }
    
}
