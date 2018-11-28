#include <iostream>
#include <string>
using namespace std;

int main () {
  string a, b;
  char m[26];
  int m2[26];  
  int i,j;
  for(i=0;i<26;i++) 
    {
      m2[i]=0;
      m[i] = '\0';
    }
  m[0]='y';
  m['o'-'a']='e';
  m['z'-'a']='q';
  m2['y'-'a']=m2['e'-'a']=m2['q'-'a']=1;
  a = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
  a.append("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
  a.append("de kr kd eoya kw aej tysr re ujdr lkgc jv");
  b = "our language is impossible to understand";
  b.append("there are twenty six factorial possibilities");
  b.append("so it is okay if you want to just give up");
  for(i=0;i<a.size();i++)
    if(a[i]>='a' && a[i]<='z') {
      m2[b[i]-'a']=1;
      m[a[i]-'a']=b[i];
    }
  for(i=0;i<26;i++) 
    if(m[i]=='\0') {
      for(j=0;j<26;j++)
	if(m2[j]==0) {
	  m[i]=j+'a';
	  break;
	}
      break;
    }
  int t;
  cin>>t;
  getline(cin, a);
  for(j=0;j<t;j++) {
    string g;
    getline(cin, g);
    for(i=0;i<g.size();i++) 
      if(g[i]>='a' && g[i]<='z') 
	g[i]=m[g[i]-'a'];
    cout<<"Case #"<<j+1<<": "<<g<<"\n";
  }
  return 0;
}
