#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <math.h>
#include <map>

using namespace std;

int t, u,v;
int factor[10];
bool done[2000000];

int Recyc(int b, int len)
{
    stringstream str;
    string sta,stb;
    int cnt=0;
    int tm;
    string tmp="";
    str << b;
    getline(str,stb,' ');
    for (int i=1; i<len; i++)
    {
        tmp="";
        for (int j=stb.length()-i; j<=stb.length()-1; j++)
        {
            tmp+=stb[j];
        }
        for (int j=0; j<stb.length()-i; j++)
        {
            tmp+=stb[j];
        }
        tm=atoi(tmp.c_str());
        if (tm>=u && tm<=v && tmp[0]!=0 && b!=tm && !done[tm])
        {
            cnt++;
            //cout << b << " " << tmp << endl;
            done[tm]=true;
        }

    }
    if (b==123)
    {
        cout << "sün";
    }
    if (cnt>=2)
    {
        cnt++;
        return factor[cnt]/(factor[2]*factor[cnt-2]);
    }
    else
    {
        return cnt;
    }

}

int main()
{

    int digit, count;
    ifstream in("input.in");
    ofstream out("output.out");
    stringstream strm;
    map<char,int> digit1,digit2;
    map<char,int>::iterator it;
    bool ok;
    string stra,strb;
    in >> t;
    factor[0]=1;
    factor[1]=1;
    for (int i=1; i<=8; i++)
    {
        factor[i]=factor[i-1]*i;
    }
    for (int c=1; c<=t; c++)
    {
        count=0;
        for (int c2=u; c2<=v; c2++)
        {
            done[c2]=false;
        }
        in>>u;
        in>>v;
        digit=log10(u)+1;
        for (int c2=u; c2<=v; c2++)
        {
            if (!done[c2]) {count+=Recyc(c2,digit);}
            //cout  << c2 << ": " << Recyc(c2,digit) << endl;
        }
        out << "Case #" << c << ": " << count << endl;
    }
    u=1111;
    v=2222;
    cout << Recyc(1212,4);
    out.close();
}
