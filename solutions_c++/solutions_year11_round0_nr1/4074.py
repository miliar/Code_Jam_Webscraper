#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
  int n, tc,pos;
  char ch;
  vector<int> O, B;
  vector<char> all;
  cin>>tc;
  for(int t=1; t<=tc; t++)
    {
      cout<<"Case #"<<t<<": ";
      cin>>n;
      all.clear();
      O.clear();
      B.clear();
      for(int i=0; i<n; i++)
	{
	  cin>>ch>>pos;
	  all.push_back(ch);
	  if(ch=='O')
	    O.push_back(pos);
	  else
	    B.push_back(pos);
	}
      int O_pos = 1;
      int B_pos = 1;
      int O_i=0, B_i=0;
      int res = 0;
      for(int i=0; i<all.size(); i++)
	{
	  if(all[i]=='O')
	    {
	      int steps = abs(O_pos - O[O_i]) + 1;
	      if( B_i < B.size() )
		{
		  if( abs(B_pos - B[B_i]) <= steps )
		    B_pos = B[B_i];
		  else 
		    B_pos += (B[B_i]-B_pos>0?1:-1)*steps;
		}
	      O_pos = O[O_i++];
	      res += steps;
	      //	      cout<<"OOO "<<steps<<B_pos<<" "<<O_pos<<endl;
	    }
	  else
	    {
	      int steps = abs(B_pos - B[B_i]) + 1;
	      if( O_i < O.size() )
		{
		  if( abs(O_pos - O[O_i]) <= steps )
		    O_pos = O[O_i];
		  else 
		    O_pos += (O[O_i]-O_pos>0?1:-1)*steps;
		}
	      B_pos = B[B_i++];
	      res += steps;
	      //	      cout<<"BBB "<<steps<<B_pos<<" "<<O_pos<<endl;
	    }
	}
      cout<<res<<endl;
    }

  return 0;
}
