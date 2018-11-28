#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>




int main()
{
  std::ifstream in("in");
  int cases;
  in >> cases;

  for (int c=0;c<cases;++c)
    {
      std::cout << "Case #" << c+1 << ": ";
      int N,K;
      in >> N >> K;

      
      std::vector<char> field(N*N);

      for (int i=0;i<N*N;++i)
	{
	  char c;
	  in >> c;
	  field[i]=c;
	}	 
if (0)
	  {
      std::cout << std::endl;
      for (int y=0;y<N;++y)
	{
	for (int x=0;x<N;++x)
	{
	  std::cout << field[x+y*N];
	  
	}
	std::cout << std::endl;
	
	}
	  }
 

        for (int y=0;y<N;++y)
	{
	  int c=N-1;
	  for (int x=N-1;x>=0;--x)
	    {
	      if (field[x+y*N]!='.')
		{
		  field[c+y*N]=field[x+y*N];
		  if (c!=x) field[x+y*N]='.';
		  --c;
		}
	      
	    }
	  

	}
	
      

	if (0)
	  {
	    
	std::cout << 'X'<<std::endl;
      for (int y=0;y<N;++y)
	{
	for (int x=0;x<N;++x)
	{
	  std::cout << field[x+y*N];
	  
	}
	std::cout << std::endl;
	
	}
	  }
	

      bool win[2]={false,false};
      char colors[2]={'R','B'};
				       //row
      for (int c=0;c<2;++c)
	{
	  
	  for (int y=0;y<N;++y)
	{
	  for (int x=0;x<N-K+1;++x)
	    {
	      int cc=0;
	      for (int k=0;k<K;++k)
		{
		  if (field[x+k+y*N]!=colors[c])
		    break;
		  else
		    ++cc;
		}
	      if (cc==K)
		win[c]=true;
	      
		  
	      
	    }
	}
	}
      
				       //col
      for (int c=0;c<2;++c)
	{
	  
      for (int y=0;y<N-K+1;++y)
	{
	  for (int x=0;x<N;++x)
	    {
	      int cc=0;
	      for (int k=0;k<K;++k)
		{
		  if (field[x+(k+y)*N]!=colors[c])
		    break;
		  else
		    ++cc;
		}
	      if (cc==K)
	            win[c]=true;
	    }
	}
      
	}

				       //diag1
      for (int c=0;c<2;++c)
	{
	  
      for (int y=0;y<N-K+1;++y)
	{
	  for (int x=0;x<N-K+1;++x)
	    {
	      int cc=0;
	      for (int k=0;k<K;++k)
		{
		  if (field[x+k+(k+y)*N]!=colors[c])
		    break;
		  else
		    ++cc;
		}
	      if (cc==K)
	            win[c]=true;
	    }
	}
      
	}

				       //diag2
      for (int c=0;c<2;++c)
	{
	  
      for (int y=0;y<N-K+1;++y)
	{
	  for (int x=K-1;x<N;++x)
	    {
	      int cc=0;
	      for (int k=0;k<K;++k)
		{
		  if (field[x-k+(k+y)*N]!=colors[c])
		    break;
		  else
		    ++cc;
		}
	      if (cc==K)
	            win[c]=true;
	    }
	}
      
	}


      
      if (win[0] && win[1])
	std::cout << "Both";
      else if (win[0])
	std::cout << "Red";
      else if (win[1])
	std::cout << "Blue";
      else
	std::cout << "Neither";
      
     


      
      std::cout << std::endl;

    }
  return 0;
}
