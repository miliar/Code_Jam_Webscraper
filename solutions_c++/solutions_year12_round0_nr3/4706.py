#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<algorithm>
#include<cstring>
#include<sstream>
#include<fstream>
using namespace std;

int inArray(int val,int arr[])
{
    for(int i=0;i<10;i++)
    {
        if(val==arr[i])
        {
            return 0;
        }
    }
    return 1;
}

int cont(string a,string b)
{
    int count=0;
    int start,end;
    start=atoi(a.c_str());
    end=atoi(b.c_str());
    //ofstream my;
    //my.open("deb.txt");
    int arr[10];
    int in;
    for(int i=start;i<=end;i++)
    {
        stringstream out;
        out<<i;
        string s=out.str();
        int sz=s.size();
        in=0;
        for(int l=0;l<10;l++)
        {
            arr[l]=0;
        }
        for(int j=0;j<sz;j++)
        {
            string a,b;
            a=s.substr(j);
            //cout<<"val of a "<<a<<endl;
            b=s.substr(0,j);
            //cout<<"val of b "<<b<<endl;
            a+=b;
            //cout<<"outcome = "<<a<<endl;
            int val=atoi(a.c_str());
            if(val>i && val>=start && val<=end)
            {
                if(inArray(val,arr))
                {
                    //my<<"value for which count is incremented "<<val<<": "<<s<<endl;
                    count++;
                    arr[in++]=val;
                }

            }
        }
    }
    //my.close();
    return count;
}

int main()
{

    ofstream lout;
    lout.open("answer.txt");
    int t;
    cin>>t;
    string a,b;
    for(int i=0;i<t;i++)
    {
        cin>>a>>b;
        int res=cont(a,b);
        cout<<"Case #"<<i+1<<": "<<res<<endl;
        lout<<"Case #"<<i+1<<": "<<res<<endl;
    }
    lout.close();
    return 0;
}

