#include <stdio.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

//struct elem{
//  long num;
//  bool used;
//};

//typedef struct elem Elem;

template <class T>
T gcd(T a, T b)
{
  T c;
  if (b==0)
    return a;
  
  if (a<b)
    {
      c=a;
      a=b;
      b=c;
    }

  while(1)
    {
      c=a%b;
      if (c==0)
	return b;
      a=b;
      b=c;
    }

  //  return gcd(b, a%b);
}

template <class T>
T ngcd(vector<T> a, int n)
{
  if (n==1)
    return a[0];

  return gcd(a[n-1], ngcd(a, n-1));

}

int main()
{
  int i=0,j=0;
  int C=0, N=0;
  //  vector<long long> t(1000, 0);
  //  vector<long long> gap(1000, 0);
  long long gcdValue;
  
  char filename[32]="B-small-attempt2";
  //char filename[32]="B-large";
  //  char filename[32]="test";

  char infile[32], outfile[32];
  strcpy(infile, filename); strcpy(outfile, filename);
  strcat(infile, ".in"); strcat(outfile, ".out");
  FILE *fp=fopen(infile, "r"), *ofp=fopen(outfile, "w");
  
  fscanf(fp, "%d", &C);
 
  for(i=1;i<=C;i++) 
    {
      int noRepeatNum=1;
      cout<<endl;
      cout<<"i="<<i<<endl;
      fscanf(fp, "%d",&N);
      vector<long long> t(N, 0);
      vector<long long> gap(N-1, 0);

      for (j=0; j<N; j++)
	fscanf(fp, "%lld", &t[j]);
      
      sort(t.begin(), t.end());
      
      for (j=0; j<N; j++)
	cout<<t[j]<<" "<<endl;
      cout<<endl;

      for (j=0; j<N-1; j++)
	{
	  if (t[j+1]!=t[j])
	    {
	      gap[noRepeatNum-1]=t[j+1]-t[0];	   
	      noRepeatNum++;
	    }
	   
	}

      cout<<"noRepeatNum="<<noRepeatNum<<endl;
      for (j=0; j<noRepeatNum; j++)
	{
	  cout<<"gap["<<j<<"]="<<gap[j]<<endl;
	}

      long long result;
      if (noRepeatNum==1)
	{
	  result=0;
	}
      else 
	{
	  if (noRepeatNum==2)
	    {
	      gcdValue=gap[0];
	    }
	  else 
	    {
	      if (noRepeatNum==3)
		gcdValue=gcd(gap[0], gap[1]);
	      else
		gcdValue=ngcd(gap, noRepeatNum);
	    }
	  
	  
	  cout<<"gcd="<<gcdValue<<endl;
	  
	  if (gcdValue>=t[0])
	    {
	      result=gcdValue-t[0];
	    }
	  else
	    {
	      if (t[0]%gcdValue==0)
		result=0;
	      else
		result=(t[0]/gcdValue+1)*gcdValue-t[0];
	      cout<<"result="<<result<<endl;
	    }
	}
	
      fprintf(ofp, "Case #%d: %lld\n", i, result);
      
    }
  
  fclose(fp);
  fclose(ofp);
  
  return 0;
}
