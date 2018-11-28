#include <vector>
#include <algorithm>

#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <cmath>
using namespace std;
int key1[]={0,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10};
int key2[]={0,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,10,10};
int main()
{
    //	freopen("D:\\GCJ 2012\\B-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2012\\B-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\B-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2012\\B-small-attempt1.out","w",stdout);
    	freopen("D:\\GCJ 2012\\B-large.in","r",stdin);freopen("D:\\GCJ 2012\\B-large.out","w",stdout);
    int testcase;
    vector <int> res;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    int n,s,p;
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        cin>>n>>s>>p;
        res.clear();
        int t,asw=0;
        for(int i=0;i<n;i++){cin>>t;res.push_back(t);}
        sort(res.begin(),res.end());
        for(int i=n-1;i>=0;i--)
        {
            if(key1[res[i]]>=p)asw++;
            else if(key2[res[i]]>=p&&s>0){s--;asw++;}
        }
        printf("Case #%d: %d\n",caseId,asw);

    }
    return 0;
}