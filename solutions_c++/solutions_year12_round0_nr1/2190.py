#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
string key ="yhesocvxduiglbkrztnwjpfmaq";
int main()
{
    //	freopen("D:\\GCJ 2012\\A-small-practice.in","r",stdin);freopen("D:\\GCJ 2012\\A-small-attempt0.out","w",stdout);
    	freopen("D:\\GCJ 2012\\A-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2012\\A-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\A-large.in","r",stdin);freopen("D:\\GCJ 2012\\A-large.out","w",stdout);
    int testcase;
    char flag[101];
    cin>>testcase;
    cin.getline(flag,101);
    char t[101];
    string t1;
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        gets(t);
        t1=t;
        printf("Case #%d: ",caseId);
        for(int i=0;i<t1.size();i++)
        {
            if(t1[i]>='a'&&t1[i]<='z')t1[i]=key[t1[i]-'a'];
            cout<<t1[i];
        }
        cout<<endl;        
    }
    return 0;
}