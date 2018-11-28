#include <iostream>
#include <string>
#include <vector>
using namespace std;

/*
int main()
{
  int casenum;
  
  int c =0;

  cin>>casenum;
  
  while(casenum--)
    {

      int enginenum;
      
      cin>>enginenum;
      
      vector<string>engines;
      vector<int>counts(enginenum,0);
      engines.reserve(enginenum);

      string s;

      getline(cin,s);

      while(enginenum!=0)
	{
	  enginenum--;
	  getline(cin,s);
	  engines.push_back(s);

	}

      int querynum;
      
      cin>>querynum;

      getline(cin,s);
      
      while(querynum--)
	{
	  getline(cin,s);
	  
	  for(int i=0;i<engines.size();++i)
	    {
	      if(engines[i]==s)
		{
		  counts[i]++;
		  break;
		}
	    }
	}//while
      
      vector<int>::iterator t = min_element(counts.begin(),counts.end());
      cout<<"Case #"<<++c<<": "<<*t<<endl;
    }
  
}
*/


int main()
{
  int casenum;

  int c =0;

  cin>>casenum;
  
  while(casenum--)
    {

      int enginenum;
      
      cin>>enginenum;
      
      vector<string>engines;
      vector<int>counts(enginenum,0);
      engines.reserve(enginenum);

      string s;

      getline(cin,s);

      while(enginenum!=0)
	{
	  enginenum--;
	  getline(cin,s);
	  engines.push_back(s);
	}

      int querynum;
      
      cin>>querynum;

      getline(cin,s);

      int cnt = 0;

      vector<bool>mark(engines.size(),false);
      int unmarked = engines.size();

      while(querynum--)
	{
	  getline(cin,s);
	  
	  for(int i=0;i<engines.size();++i)
	    {
	      if(engines[i]==s)
		{
		  if(mark[i]==false)
		    {
		      unmarked--;
		      		      
		      if(unmarked==0)
			{
			  cnt++;
			  unmarked = engines.size()-1;

			  for(int j=0;j<mark.size();++j)
			    mark[j]=false;

			  mark[i]=true;
			}
		      else
			{
			  mark[i] = true;
			}
		    }
		  break;
		}// find it
	    }
	}//while
      
      cout<<"Case #"<<++c<<": "<<cnt<<endl;
    }  
}
