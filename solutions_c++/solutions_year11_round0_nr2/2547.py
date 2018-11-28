#include <vector>
#include <string>
#include <iostream>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      string s;
      int C,i,j;
      cin>>C;
      char comb[26][26];
      int opp[26][26];
      for(i=0;i<26;i++)
	for(j=0;j<26;j++)
	  {
	    comb[i][j]=0;
	    opp[i][j]=0;
	  }
      for(i=0;i<C;i++)
	{
  	  cin>>s;
	  comb[s[0]-'A'][s[1]-'A']=comb[s[1]-'A'][s[0]-'A']=s[2];
	}
      cin>>C;
      for(i=0;i<C;i++)
	{
  	  cin>>s;
	  opp[s[0]-'A'][s[1]-'A']=opp[s[1]-'A'][s[0]-'A']=1;
	}
      cin>>C;
      cin>>s;
      char a[150];
      int last=-1;
      for(i=0;i<C;i++)
	{
	  if(last==-1)  
	    a[++last]=s[i];
	  else if(comb[s[i]-'A'][a[last]-'A'])
	    a[last]=comb[s[i]-'A'][a[last]-'A'];
	  else {
	    for(j=0;j<=last;j++)
	      if(opp[s[i]-'A'][a[j]-'A'])
		break;
	    if(j>last)
	      a[++last]=s[i];
	    else
	      last=-1;
	  }
	}
      cout<<"Case #"<<t<<": [";
      for(i=0;i<last;i++)
	cout<<a[i]<<", ";
      if(last!=-1)
	cout<<a[last];
      cout<<"]\n";
    }
  return 0;
}
