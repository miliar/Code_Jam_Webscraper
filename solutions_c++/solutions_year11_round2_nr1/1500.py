#include <iostream>
#include <vector>
#include <string>
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
      vector <string> sched;
      int i,j;
      double num,den;
      double wp[100][100],owp[100],oowp[100];
      for(i=0;i<N;i++)
	{
	  string s;
	  cin>>s;
	  sched.push_back(s);
	  for(j=0,num=0.0,den=0.0;j<N;j++)
	    {
	      if(s[j]=='1') {
		num++;
		den++;
	      } else if(s[j]=='0')
		den++;
	    }
	  for(j=0;j<N;j++)
	    {
	      if(s[j]=='.')
		wp[i][j]=num/den;
	      else if(s[j]=='1')
		wp[i][j]=(num-1.0)/(den-1.0);
	      else if(s[j]=='0')
		wp[i][j]=num/(den-1.0);
	      //	      cout<<wp[i][j]<<"\t";
	    }
	  //	  cout<<den<<"\n";
	}
      for(i=0;i<N;i++)
	{
	  for(j=0,num=0.0,den=0.0;j<N;j++)
	    if(sched[i][j]!='.') {
	      num+=wp[j][i];
	      den++;
	    }
	  owp[i]=num/den;
	  //	  cout<<owp[i]<<"\n";
	}
      for(i=0;i<N;i++)
	{
	  for(j=0,num=0.0,den=0.0;j<N;j++)
	    if(sched[i][j]!='.') {
	      num+=owp[j];
	      den++;
	    }
	  oowp[i]=num/den;
	}
      cout<<"Case #"<<t<<": "<<"\n";
      for(i=0;i<N;i++) {
	cout<<0.25*wp[i][i]+0.5*owp[i]+0.25*oowp[i]<<"\n";
      }
    }
  return 0;
}
