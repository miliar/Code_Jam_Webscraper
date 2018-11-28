#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
ifstream fin("in.txt");
ofstream fout("out.txt");

bool equal(char a,char b, const string& s)
{
   return ((s[0]==a)&&(s[1]==b))||((s[0]==b)&&(s[1]==a));
}
////////////
char combine(char a, char b,const vector<string>& vs)
{
   for(int i=0;i<vs.size();i++)
       if(equal(a,b,vs[i])) return vs[i][2]; 
   return 0;
}
bool oppose(char a,char b,const vector<string>& vs)
{
   for(int i=0;i<vs.size();i++)
       if(equal(a,b,vs[i])) return true;
   return false;
}
////////////
bool clear(const string& str,const vector<string>& vs)
{
   for(int i=0;i<str.length()-1;i++)
      if(oppose(str[i],str[str.length()-1],vs)) return true;
   return false;
}
int main()
{
   int T;
   fin>>T;
   for(int tt=0;tt<T;tt++)
   {
      vector<string> cmb,clr;
      string in;
      {
        int c,d,n;
        string str;
        fin>>c;
        for(int i=0;i<c;i++)
        {
           fin>>str;
           cmb.push_back(str);
        }
        fin>>d;
        for(int i=0;i<d;i++)
        {
           fin>>str;
           clr.push_back(str);
        }
        fin>>n;
        fin>>in;
      }
      
      string ans;
      ans=in[0];
      for(int i=1;i<in.length();i++)
      {
         char chr=combine(ans[ans.length()-1],in[i],cmb);
         if(chr)
         {
            ans[ans.length()-1]=chr;
         }else
         if(clear(ans+in[i],clr))
         {
            ans="";
         }else
         ans+=in[i];
      }
      fout<<"Case #"<<tt+1<<": [";
      if(ans.length()>0) fout<<ans[0];
      for(int i=1;i<ans.length();i++)
        fout<<", "<<ans[i];
      fout<<"]"<<endl;
   }    
}
