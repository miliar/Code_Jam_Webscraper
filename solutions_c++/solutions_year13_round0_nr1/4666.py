#include <iostream>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    int t;
    cin>>t;

    ofstream cout("res.txt");
    for(int tt=0;tt<t;tt++)
    {
        bool b=false;
        cout<<"Case #"<<tt+1<<":";
        vector<string> v;
        for(int i=0;i<4;i++)
        {
            string s;
            cin>>s;
            v.push_back(s);
        }
        for(int i=0;i<4;i++)
        {
            string s;
            for(int j=0;j<4;j++)
            {
                s+=v[j][i];
            }
            v.push_back(s);
        }
        string d1,d2;
        for(int i=0;i<4;i++)
        {
            d1+=v[i][i];
            d2+=v[i][4-i-1];
        }
        v.push_back(d1);
        v.push_back(d2);
        for(int i=0;i<v.size();i++)
        {
            if(v[i]=="XXXX"||v[i]=="XXXT"||v[i]=="XTXX"||v[i]=="XXTX"||v[i]=="TXXX")
            {
                cout<<" X won"<<endl;
                b=true;
                break;
            }
            else if(v[i]=="OOOO"||v[i]=="OOOT"||v[i]=="OTOO"||v[i]=="OOTO"||v[i]=="TOOO")
            {
                cout<<" O won"<<endl;
                b=true;
                break;
            }
        }
        if(b)
            continue;
        b=false;
        for(int i=0;i<v.size();i++)
        {
            for(int j=0;j<4;j++)
            {
                if(v[i][j]=='.')
                {
                    cout<<" Game has not completed"<<endl;
                    b=true;
                    break;
                }
            }
            if(b)
                break;
        }
        if(!b)
            cout<<" Draw"<<endl;
    }
    return 0;
}
