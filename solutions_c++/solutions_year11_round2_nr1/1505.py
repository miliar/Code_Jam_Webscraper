#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

  char mapa[120][120];
  long double wp[120];
  long double owp[120];
  long double oowp[120];
  

long double rpi(int n)
{
  return 0.25 * wp[n] + 0.5 * owp[n] + 0.25 * oowp[n];  
}

int main()
{
  int t;
  cin>>t;
  
  
  for(int i=1; i<=t; i++)
  {
    int n;
    cin>>n;
    
    for(int ii=0; ii<n; ii++)
      for(int jj=0; jj<n; jj++)
	cin>>mapa[ii][jj];
      
    //calculo wp
    for(int ii=0; ii<n; ii++)
    {
      int cont=0;
      int todos=0;
      for(int jj=0; jj<n; jj++)
      {
	  if(mapa[ii][jj]=='.') continue;
	  if(mapa[ii][jj]=='1') cont++;
	  todos++;	
      }
      wp[ii]=(1.0*cont)/(1.0*todos);
    }
    
    
    //calculo owp 
    for(int ii=0; ii<n; ii++)
    {
	int total=0;
	vector<long double> owps;
	for(int jj=0; jj<n; jj++)
	{
	    if(mapa[ii][jj]=='.') continue;
	    else
	    {
		total++;
		int cont=0;
		int todos=0;
		for(int kk=0; kk<n; kk++)
		{
		    if(kk==ii || mapa[jj][kk]=='.') continue;
		    if(mapa[jj][kk]=='1') cont++;
		    todos++;
		}
		
		owps.push_back((1.0*cont)/(1.0*todos));
	    }
	}
	long double sum=0.0;
	for(int jj=0; jj<owps.size(); jj++)
	  sum+=owps[jj];
	
	owp[ii]=sum/(total*1.0);
    }
    
    //calcula oowp
    for(int ii=0; ii<n; ii++)
    {
      long double sum=0.0;
      long double cont=0.0;
      for(int jj=0; jj<n; jj++)
	{
	  if(mapa[ii][jj]!='.')
	  {
	      sum+=owp[jj];
	      cont+=1.0;
	  }
	  
	}
	oowp[ii]=sum/cont;
    }
    
    cout<<"Case #"<<i<<":\n";
    for(int ii=0; ii<n; ii++)
      printf("%.12Lf\n",rpi(ii));
      
      //cout<<rpi(ii)<<endl;
    
    
    
    
  }
  return 0;
}