#include<iostream>

using namespace std;

int GCD( int n, int m)
{
  if(( n >= m) && (( n % m) == 0))
    return(m);
  else
    GCD(m,(n % m));
}

int LCM( int n, int m, int g)
{
  return ((n*m)/g);
}

using namespace std;

int main() 
{

  int i,j,k, T,c;
  char ch;
  int L, H,N;
  int freq[10010];
  int gcd;
  int lcm;
  int f=0;

  cin>>T;

  while(c++<T)
  {
    cin>>N>>L>>H;

    for(i=0;i<N;i++)
      cin>>freq[i];

    for(i=L; i<=H; i++)
    {
      f=1;
      for(j=0;j<N;j++)
      {
        if((i%freq[j] != 0 ) && ( freq[j]%i != 0))
        {
          f=0;
          break;
        }
      }
      if(f==1) break;
    }
    //printf("gcd=%lld, lcm=%lld\n", gcd, lcm);

    //    printf("gcd=%d, %d , %d", gcd , L, H);
    printf("Case #%d: ",c);
    if(f) printf("%d\n", i);
    else printf("NO\n");
  }

  return 0;
}

