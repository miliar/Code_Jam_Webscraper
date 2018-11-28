#include <stdio.h>
#include<map>
#include<set>
#include<deque>

class ch_pair
{
public:
  char a;
  char b;
  ch_pair(char _a, char _b)
  {
	if(_b < _a)
	  {
		a = _b;
		b = _a;
	  }
	else
	  {
		b = _b;
		a = _a;
	  }
  }
  bool operator==(const ch_pair& nextPair) const
  {
    if((a == nextPair.a && b == nextPair.b) || ((b == nextPair.a && a == nextPair.b)))
      {
	return true;
      }
    else
      {
	return false;
      }
  };

  bool operator <(const ch_pair &nextPair) const
  {
	char _a,_b;
	if(nextPair.b < nextPair.a)
	  {
		_a = nextPair.b;
		_b = nextPair.a;
	  }
	else
	  {
		_b = nextPair.b;
		_a = nextPair.a;
	  }
	if(a == _a)
	  {
		return (b < _b);
	  }
    return (a < _a);
  };
};

bool fncomp (char lhs, char rhs) 
{
  return lhs<rhs;
};

typedef std::set<char> setChar;
typedef std::pair<char,setChar> setPair;
typedef std::map<char,setChar> mapCharSetChar;
typedef mapCharSetChar::iterator mapcsetciter;

typedef std::map<ch_pair,char> mapCharPair;
typedef mapCharPair::iterator mapcpiter;

using namespace std;

int main()
{
  int nTests;
  scanf("%d",&nTests);
  for(int i=0;i<nTests;i++)
    {
      int c;int d;int n;
      mapCharPair vMapCharPair;
      mapCharSetChar vMapCharSetChar;
      std::multiset<char> chSet;;
      std::deque<char> chDeque;
      scanf("%d",&c);
      char str[100];
      for(int j=0;j<c;j++)
	{
	  char c3[4];
	  scanf("%s",c3);
	  ch_pair cPair(c3[0],c3[1]);
	  vMapCharPair.insert(make_pair(cPair,c3[2]));
	}
      scanf("%d",&d);
      for(int j=0;j<d;j++)
	{
	  char c3[3];
	  scanf("%s",c3);
	  mapcsetciter vMapcsetciter = vMapCharSetChar.find(c3[0]);
	  if(vMapcsetciter == vMapCharSetChar.end())
	    {
	      setChar tempsetChar;
	      tempsetChar.insert(c3[1]);
	      vMapCharSetChar.insert(make_pair(c3[0],tempsetChar));
	    }
	  else
	    {
	      setChar tempsetChar;
	      tempsetChar= vMapcsetciter->second;
	      tempsetChar.insert(c3[1]);
	      vMapCharSetChar.erase(vMapcsetciter);
	      vMapCharSetChar.insert(make_pair(c3[0],tempsetChar));
	    }
	  vMapcsetciter = vMapCharSetChar.find(c3[1]);
	  if(vMapcsetciter == vMapCharSetChar.end())
	    {
	      setChar tempsetChar;
	      tempsetChar.insert(c3[0]);
	      vMapCharSetChar.insert(make_pair(c3[1],tempsetChar));
	    }
	  else
	    {
	      setChar tempsetChar = vMapcsetciter->second;
	      tempsetChar.insert(c3[0]);
	      vMapCharSetChar.erase(vMapcsetciter);
	      vMapCharSetChar.insert(make_pair(c3[1],tempsetChar));
	    }
	}
      scanf("%d",&n);
      scanf("%s",str);
      //chDeque.push_front(str[0]);
      //chSet.insert(str[0]);
      for(int j=0;j<n;j++)
	{
	  char currChar = str[j];
	  if(chDeque.empty())
		{
		  chDeque.push_front(currChar);
	      chSet.insert(currChar);
		  continue;
		}
	  ch_pair pair1(chDeque.front(),str[j]);
	  mapcpiter iter=vMapCharPair.find(pair1);
	  if(iter!=vMapCharPair.end())
	    {
	      char replacement=iter->second;
	      char removal = chDeque.front();
		  chDeque.pop_front();
	      chDeque.push_front(replacement);
	      multiset<char>::iterator chIter=chSet.find(removal);
	      chSet.erase(chIter);
	      continue;
   	    }
	  bool clear=false;
	  mapcsetciter vMapcpiter = vMapCharSetChar.find(currChar);
	  if(vMapcpiter!=vMapCharSetChar.end())
		{
		  set<char> tempSet = vMapcpiter->second; 
		  set<char>::iterator chSetIter = tempSet.begin();
	  
		  for(;chSetIter!=tempSet.end();chSetIter++)
			{
			  if(chSet.find(*chSetIter)!=chSet.end())
				{
				  chDeque.clear();
				  chSet.clear();
				  clear=true; 
				  break;
				}
			}
		}
	  if(clear == false)
	    {
	      chDeque.push_front(currChar);
	      chSet.insert(currChar);
	    }
	}
      printf("Case #%d: [",i+1);
      if(chDeque.empty())
	{
	  printf("]\n");
	  continue;
	}
      while(chDeque.size() > 1) 
	{
	  printf("%c, ", chDeque.back());
	  chDeque.pop_back();
	}
      printf("%c]\n",chDeque.back());
	  fflush(stdout);
    }
}

