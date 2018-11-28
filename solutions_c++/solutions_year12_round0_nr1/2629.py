#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
ifstream fin("A.in");
ofstream fout("A.out");
int mp[30];
int main()
{
    memset(mp,-1,sizeof(mp));
    string in,out;
    in="ejp mysljylc kd kxveddknmc re jsicpdrysi";
    out="our language is impossible to understand";
    for(int i=0;i<in.size();i++)
    {
      if(in[i]==' ')continue;
      mp[in[i]-'a']=out[i]-'a';
    }
    in="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
    out="there are twenty six factorial possibilities";
    for(int i=0;i<in.size();i++)
    {
      if(in[i]==' ')continue;
      mp[in[i]-'a']=out[i]-'a';
    }
    in="de kr kd eoya kw aej tysr re ujdr lkgc jv";
    out="so it is okay if you want to just give up";
    for(int i=0;i<in.size();i++)
    {
      if(in[i]==' ')continue;
      mp[in[i]-'a']=out[i]-'a';
    }
    /*for(int i=0;i<26;i++)
    {
        if(mp[i]==-1)
        fout<<"+++ "<<char(i+'a')<<endl;
    }*/
    mp['z'-'a']='q'-'a';
    mp['q'-'a']='z'-'a';
    int T;
    fin>>T;
    getline(fin,out);
    for(int c=1;c<=T;c++)
    {
       getline(fin,in);
       out=in;
       for(int i=0;i<in.size();i++)
       {
          if(in[i]==' ')
          continue;
          out[i]=char(mp[in[i]-'a']+'a');
       } 
       fout<<"Case #"<<c<<": "<<out<<endl;
    }
}
