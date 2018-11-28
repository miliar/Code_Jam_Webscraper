#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
string de(string a,string b)
{
    string c(51,'0');
    for(int i=50;i>=0;i--)
    {
        if(a[i]<b[i]){c[i]=('0'+(10+int(a[i]-b[i])));a[i-1]=a[i-1]-1;}
        else {c[i]=('0'+(a[i]-b[i]));}
    }
    return c;
}
string GCD(string a,string b)
{
    string c(51,'0');
    while(a>=b&&b!=c)
    {
        a=de(a,b);
    }
    return (b==c)?a:GCD(b,a);
}
int main()
{
    	freopen("D:\\GCJ 2010\\B-small-attempt2.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt2.out","w",stdout);
   	//freopen("D:\\GCJ 2010\\B-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\B-small-attempt1.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\B-large.in","r",stdin);freopen("D:\\GCJ 2010\\B-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int n;
        string res[1001];
        string t;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>t;
            string t2((51-t.size()),'0');
            res[i]+=t2;res[i]+=t;
        }
        sort(res,res+n);
        printf("Case #%d: ",caseId);
        string k=de(res[1],res[0]);
        for(int i=1;i<n-1;i++)
        {
            k=GCD(k,de(res[i+1],res[1]));
        }
        while(res[0]>k)
        {
            res[0]=de(res[0],k);
        }
        string asw=de(k,res[0]);
        int t1=0;
        for(int i=0;i<51;i++)
        {
            if(asw[i]!='0')t1=1;
            if(t1==1)cout<<asw[i];
        }
        if(t1==0)cout<<'0';
        cout<<endl;
    }
    return 0;
}