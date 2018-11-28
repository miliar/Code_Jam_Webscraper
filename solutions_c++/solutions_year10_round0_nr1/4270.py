#include<iostream>
#include<fstream>

using namespace std;


class abc 
{ 
	public: int p , s; 
	abc(){ p=s=0;}
};


int solve(int N ,int K)
{
	abc *a=new abc[N];
	a[0].p=1;
	while(K!=0)
	{
		for(int i=0 ;i <N ;i++)
		{
			if(a[i].p==1) 
				if(a[i].s==0)a[i].s=1;
				else a[i].s=0;
			else break;
		} 
		for(int i=0 ;i <N ;i++)
		{
			if(a[i].p && a[i].s ==0) 
				while(++i!=N)
					a[i].p=0;
			else if(a[i].p && a[i].s ==1) 
				while(i!=N)
				{
					if(a[i].p && a[i].s ==1)
					{	i++;
						a[i].p=1;
					}
					else break;
				}
		
		} 
		K--;
	}
	
		return a[N-1].p && a[N-1].s;
	

} 

int main()
{
	ifstream in("a.in");
	ofstream out("out.out");
	int T,N,K;
	in>>T;
	for(int i=1 ;i<=T ;i++)
	{
		in>>N>>K;
		if(solve(N,K)==0)
			out<<"Case #"<<i<<": "<<"OFF"<<endl;		
		else 
			out<<"Case #"<<i<<": "<<"ON"<<endl;	
	}	
	in.close();
	out.close();
	return 0;
}
