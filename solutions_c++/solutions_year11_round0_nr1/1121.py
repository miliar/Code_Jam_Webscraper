#include<iostream>
#include<fstream>
using namespace std;
int solve();
int main()
{ofstream out1("outfile.out",ios::out);
	int caseNum,t,n,i,ans;
	cin>>t;
	for(caseNum=0;caseNum<t;caseNum++)
	{ 
		 ans=solve();
		 out1<<"Case #"<<caseNum+1<<": "<<ans<<endl;
	}
	return 0;
}
int solve()
{int n,i,counter=0,left;
			int oLeft=0,bLeft=0;
			  int oprt,bprt;
	    int oLast,bLast;

	 cin>>n;
	 char id;
	 int num;
	 oLast=1;bLast=1;
	 oprt=1;bprt=1;
	 oLeft=0;bLeft=0;
	for(i=0;i<n;i++)
	  {int o,b;
		  cin>>id>>num;
		  if(id=='O')
		  {
			  o=abs(num-oLast)-oLeft;
			  oLeft=0;
			  if(o+1<=0){bLeft=1;counter++;}
			  else
			  {
				  counter+=o+1;bLeft+=o+1;
			  }
			  oLast=num;

		  }
		  else
		  {
			    b=abs(num-bLast)-bLeft;
			  bLeft=0;
			  if(b+1<=0){oLeft=1;counter++;}
			  else
			  {
				  counter+=b+1;oLeft+=b+1;
			  }
			  bLast=num;
		  }
	      
	   }

	


	return counter;



}