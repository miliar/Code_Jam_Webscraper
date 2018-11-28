#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

int main()
{
  int T;
  cin>>T;
  for(int zz=1;zz<=T;zz++)
  {
    int C,D,N;
    map< pair<char,char>,char > comb;
    set< pair<char,char> > ops;
    cin>>C;
    for(int i=0;i<C;i++)
    {
      string in;
      cin>>in;
      comb[make_pair(in[0],in[1])]=in[2];
    }
    cin>>D;
    for(int i=0;i<D;i++)
    {
      string in;
      cin>>in;
      ops.insert(make_pair(in[0],in[1]));
    }
    cin>>N;
    vector<char> lst;
    string in;
    cin>>in;
    out:
    for(int i=0;i<N;i++)
    {
      bool b=true;
      if(!lst.empty())
      {
	map< pair<char,char>,char >::iterator it=comb.find(make_pair(lst.back(),in[i]));
	if(it==comb.end()) it=comb.find(make_pair(in[i],lst.back()));
	if(it!=comb.end())
	{
	  lst.pop_back();
	  lst.push_back(it->second);
	  continue;
	}
	
	for(int j=0;j<lst.size();j++)
	{
	  set< pair<char,char> >::iterator itop=ops.find(make_pair(in[i],lst[j]));
	  if(itop==ops.end()) itop=ops.find(make_pair(lst[j],in[i]));
	  if(itop!=ops.end()){
	    lst.clear();
	    b=false;
	    break;
	  }
	}
      }
      if(b)
	lst.push_back(in[i]);
    }
    
    cout<<"Case #"<<zz<<": [";
    if(lst.empty())
      cout<<"]"<<endl;
    else
    {
      cout<<lst[0];
      for(int i=1;i<lst.size();i++)
	cout<<", "<<lst[i];
      cout<<"]"<<endl;
    }
  }
  return 0;
}

