#include<stdio.h>
#include<algorithm>
#include<string>
#include<map>
#include<vector>
using namespace std;
#define pb push_back

FILE * in = fopen("in.in","r");
FILE * out = fopen("out.out","w");

int n , m , c;
vector<string> tt;
vector< vector<string> > arr;

int calc(vector<string> s)
{
    int i , a , ret = s.size() , sum;
    for(i=0;i<arr.size();i++)
    {
        sum = 0;
        for(a=0;a<arr[i].size() && a < s.size();a++)
        {
            if(arr[i][a] != s[a]) break;
            sum++;
        }
        ret = min(ret , (int)(s.size() - sum));
    }
    return ret;
}

vector<string> make(string s)
{
    vector<string> ret;
    ret.clear();
    string t = "";
    for(int i=1;i<=s.size();i++)
    {
        if(s[i] == '/' || i == s.size())
        {
            ret.pb(t);
            t = "";
            continue;
        }
        t += s[i];
    }
    return ret;
}

int main()
{
    int i , a , k , caseID = 0 , ret;
    char x[100000];
    fscanf(in,"%d",&k);
    vector<string> g;
    while(k--)
    {
        c++;
        fprintf(out,"Case #%d: ",++caseID);
        fscanf(in,"%d %d",&n,&m);
        arr.clear();
        for(i=0;i<n;i++)
        {
            fscanf(in,"%s",x);
            g = make(x);
            arr.pb(g);
        }
        ret = 0;
        for(i=0;i<m;i++)
        {
            fscanf(in,"%s",x);
            g = make(x);
            ret += calc(g);
            arr.pb(g);
        }
        fprintf(out,"%d\n",ret);
    }
    return 0;
}
