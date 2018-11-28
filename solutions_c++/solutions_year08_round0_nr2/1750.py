#include<fstream>
#include<iostream>
#include<map>
#include<vector>
#include<cmath>
#include<string>
#include<algorithm>
#include<sstream>
using namespace std;

struct P
{
    int tim;
    int dir;    
};

int con(string s)
{
    stringstream ss;
    ss<<s;
    int ret;
    ss>>ret;
    return ret;    
}

bool cmp(const P &a,const P &b)
{
    if(a.tim!=b.tim)    
        return a.tim<b.tim;
    if(a.dir!=b.dir) 
    {
     if(a.dir==-2)
      return true;
     if(b.dir==-2)
      return false;
      if(a.dir==1)
       return true;
      if(b.dir==1)
      return false;
      if(a.dir==-1)
       return true;
       if(b.dir==-1)
       return false;
    }
    return true;
}

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("c:\\data\\B-small-attempt2.in");
    fout.open("c:\\data\\bs.txt");
    int t;
    fin>>t;
    int ta,tu,tb;
    string temp;
    for(int cas=1;cas<=t;++cas)
    {
        fin>>tu;
        fin>>ta>>tb;
        vector< P > a;
        for(int i=0;i<ta;++i)
        {
            fin>>temp;
            int te=con(temp.substr(0,2))*60+con(temp.substr(3,2));
            P p;
            p.tim=te;
            p.dir=1;
            a.push_back(p);
            fin>>temp;
            te=con(temp.substr(0,2))*60+con(temp.substr(3,2))+tu;
            p.tim=te;
            p.dir=-1;
            a.push_back(p);            
        }
        for(int i=0;i<tb;++i)
        {
            fin>>temp;
            int te=con(temp.substr(0,2))*60+con(temp.substr(3,2));
            P p;
            p.tim=te;
            p.dir=2;
            a.push_back(p);
            fin>>temp;
            te=con(temp.substr(0,2))*60+con(temp.substr(3,2))+tu;
            p.tim=te;
            p.dir=-2;
            a.push_back(p);
        }
        int xa=0,xb=0,na=0,nb=0;
        sort(a.begin(),a.end(),cmp);
        for(int i=0;i<int(a.size());++i)
        {
            if(a[i].dir<0)
            {
                if(a[i].dir==-2)
                 xa++;
                else 
                 xb++;
            }
            else
            {
                if(a[i].dir==1)
                {
                 if(xa>0)xa--;
                 else na++;   
                }
                else
                {
                 if(xb>0)xb--;
                 else nb++;   
                }
            }
        }
        fout<<"Case #"<<cas<<": "<<na<<" "<<nb<<endl;
    }
    return 0;    
}
