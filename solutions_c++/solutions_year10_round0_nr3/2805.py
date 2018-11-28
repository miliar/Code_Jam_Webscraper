#include <iostream>
#include <fstream>

using namespace std;

int g[10];
int main()
{
  int T,R,k,N,x,y;
  int j,p;
  int count_r,count_n;
  int sum;
  x=0;
  freopen("C-small-attempt0.in", "r", stdin);
  freopen("C-small-attempt0.out", "w", stdout);
  while(cin>>T)
  {
    for (int i=0;i<T;i++)
    {
      y=0;
      cin >> R >> k >> N;
      for( j=0; j<N; j++){
        cin >> g[j];
      }
      count_r=0;
	  count_n=1;
      sum=0;
      p=0;
      while(count_r<R ){
        if(sum+g[p]<=k && count_n<=N)
        {
            sum+=g[p];
        }
        else{
            y+=sum;
            sum=0;
            count_r++;
			
			p--;
			//count_n--;
			count_n=0;
        }
        p++;
		count_n++;
        if(p>=N)
          p=0;
      }
      cout<<"Case #"<<x+1<<": "<<y<<endl;
      x++;
    }
  }
}
