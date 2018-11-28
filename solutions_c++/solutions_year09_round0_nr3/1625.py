#include<iostream>
#include<cmath>
#include<cstdlib>
#include<vector>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

int count(string x,string t)
{
    if(x.size()<t.size()) return 0;
    if(t.size()==0) return 1;
    string::iterator it=x.begin();
    while(*it!=t[0])
    {
        ++it;
        if(it==x.end()) return 0;
    }
    return (count(string(it+1,x.end()),string(t.begin()+1,t.end()))%10000)+(count(string(it+1,x.end()),t)%10000);

}


void g(ifstream& myfile)
{
    ofstream m;
    m.open ("C-small-attempt0.out");
    string tar("welcome to code jam");
    if (myfile.is_open())
    {
        int num,c=0,ans;
            myfile>>num;
        while(c<num)
        {
            string s;
            getline(myfile,s);
            if(s.size()>0)
            {
            ans=count(s,tar)%10000;

            if(ans<10)
                m<<"Case #"<<c+1<<": "<<"000"<<ans<<endl;
            else if(ans<100)
                m<<"Case #"<<c+1<<": "<<"00"<<ans<<endl;
            else if(ans<1000)
                m<<"Case #"<<c+1<<": "<<"0"<<ans<<endl;
            else m<<"Case #"<<c+1<<": "<<ans<<endl;
            ++c;
            }
        }
        myfile.close();
        return;
    }
    else cout << "Unable to open file";
    return;
}


int main ()
{
    ifstream myfile ("C-small-attempt0.in");
    //ifstream myfile ("g2.in");
    g(myfile);

    return 0;
}

