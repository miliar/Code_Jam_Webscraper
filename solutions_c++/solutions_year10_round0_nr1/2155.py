#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int main()
{
    //	freopen("D:\\GCJ 2010\\A-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2010\\A-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2010\\A-small-attempt1.out","w",stdout);
    	freopen("D:\\GCJ 2010\\A-large.in","r",stdin);freopen("D:\\GCJ 2010\\A-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        int a,b;
        cin>>a>>b;
        printf("Case #%d: ",caseId);
        a=(pow(2.0,a)-1);
        if((b|a)==b)cout<<"ON"<<endl;else cout<<"OFF"<<endl;   
    }
    return 0;
}