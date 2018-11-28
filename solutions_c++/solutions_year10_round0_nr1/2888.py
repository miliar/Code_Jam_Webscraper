#include <iostream>

using namespace std;


int main()
{
  int T,k,N;
  int x=0;
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  while(cin>>T)
  {
    for (int i=0;i<T;i++)
    {
      cin >> N >> k;
	  int a=((1<<N)-1) ;
	  int b=(k%(1<<N));
	  if(a==b)
        cout<<"Case #"<<x+1<<": ON"<<endl;
	  else
	    cout<<"Case #"<<x+1<<": OFF"<<endl;
      x++;
    }
  }
}
