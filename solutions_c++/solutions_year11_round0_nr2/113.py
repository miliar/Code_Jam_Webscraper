#include <stdio.h>
#include <math.h>
#include <map>
#include <set>
#include <iostream>
#include <string>
using namespace std;
int C,D;
int main()
{
  int T;
  scanf("%d",&T);
  for(int t=1;t<=T;t++)
    {
      map<pair<int,int>,int> Comb;
      set<pair<int,int> > Del;
      cin>>C;
      for(int i=0;i<C;i++)
	{
	  string tmp;
	  cin>>tmp;
	  Comb[make_pair(tmp[0],tmp[1])]=tmp[2];
	  Comb[make_pair(tmp[1],tmp[0])]=tmp[2];
	}
      cin>>D;
      for(int i=0;i<D;i++)
	{
	  string tmp;
	  cin>>tmp;
	  Del.insert(make_pair(tmp[0],tmp[1]));
	  Del.insert(make_pair(tmp[1],tmp[0]));
	}
      int N;string word;
      cin>>N>>word;
      string answer="";
      for(int i=0;i<word.size();i++)
	{
	  if(answer.size()>0)
	    {
	      char lc=answer[answer.size()-1];
	      if(Comb.find(make_pair(lc,word[i]))!=Comb.end())
		{
		  answer[answer.size()-1]=Comb[make_pair(lc,word[i])];
		  continue;
		}
	    }
	  answer.push_back(word[i]);
	  for(int j=0;j<(int)answer.size()-1;j++)
	    if(Del.find(make_pair(answer[answer.size()-1],answer[j]))!=Del.end())
	      {
		answer="";
		break;
	      }
	}
      printf("Case #%d: ",t);
      printf("[");
      for(int i=0;i<(int)answer.size()-1;i++)
	printf("%c, ",answer[i]);
      if(answer.size()>0)
	printf("%c",answer[answer.size()-1]);
      printf("]\n");
    }
}
