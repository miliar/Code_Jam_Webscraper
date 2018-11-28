#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
  int n,t,na,nb,x,i,y,cntr;
  string input;
  vector <int> a,b;
  istringstream sin;
  getline(cin,input);
  sin.clear();
  sin.str(input);
  sin>>n;
  for(x=1;x<=n;x++)
    {
      a.clear();
      b.clear();
      getline(cin,input);
      sin.clear();
      sin.str(input);
      sin>>t;
      getline(cin,input);
      sin.clear();
      sin.str(input);
      sin>>na>>nb;
      //      cout<<na<<" "<<nb<<endl;
      for(i=0;i<na;i++)
	{
	  getline(cin,input);
	  a.push_back(((input[0]-'0')*600+(input[1]-'0')*60+(input[3]-'0')*10+input[4]-'0')*2+1);
	  b.push_back(((input[6]-'0')*600+(input[7]-'0')*60+(input[9]-'0')*10+input[10]-'0'+t)*2);
	}
      for(i=0;i<nb;i++)
	{
	  getline(cin,input);
	  b.push_back(((input[0]-'0')*600+(input[1]-'0')*60+(input[3]-'0')*10+input[4]-'0')*2+1);
	  a.push_back(((input[6]-'0')*600+(input[7]-'0')*60+(input[9]-'0')*10+input[10]-'0'+t)*2);	
  	}
      sort(a.begin(),a.end());
      sort(b.begin(),b.end());
      //     for(i=0;i<b.size();i++)
      //	cout<<b[i]<<" ";
      cntr=0,y=0;
      for(i=0;i<a.size();i++)
	{
	  if(a[i]%2)
	    {
	      if(cntr>0)
		cntr--;
	      else
		y++;
	    }
	  else
	    cntr++;
	}
      cout<<"Case #"<<x<<": "<<y<<" ";
      cntr=0,y=0;
      for(i=0;i<b.size();i++)
	{
	  if(b[i]%2)
	    {
	      if(cntr>0)
		cntr--;
	      else
		y++;
	    }
	  else
	    cntr++;
	}
      cout<<y<<"\n";
    }
  return 0;
}
