#include <iostream>

using namespace std;

int main()
{
  int T;
  int count = 0;
  cin>>T;
  for(int it = 1; it<=T; it++)
  {
    count = 0;
    int N, S, p, score;
    cin>>N>>S>>p;
    for(int j = 0; j<N; j++)
    {
      cin>>score;
      int a= score/3;
      int b = a+1;
      int c = a-1;
      if(a+a+a == score && a>=p)
      {
	count +=1;
	continue;
      }
      else if(a+a+b == score && b>=p && b <= 10)
      {
	count +=1;
	continue;
      }
      
      else if(a+b+b == score && b>=p && b <= 10)
      {
	count +=1;
	continue;
      }
      
      else if(a+a+a+2 == score && a+2>=p && a+2<=10 && S>0)
      {
	count +=1;
	S -=1;
	continue;
      }
      else if(c+a+b == score && b>=p && c>=0 && b<= 10 && S>0)
      {
	count +=1;
	S -=1;
	continue;
      }
      else if(c+b+b == score && b>=p && c>=0 && b<=10 && S>0)
      {
	count +=1;
	S -=1;
	continue;
      } 
    }
    cout<<"Case #"<<it<<": "<<count<<endl;
  }
  return 0;
}