#include <iostream>
#include <fstream>

using namespace std;

int main()
{
 ifstream in("A-small-attempt0.in");
 ofstream out("output.txt");
 int n;
 in>>n;
 char temp[2];
 in.getline(temp,2);
 char arr[26];
 char str1[300]= "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvzq";
 char str2[300]= "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upqz";
 for(int i=0;i<strlen(str1);i++)
 {
     arr[str1[i]-'a']=str2[i];        
         
 }/* 
 for(int i=0;i<26;i++)
 {
     cout<<arr[i]<<" "<<(char)('a'+i)<<endl;        
 }*/
 

 for(int x=1;x<=n;x++)
 {
         out<<"Case #"<<x<<": ";
         char s[200];
         in.getline(s,200);
         for(int i=0;i<strlen(s);i++)
         {
                 s[i]=arr[s[i]-'a'];        
         }
         out<<s<<endl;
                       
 }
 system("pause");   
    
    
}
