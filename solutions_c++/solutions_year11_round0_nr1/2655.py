#include <iostream>
using namespace std;

int absdiff(int x, int y)
{
  return (x>y)?(x-y):(y-x);
}

int main()
{
  int T;
  cin>>T;
  for(int t=1;t<=T;t++)
    {
      int N;
      cin>>N;
      int pos[2], flex[2];
      pos[0]=pos[1]=1;
      flex[0]=flex[1]=0;
      int color, prevColor=-1, totalCost =0;
      for(int i=0;i<N;i++)
	{
	  int cost,button;
	  char ch;
	  cin>>ch;
	  color=(ch=='B')?0:1;
	  cin>>button;
	  if(color == prevColor) {
	    cost = absdiff(button, pos[color])+1;
	    flex[1-color]+=cost;
	    totalCost += cost;
	  } else {
	    if(absdiff(button, pos[color]) <= flex[color])
	      cost = 1; 
	    else 
	      cost=absdiff(button, pos[color]) - flex[color] + 1;
	    flex[1-color]=cost;
	    flex[color]=0;
	    totalCost+=cost;
	  }
	  pos[color]=button;
	  prevColor=color;
	  //	  cout<<"Color "<<color<<" Cost "<<cost<<"\n";
	}
      cout<<"Case #"<<t<<": "<<totalCost<<"\n";
    }
  return 0;
}
