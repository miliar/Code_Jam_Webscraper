#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

/*
typedef struct node
{
  node *parent;
} node;
*/

unsigned int gcd(unsigned int a, unsigned int b) //a>=b
{
  if (a<b)
    {
      unsigned int tmp;
      tmp=b;
      b=a;
      a=tmp;
    }
  if (a%b==0)
    return b;
  else
    {
      a=a%b;
      return gcd(b,a);
    }
}

bool prime(unsigned int p)
{
  if (p%2==0)
    return false;
  for (int i=3; i<=(unsigned int)sqrt((double)p); i++)
    {
      if (p%i==0)
	return false;
    }
  return true;
}

int main()
{
  
  unsigned int C;
  cin >> C;

  vector<unsigned int> primes; //primes<P

  for (int c=0; c<C; c++)
    {
      unsigned long long A,B,P;
      cin >> A >> B >> P;
      primes.clear();
      if (P>2)
	primes.push_back(2);

      for (int i=3; i<P; i+=2)
	if (prime(i))
	  primes.push_back(i);


      //      cout << "A" << endl;

      unsigned int nums[B+1];

      for (int i=A; i<=B; i++)
	nums[i]=0;

      //     cout << "B" << endl;
      for (int i=A; i<=B-1; i++)
	{
	  for (int j=i+1; j<=B; j++)
	    {
	      unsigned int d=gcd(i,j);
	      if (d>1)
		{
		  for (int k=0; k<primes.size(); k++)
		    {
		      while (d%primes[k]==0)
			d/=primes[k];
		    }
		  if (d>=P)
		    {
		      int k1=i;
		      int k2=j;
		      while (nums[k1]!=0)
			{
			  //			  cout << "k: " << k << " | " << nums[k]<< endl;
			  k1=nums[k1];
			}
		      while (nums[k2]!=0)
			{
			  //			  cout << "k: " << k << " | " << nums[k]<< endl;
			  k2=nums[k2];
			}
		      if (k1!=k2)
			nums[k2]=k1;
		      //		      cout << k1 << "<--" << k2 <<  " :: " << i << " " << j <<endl;
		      //		      nums[k]=i;
		    }
		}
	    }
	}
      //      cout << "C" << endl;

      bool in[B+1];
      for (int i=A; i<=B; i++)
	in[i]=false;
      //          cout << "D" << endl;

      unsigned int sol=0;
      for (int i=A; i<=B; i++)
	{
	  int j=i;
	  while (!in[j] && nums[j]>0)
	    {
	      //			  cout << "j: " << j << " | " << nums[j]<< endl;
	      j=nums[j];
	    }
	  if (!in[j] && nums[j]==0)
	    {
	      sol++;
	      //	      cout << "new set: " << i << endl;
	    }
	  in[j]=true;
	}
      //           cout << "E" << endl;

      cout << "Case #" << c+1 << ": " << sol << endl;
    }
  

  return 0;
}
