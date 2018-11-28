#include<iostream>
using namespace std;
int main()
{
    string s=" abcdefghijklmnopqrstuvwxyz";
    string s1=" ynficwlbkuomxsevzpdrjgthaq";
    int n;
    cin>>n;
    int h=1;
    cin.ignore();
    while(n--)
    {
        string x,ans;
        ans="";
        getline(cin,x);
        size_t found;
        for(int i=0;i<x.length();i++)
        {
            found=s1.find(x[i]);
            ans.append(1,s[(int)found]);
        }
        cout<<"Case #"<<h++<<": "<<ans<<endl;
    }
    return 0;
}
