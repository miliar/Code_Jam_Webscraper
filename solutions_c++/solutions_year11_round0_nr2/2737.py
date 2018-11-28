#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

int comb(char a,char b)
{
  return (a<<8) | b;
}


int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int i=0;i<cases;++i)
    {
      int C;
      in >> C;

      std::map<int,char> conv;
      bool opp[256][256];
      for (int x=0;x<256;++x)
	for (int y=0;y<256;++y)
	  opp[x][y]=0;

      for (int j=0;j<C;++j)
	{
	  string r;
	  in >> r;
	  conv.insert(std::pair<int,char>(comb(r[0],r[1]),r[2]));
	  conv.insert(std::pair<int,char>(comb(r[1],r[0]),r[2]));
	}

      int D;
      in >> D;
      
      for (int j=0;j<D;++j)
	{
	  string r;
	  in >> r;
	  opp[r[0]][r[1]]=1;
	  opp[r[1]][r[0]]=1;
	}

      int N;
      in >> N;
      string r;
      in >> r;

      string out;
      for (int j=0;j<N;++j)
	{
//	  std::cout << out << std::endl;
	  
	  bool done=false;
	  
	  if (out.size())
	    {
//	      std::cout << "c(" << out[out.size()-1] << r[j] << "=" << comb(out[out.size()-1],r[j]) << ")";
	      
	  std::map<int,char>::iterator it = conv.find(comb(out[out.size()-1],r[j]));
	  if (it != conv.end())
	    {
//	      std::cout << "r";
	      out[out.size()-1]=it->second;
	      done=true;
	      
	      continue;
	    }
	    }

	  if (done)
	    continue;
	  
	  for (int k='A';k<='Z';++k)
	    {
	      if (opp[r[j]][k])
		{
		  if (string::npos!=out.find(k))
		    {
//		      std::cout << "!";
		    out.clear();
		    done=true;
		    
		    break;
		    
		    }
		  
		}
	      
	    }

	  if (!done)
	    out.push_back(r[j]);
	}
      
      
      std::cout << "Case #" << i+1 << ": ";

      std::cout << "[";
      if (out.size())
      for (int j=0;j<out.size()-1;++j)
	{
	  std::cout << out[j] << ", ";
	}
      if (out.size())
	std::cout << out[out.size()-1];

      std::cout << "]";
      
      std::cout << std::endl;

    }
  return 0;
}
