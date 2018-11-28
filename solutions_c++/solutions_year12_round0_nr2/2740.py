#include <iostream>
#include <cstring>
#include <map>

using namespace std;

int main()
{
  int t,count=1;
  cin>>t;
  while(t--)
    {
      int n,s,p,score,ta,tb,result=0;
      cin>>n>>s>>p;
      while(n--)
	{
	  cin>>score;
	  if(score%3==0)
	      ta=score/3,tb=ta+1;
	  else if(score%3==1)
	      ta=(tb=(score+2)/3);
	  else
	      ta=(score+1)/3;tb=ta+1;

	  if(score%3==0 && score<3)tb=-1;
	  if(score%3==1 && score<4)tb=-1;
	  
	  if(ta>=p)result++;
	  else if(tb>=p && s>0){result++;s--;}
	}
      cout<<"Case #"<<count<<": "<<result<<endl;
      count++;
    }
  return 0;
}
