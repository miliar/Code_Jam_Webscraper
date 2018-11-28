#include <iostream>
#include <string>


using namespace std;
string s[6000];
int main()
{
 freopen("out","w",stdout);
 int k,n,m;
 cin >> k >> n >> m;
 for(int i=0; i<n; i++)cin >> s[i];
 string ss;
 for(int z=0; z<m; z++)
 {
  cin >> ss;
  int c=0;
  for(int j=0; j<n; j++)
  {
   int jj=0;
   bool b=1;
   for(int i=0; i<ss.length(); i++)
   {
    if(jj>=s[j].length())
    {
     b=0;
     break;
    }
    if(ss[i]==s[j][jj]){jj++;continue;}
    if(ss[i]!=s[j][jj]&&ss[i]!='('){b=0;break;}
    if(ss[i]=='(')
    {
     while(ss[++i]!=')')
     {
      if(ss[i]==s[j][jj])
      {
       jj++;
       while(ss[i+1]!=')')i++;
      }
     }
    }
   }
   if(jj<s[j].length())b=0;
   if(b){c++;}
  }
  cout << "Case #" << z+1 << ":" << " " << c << endl;
 }
}
