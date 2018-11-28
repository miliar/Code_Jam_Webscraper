#include<fstream>
#define dmax 103
using namespace std;
ifstream in("dancing.in");
ofstream out("dancing.out");

int t, n, x[dmax], p, s;

int mn(int a, int b)
{
	if(a < b)
		return a;
	return b;
}

void solve(int index)
{
	int sol=0, k=0;
	
	for(int i=1; i<=n; i++)
	{
		int m = x[i]/3;
		
		bool ok = 0;
		
		//out<<m<<'\n';
		//out<<m<<" "<<m<<" "<<m+2<<" "<<x[i]<<'\n';
		
		if(m + m + m == x[i])
		{	
			if(m >= p)
			{	sol++;
				ok = 1;
			}	
			//out<<"%"<< i<<" "<<ok<<"%";
		}
		if(m + m + m+1 == x[i])
		{	
			if(m+1 >= p)
			{	sol++;
				ok = 1;
			}	
			//out<<"%"<< i<<" "<<ok<<"%";
		}
		else if(m + m + m-1 == x[i] && m>0)
		{
			if(m >= p)
			{	sol++;
				ok = 1;
			}
			//out<<"%"<< i<<" "<<ok<<"%";
		}
		else if(m + m+1 + m+1 == x[i])
		{	
			if(m+1 >= p)
			{	sol++;
				ok = 1;
			}
			//out<<"%"<< i<<" "<<ok<<"%";
		}
		else if(m + m-1 + m-1 == x[i] && m>0)
		{
			if(m >= p)
			{	sol++;
				ok = 1;
			}
			//out<<"%"<< i<<" "<<ok<<"%";
		}
		//----------------------
		
		if(m + m-1 + m+1 == x[i] && !ok && m>0)
		{
			if(m+1 >= p)
				k++;
		}
		else if(m + m+1 + m+2 == x[i] && !ok)
		{
			if(m+2 >= p)
				k++;
		}
		else if(m + m+2 + m+2 == x[i] && !ok)
		{
			if(m+2 >= p)
				k++;
		}
		else if(m + m-1 + m-2 == x[i] && !ok && m>0)
		{
			if(m >= p)
				k++;
		}
		else if(m + m-2 + m-2 == x[i] && !ok && m>1)
		{
			if(m >= p)
				k++;
		}
		else if(m + m + m+2 == x[i] && !ok)
		{	
			if(m+2 >= p)
				k++;
		}
		else if(m + m + m-2 == x[i] && !ok && m>1)
		{
			if(m >= p)
				k++;
		}
	}		
	
	//out<<sol<<" "<<k<<'\n';
	
	out<<"Case #"<<index<<": "<<sol + mn(k, s)<<'\n';
	
}	



int main()
{
	int i;
	
	in>>t;

	for(i=1; i<=t; i++)
	{
		in>>n>>s>>p;
		
		for(int j=1; j<=n; j++)
			in>>x[j];
		
		solve(i);
	}
	
	in.close();
	out.close();
	return 0;
}	