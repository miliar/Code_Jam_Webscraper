#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
#include <vector>
#include <math.h>
#include <iomanip>
//#include<>
using namespace std;

bool zero(double a)
{
  return ((a<0.00000001)&&(a>-0.00000001));    
};
int min (int a, int b)
{
	return (a<b?a:b);	
};

bool current[10000];

int release[100],depth,P,Q;

int poisk()
{
	if (depth==Q) return 0;
	int i,j,a=100000000,s;
	for (i=0;i<Q;i++) if (!current[release[i]])
	{
//		if (i==2) cout<<"depth: "<<depth<<"\n";
		s=0;
		for(j=release[i]+1;(j<P)&&(!current[j]);j++) s++;
		for(j=release[i]-1;(j>=0)&&(!current[j]);j--) s++;
		current[release[i]]=true;
		depth++;
		s+=poisk();
		depth--;
		current[release[i]]=false;
		a=min(a,s);
	};
//	cout<<depth<<" "<<a<<"\n";
	return a;
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("C-small-attempt0(2).in",ios::in);
    out.open("ap.out",ios::out);
    int N,T,t,m,n,i,j,p,q;
    in >> N;
    for (n=1;n<=N;n++)
    {
		in>>P>>Q;
		for (i=0;i<P;i++) current[i]=false;
		for (i=0;i<Q;i++) 
		{
			in>>release[i];
			release[i]--;
		};
		depth=0;
		out<<"Case #"<<n<<": "<<poisk()<<"\n";
		
    };
    
    
    
    in.close();
    out.close();
//	getch();
    return EXIT_SUCCESS;
   
}
