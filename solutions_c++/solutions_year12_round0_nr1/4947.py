#include<iostream>
using namespace std;
int main()
{
 char map[26];
    string s="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
   string out="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"; 
   for(int i=0;i<s.length();i++)
   map[s[i]-'a']=out[i];
   
   
   map[25]='q';
   map['q'-'a']='z';
   //for(int i=0;i<26;i++)
   //cout<<(char)(i+'a')<<" "<<map[i]<<"\n";
   
   int t;
   cin>>t;
   cin.ignore();
   int abc=1;
   while(t--)
   {
   
   char in[200];
   cin.getline(in,200);
   cout<<"Case #"<<abc++<<": ";
   for(int i=0;in[i]!='\0';i++)
   if(in[i]!=' ')
         cout<<map[in[i]-'a'];
         else
         cout<<" ";
   cout<<"\n";
             
             
   }
   //system("pause");
   
return 0;    
}
