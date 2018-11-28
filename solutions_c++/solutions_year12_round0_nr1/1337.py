#include <fstream>
#include <cstring>
using namespace std;
string from1,from2,from3,to1,to2,to3,s;
char key[40];
int n,i,t,T;
int main()
{
    ifstream fi("translate.in");
    ofstream fo("translate.out");
    from1="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    from2="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    from3="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    to1="our language is impossible to understand";
    to2="there are twenty six factorial possibilities";
    to3="so it is okay if you want to just give up";
    n=from1.length();
    for(i=0;i<n;i++) if(from1[i]!=' ') key[from1[i]-'a']=to1[i];
    n=from2.length();
    for(i=0;i<n;i++) if(from2[i]!=' ') key[from2[i]-'a']=to2[i];
    n=from3.length();
    for(i=0;i<n;i++) if(from3[i]!=' ') key[from3[i]-'a']=to3[i];
    key['z'-'a']='q'; key['q'-'a']='z';
    fi>>T; getline(fi,s);
    for(t=1;t<=T;t++)
    {
        getline(fi,s); n=s.length();
        fo<<"Case #"<<t<<": ";
        for(i=0;i<n;i++) if(s[i]!=' ') fo<<key[s[i]-'a']; else fo<<' ';
        fo<<"\n";
    }
    return 0;
}
