#include<iostream>
#include<string>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

void p(long n)
{
  if(n<10) {cout<<"000"<<n<<endl; return;}
  if(n<100) {cout<<"00"<<n<<endl; return;}
  if(n<1000) {cout<<"0"<<n<<endl; return;}
  if(1) {cout<<n<<endl; return;}

  
}


int main()
{
  string s, Ns;
  long N;
  long i,j,k;
  long xx[601][20];


  getline (cin,Ns);
  
  N = atoi(Ns.c_str());
  string w("welcome to code jam");




  for(i = 1; i <= N; ++i)
    {

      
      getline (cin,s);
      xx[s.size()][18] = 0;
      for(j = s.size()-1; j >= 0; --j)
	{
	  xx[j][18] = xx[j+1][18]; 
	  if(s[j] == w[18]) ++xx[j][18];
	}
    
      //      for(j=0; j<s.size(); ++j) cout <<xx[j][18]<<endl;

      for( j = 17; j >= 0; --j)
	{
	  xx[s.size()-1][j] = 0;
	  for(k = s.size()-2; k>=0; --k)
	    {
	      xx[k][j] = xx[k+1][j];
	      if(s[k] == w[j]) xx[k][j] = (xx[k][j] + xx[k][j+1]) % 10000;
	    }
	}
      
      cout <<"Case #"<<i<<": ";
      p(xx[0][0]);
      
      //      for(j=0; j<=18; ++j) {
      //	cout <<w[j]<<" ";
      //	for(k = 0; k < s.size(); ++k) {
      //	  cout <<xx[k][j];
      //	}
      //	cout <<endl;
      //}
      //cout <<"  "<<s<<endl;

    }

}

