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
    	freopen("D:\\GCJ 2012\\D-small-attempt0.in","r",stdin);freopen("D:\\GCJ 2012\\D-small-attempt0.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\D-small-attempt1.in","r",stdin);freopen("D:\\GCJ 2012\\D-small-attempt1.out","w",stdout);
    //	freopen("D:\\GCJ 2012\\D-large.in","r",stdin);freopen("D:\\GCJ 2012\\D-large.out","w",stdout);
    int testcase;
    char flag[100];
    cin>>testcase;
    cin.getline(flag,100);
    int H,W,d;
    vector <string> a;
    vector <double> res;
    for (int caseId=1;caseId<=testcase;caseId++)
    {
        cin>>H>>W>>d;
        string str;
        str.clear();
        a.clear();
        res.clear();
        int U,D,L,R,asw=0;
        for(int i=0;i<H;i++){cin>>str;a.push_back(str);}
        for(int i=0;i<H;i++)
        {
            for(int j=0;j<W;j++)
            {
                if(a[i][j]=='X')
                {
                    U=i+i-1;
                    D=2*(H-i)-3;
                    L=j+j-1;
                    R=2*(W-j)-3;
                }
            }
        }
        //1
        for(int i=0;i<=d;)
        {
            i+=U;
            for(int j=0;j<=d;)
            {
                j+=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j+=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
            i+=D;
            for(int j=0;j<=d;)
            {
                j+=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j+=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
        }
        if(res.size()>1)
        {
            sort(res.begin(),res.end());
            asw++;
            for(int i=1;i<res.size();i++)if(res[i]!=res[i-1])asw++;
        }
        else asw+=res.size();
        res.clear();
        //2
        for(int i=0;-i<=d;)
        {
            i-=D;
            for(int j=0;j<=d;)
            {
                j+=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j+=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
            i-=U;
            for(int j=0;j<=d;)
            {
                j+=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j+=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
        }
        
        if(res.size()>1)
        {
            sort(res.begin(),res.end());
            asw++;
            for(int i=1;i<res.size();i++)if(res[i]!=res[i-1])asw++;
        }
        else asw+=res.size();
        res.clear();
        //3
        for(int i=0;-i<=d;)
        {
            i-=D;
            for(int j=0;-j<=d;)
            {
                j-=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j-=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
            i-=U;
            for(int j=0;-j<=d;)
            {
                j-=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j-=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
        }
        if(res.size()>1)
        {
            sort(res.begin(),res.end());
            asw++;
            for(int i=1;i<res.size();i++)if(res[i]!=res[i-1])asw++;
        }
        else asw+=res.size();
        res.clear();
        //4
        for(int i=0;i<=d;)
        {
            i+=U;
            for(int j=0;-j<=d;)
            {
                j-=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j-=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
            i+=D;
            for(int j=0;-j<=d;)
            {
                j-=L;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
                j-=R;
                if(i*i+j*j<=d*d)res.push_back(double(j)/double(i));
            }
        }
        if(res.size()>1)
        {
            sort(res.begin(),res.end());
            asw++;
            for(int i=1;i<res.size();i++)if(res[i]!=res[i-1])asw++;
        }
        else asw+=res.size();
        if(U<=d)asw++;
        if(R<=d)asw++;
        if(L<=d)asw++;
        if(D<=d)asw++;
        printf("Case #%d: ",caseId);
        cout<<asw<<endl;

    }
    return 0;
}