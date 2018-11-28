#include <iostream>
#include <sstream>
using namespace std;
#define rep(i,n) for(i=0;i<n;i++)
int main()
{
    int cases,k=0,i,flag=1;
    cin>>cases;
    char l[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
    string str;
    while(k<=cases)
    {
        getline(cin,str);
        string temp;
        stringstream ss(str);
        ss<<str;



        while(ss>>temp)
        {
            if(flag){cout<<"Case #"<<k<<": ";flag=0;}
            int n=temp.size();
            rep(i,n)
            {
                cout<<l[temp[i]-97];
            }
            cout<<" ";
        }
        if(!flag)cout<<endl;
        flag=1;

        k++;
    }
    return 0;
}
