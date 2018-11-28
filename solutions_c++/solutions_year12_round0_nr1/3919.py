#include<fstream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
    ifstream in("A-small-attempt1.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    char d;
    in>>noskipws>>d;
    for(int i=0;i<T;i++)
    {
        out<<"Case #"<<i+1<<": ";
        char c;
        string a1="zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
        string a2="qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";
        while(in>>noskipws>>c)
        {
            if(c=='\n') break;
            for(int j=0;j<a1.size();j++)
            if(c==a1[j])
            {out<<a2[j];break;}
        }
        out<<endl;
    }
    return 0;
}
