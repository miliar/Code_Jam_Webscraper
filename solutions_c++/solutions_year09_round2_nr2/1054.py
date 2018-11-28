#include <iostream>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <set>
#include <numeric>
using namespace std;

void g1A()
{
    ifstream fin ("2B.in");
    ofstream fout;
    fout.open ("2B.out");
    int num,c=0;
    fin>>num;
    while(c<num)
    {
        string s;

        fin>>s;
        int l=s.length();
        char max=s[l-1];
        string x;
        int i;
        for( i=l-1;i>=0;--i)
        {
            x.push_back(s[i]);
            if (s[i]>max) max=s[i];
            else if(s[i]<max) break;
        }
        for(int j=0;j<x.length();++j)
        {
            if(x[j]>s[i] &&x[j]<max) max=x[j];
        }
        ++c;
        sort(x.begin(),x.end());

        if (i==-1&&(max=='0'||s.length()==1)) {        char min;
        for(string::iterator k=x.begin();k<x.end();++k)
            if(*k!='0') {min=*k;x.erase(k); break;}
            fout<<"Case #"<<c<<": "<<min<<'0'<<x<<endl;continue;}
        if(i==-1) {fout<<"Case #"<<c<<": "<<x[0]<<'0'<<string(x.begin()+1,x.end())<<endl;continue;}



        fout<<"Case #"<<c<<": ";
        for(int k=0;k<i;++k)
            fout<<s[k];
        fout<<max;
        int count=0;
        for(int kk=0;kk<x.length();++kk)
        {
            if(count==0&&x[kk]==max) {count++;continue;}
            if(x[kk]!=max|| count>0) fout<<x[kk];
        }
        fout<<endl;
    }
    fout.close();
    fin.close();
    return;
}



int main ()
{
    g1A();
    return 0;
}

