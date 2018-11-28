#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector <vector<int> > C;
vector <vector<bool> > O;

void initsets()
{
    C.clear();
    O.clear();
    vector <int> a(26,0);
    vector <bool> b(26,false);
    C.insert(C.begin(),26,a);
    O.insert(O.begin(),26,b);
}

void setrule1(string str)
{
    C[str[0]-'A'][str[1]-'A']=str[2]-'A'+1;
    C[str[1]-'A'][str[0]-'A']=str[2]-'A'+1;
}

void setrule2(string str)
{
    O[str[0]-'A'][str[1]-'A']=true;
    O[str[1]-'A'][str[0]-'A']=true;
}

void printline(int n, vector<char> A)
{
    cout<< "Case #"<<n+1<< ": [";
    for (int i=0;i<A.size();i++)
    {
        if (i==0) cout << A[i];
        else cout << ", " << A[i];
    }
    cout<< "]\n";
}

bool checkrule1(char ch,vector<char> str)
{
    if (str.size()==0) return false;
    return C[ch-'A'][str[str.size()-1]-'A']>0;
}

bool checkrule2(char ch,vector<char> str)
{
    for (int i=0;i<str.size();i++)
    {
        if (O[ch-'A'][str[i]-'A'])
            return true;
    }
    return false;
}

vector <char> solve(string str)
{
    vector<char> ans(1,str[0]);
    char tempc;
    for (int i=1;i<str.size();i++)
    {
        if (checkrule1(str[i],ans))
        {
            tempc=ans[ans.size()-1];
            ans.pop_back();
            ans.push_back('A'+C[tempc-'A'][str[i]-'A']-1);
        } else if (checkrule2(str[i],ans))
        {
            ans.clear();
        } else
        {
            ans.push_back(str[i]);
        }
    }
    return ans;
}            

int main()
{
    int T;
    cin >> T;
    int c, d,n;
    string str;
    vector<char> ans;

    for (int i=0; i< T; i++)
    {
        initsets();
        cin >> c;
        for (int j=0;j<c;j++)
        {
            cin >> str;        
            setrule1(str);
        }
        cin >> d;
        for (int j=0;j<d;j++)
        {
            cin >> str;
            setrule2(str);
        }
        cin >> n;
        cin >> str;
        ans = solve(str);
        printline(i,ans);
    }
    return 0;
}
