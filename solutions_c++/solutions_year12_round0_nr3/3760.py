#include<iostream>
#include<cstdio>
#include<set>
#include<algorithm>
#include<sstream>
using namespace std;

int A , B;

int dig(int n)
{
    int ans = 0;
    while(n > 0)
    {
        n /= 10;
        ans ++;
    }
    return ans;
}

string rotate(string s)
{
    int n = s.size();
    char temp = s[n - 1];
    for(int i=n-1;i>=1;i--)
    {
        s[i] = s[i-1];
    }
    s[0] = temp;
    return s;
}

string toString(int n)
{
     string ans = "";
     while(n > 0)
     {
         ans += n % 10 + '0';
         n /= 10;
     }
     reverse(ans.begin() , ans.end());

    return ans;
}



int toInt(string s)
{
    int ans = 0;
    int sz = s.size();
    for(int i=0;i<sz;i++)
    {
        ans *= 10;
        ans += s[i] - '0';
    }
    return ans;
}


int findNumbers(int n)
{
    int cnt = 0;
    //if(n >= A && n<= B)cnt++;
    int sz = dig(n);
    int temp = n;
    set<int> st;

    string str = toString(n), myStr;

    for(int i=0;i<sz;i++)
    {
        myStr = rotate(str);
        int myInt = toInt(myStr);
        str = myStr;

        if(myInt >= A && myInt <= B && myInt > temp)
            st.insert(myInt);
    }

    set<int> :: iterator it ;
    for(it = st.begin() ;it != st.end() ;it ++)
        cnt++;

    return cnt;
}


int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);

    int testcase , caseNo = 1;
    cin>>testcase;
    while(testcase--)
    {
        cin>>A>>B;
        int ans = 0;
        for(int n=A;n<=B;n++)
        {
            ans += findNumbers(n);
        }
        printf("Case #%d: ",caseNo++);
        printf("%d\n",ans);
    }
    return 0;
}