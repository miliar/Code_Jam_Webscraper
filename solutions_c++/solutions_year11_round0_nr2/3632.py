#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>
#include <cctype>

using namespace std;

int main()
{
  int tc, c, d, n;
  cin>>tc;
  vector<string> op, comb;
  string inp;
  vector<char> res;
  string elem = "QWERASDF";
  for(int t=1; t<=tc; t++)
    {
      op.clear();
      comb.clear();
      res.clear();

      cout<<"Case #"<<t<<": ";
      cin>>c;
      string dum;
      for(int i=0; i<c; i++)
	{cin>>dum; comb.push_back(dum);}
      cin>>d;
      for(int i=0; i<d; i++)
	{cin>>dum; op.push_back(dum);}
      int dummy;
      cin>>dummy>>inp;

      for(int i=0; i<inp.size(); i++)
	{
	  inp[i] = toupper(inp[i]);
	  if(elem.find(inp[i])==string::npos)
	    continue;
	 
	  res.push_back(inp[i]);
	  if(res.size()<2)
	    continue;
	  
	  //combination
	  while(res.size()>=2)
	    {
	      //	      cout<<"w1"<<endl;
	      char ch1, ch2;
	      ch1 = res[res.size()-1];
	      ch2 = res[res.size()-2];
	      bool found=false;
	      for(int j=0; j<c; j++)
		{
		  if((comb[j][0] == ch1 && comb[j][1] == ch2) || (comb[j][0] == ch2 && comb[j][1] == ch1))
		    {
		      res.pop_back();		      
		      res.pop_back();
		      res.push_back(comb[j][2]);
		      found = true;
		      break;
		    }
		}
	      if(!found)
		break;
	    }

	  //opposition
	  for(char j = 0; res.size()>=2 && j<res.size(); j++)
	    {
	      //	      cout<<"w2"<<endl;
	      char ch1, ch2;
	      ch1 = res[j];
	      ch2 = res[res.size()-1];

	      for(int j=0; j<d; j++)
		{
		  if((op[j][0] == ch1 && op[j][1] == ch2) || (op[j][0] == ch2 && op[j][1] == ch1))
		    {
		      res.clear();
		      break;
		    }
		}
	    }

	}
      cout<< '[';
      for(int i=0; i<res.size(); i++)
	{
	  if(i!=0)
	    cout<<", ";
	  cout<<res[i];
	}
      cout<< ']' <<endl;

    }

  return 0;
}
