#include <iostream>
#include <sstream>
#include <fstream>
#include <conio.h>
#include <vector>
//#include<>
using namespace std;

int min(int a, int b)
{
  return a<b?a:b;  
    
};

int main(int argc, char *argv[])
{
   
    ifstream in;
    ofstream out;
    in.open("A-large(2).in",ios::in);
    out.open("ap.out",ios::out);
    int N,m,n,i,j,p,q;
    long long ans,base,mult;
    in >> N;
	string s,ts;
	bool got;
	int num[70],diff;
    for (n=1;n<=N;n++)
    {
		in>>s;
		if (s.size()==1) 
		{
			out<<"Case #"<<n<<": "<<1<<"\n";	
			continue;
		};
		diff=0;
		m=s.size();
		for (i=0;i<m;i++) num[i]=-1;
		num[0]=1;
		for (i=0;i<m;i++) if (s[i]==s[0]) num[i]=1;
		p=0;
		while ((p<m)&&(num[p]!=-1)) p++;
		if (p<m) 
		{
			diff++;
			for (i=0;i<m;i++) if (s[i]==s[p]) num[i]=0;		
		};
		got=true;
		while (got)
		{
			got=false;	
			p=0;
			while ((p<m)&&(num[p]!=-1)) p++;
			if (p<m)
			{
				got=true;
				diff++;	
				for (i=0;i<m;i++) if (s[i]==s[p]) num[i]=diff;						
			};
				
		};
		if (diff==0) diff++;
		base=diff+1;
		mult=1;
		ans=0;
		for (i=m-1;i>=0;i--)
		{
			ans+=mult*num[i];
			mult*=base;			
		};
		out<<"Case #"<<n<<": "<<ans<<"\n";

    };
    
    
    
    in.close();
    out.close();
    return EXIT_SUCCESS;
   
}
