#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
using namespace std;

bool harm(long a, long b)
{
  if (a<b)
    return harm(b,a);

  return (a%b)==0;
}

vector<long> pfacs(long number)
{
  vector<long> ps;

  for(long i = 2; i <= number; i++) // Test for factors > 1
	 {
	   if (number % i == 0) // It is a factor > 1
		 {
			 bool prime = true;
			 for(long j = 2; j < i; j++) // Test for prime
			 {
				 if(i % j == 0) // It is not prime
					 prime = false;
			 }
			 if(prime)
			   {
			     while (number % i ==0)
			       {
				 
			     ps.push_back(i);
			     number/=i;
			     
			       }
			     
			     
			   }
			 
			 
		 }
	 }

  return ps;
}

void make_subset(vector<long> & dest, vector<long> & src_copy)
{
//  vector<long> src_copy=src;
  for (long i=0;i<dest.size();++i)
    {
      for (vector<long>::iterator it=src_copy.begin();it!=src_copy.end();++it)
	{
	  if (*it>dest[i])
	    break;
	  if (*it==dest[i])
	    {
	      src_copy.erase(it);
	      break;
	    }
	}
    }

  dest.insert(dest.end(),src_copy.begin(),src_copy.end());
  sort(dest.begin(),dest.end());
  
     
}



int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int case_=0;case_<cases;++case_)
    {
      long N,L,H;
      in >> N >> L >> H;
      vector<long> fr;
      for (long i=0;i<N;++i)
	{
	  long t;
	  in >> t;
	  fr.push_back(t);
	  
	  
	}

      bool fail=true;
      long me;
      
/*
      for (int i=1;i<100;++i)
	{
	  cout << i << ":";
	  vector<long> ps=pfacs(i);
	  
	  for (int j=0;j<ps.size();++j)
	    cout << ps[j]<<" ";
	  cout << endl;
	  
	  }*/

      sort(fr.begin(),fr.end());
      for (long m=L;m<=H;++m)
	{
	  bool skip=false;
	  for (long k=0;k<fr.size();++k)
	    if (!harm(m,fr[k]))
	      {
		skip=true;
		break;
	      }
	  if (skip)
	    continue;

	  me=m;
	  fail=false;
	  goto on;
	}


      fail=true;	  
      
      on:
      if (fail==false)
	{
	  
      for (long j=0;j<N;++j)
	{
	  if (!harm(me,fr[j]))
	    cout << me << "!=" << fr[j] << endl;
	}

      if (me<L || me>H)
	cout << "WWWWaaaaaaaaaaaaaa";
      
	}
      

      std::cout << "Case #" << case_+1 << ": ";// << endl;

      if (fail)
	cout << "NO";
      else
	cout << me;

      std::cout << std::endl;

    }
  return 0;
}
