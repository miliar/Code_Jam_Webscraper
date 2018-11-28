#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

//map <char,int> mymap1;
//vector <char> zv;
vector <char> resv;
//map <char,int> mymap2;
int t,ti,c,d,n;
char resz;

int cntd[1000];
bool let[30];

struct mys
{
    char a;
    char b;
    char c;
};
vector<mys> nmap1;
vector<mys> nmap2;
mys tps;

bool tru1(char ch1,char ch2)
{
    for(int i=0;i<nmap1.size();i++)
    {
        if(nmap1[i].a==ch1)
            if(nmap1[i].b==ch2)
        {
            resz=nmap1[i].c;
            return true;
        }
        if(nmap1[i].b==ch1)
            if(nmap1[i].a==ch2)
        {
            resz=nmap1[i].c;
            return true;
        }


    }
    return false;


}

bool tru2()
{
    char tc1=resv[resv.size()-1];
    for(int i=0;i<=resv.size()-2;i++)
    {
        char tc2=resv[i];
        for(int i=0;i<nmap2.size();i++)
        {
            if(nmap2[i].a==tc1)
             if(nmap2[i].b==tc2)
              return true;
            if(nmap2[i].b==tc1)
             if(nmap2[i].a==tc2)
              return true;
        }
    }
    return false;

}



int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);

    string st1;
    char ch1,ch2,ch3;
    cin>>t;
    for(ti=1;ti<=t;ti++)
    {
        nmap1.clear();
        //zv.clear();
        //zv.push_back('d');
        cin>>c;
        for(int i=1;i<=c;i++)
        {
            cin>>st1;
            //mymap1[st1[0]]=i;mymap1[st1[1]]=i;
            //zv.push_back(st1[2]);
            tps.a=st1[0];tps.b=st1[1];tps.c=st1[2];
            nmap1.push_back(tps);
        }
        cin>>d;
        nmap2.clear();
        for(int i=1;i<=d;i++)
        {
            cin>>st1;
            tps.a=st1[0];tps.b=st1[1];
            nmap2.push_back(tps);
        }
        resv.clear();
        cin>>n;
        cin>>st1;
        for(int i=0;i<n;i++)
        {
            //cin>>ch1;
            resv.push_back(st1[i]);
            if(resv.size()>1)
            {
                ch1=resv[resv.size()-1];
                ch2=resv[resv.size()-2];
                if(tru1(ch1,ch2))
                {
                  resv.pop_back();resv.pop_back();resv.push_back(resz);
                }
            }
             if(resv.size()>1)
                if(tru2()) resv.clear();
        }
        cout<<"Case #"<<ti<<": [";
        for(int i=1;i<resv.size();i++) cout<<resv[i-1]<<", ";
        if(resv.size()>0) cout<<resv[resv.size()-1];
        cout<<"]\n";
    }
    return 0;
}
