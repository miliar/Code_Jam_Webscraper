#include <fstream>
#include <iostream>
#include <cmath>
using namespace std;

int gcd (int l_x, int s_x)
{
	int ret; 
	int large, small;
	if(l_x >s_x)
	{	
		large=l_x;
		small =s_x;
	}
	else 
		{large=s_x;
	small =l_x;}
	
	ret = large % small; 

	if (ret ==0 )
		return small; 
	else 
		ret = gcd(small, ret);

	return ret; 
}

int main()
{
ifstream fin;
ofstream fout; 
fin.open("B-small-attempt1.in");
fout.open("test.out");

int tc_count;
int N; 
int val[1000];
long long int sep_val[1000];
int n =0;
int x ; long long int a, b,c; 
fin>>tc_count;
while(n < tc_count)
{
	fin>>N;
	if(N==2)
	{
		
		fin>>a>>b; 
		if(a>b)
			sep_val[0] = a-b;
		else 
			sep_val[0] = b-a;

		int mod = b%sep_val[0];
		if (mod){
			;
			fout<<"Case #"<<n+1<<": "<<sep_val[0]-mod<<endl;
		}
		else 
			fout<<"Case #"<<n+1<<": "<<"0"<<endl;
	}
	else 
	{
		fin>>a>>b>>c; 
		if(a>b)
			sep_val[0] = a-b;
		else 
			sep_val[0] = b-a;

		if(b>c)
			sep_val[1] = b-c;
		else
			sep_val[1] = c-b;

		cout<<sep_val[0]<<" "<<sep_val[1]<<endl;
		int gcd_val;
		if (sep_val[0]==0)
			gcd_val=sep_val[1];
		else if (sep_val[1]==0)
			gcd_val=sep_val[0];
		else
			 gcd_val = gcd(sep_val[0],sep_val[1]);
		
		int mod = b%gcd_val;
		if (mod){
			;
			fout<<"Case #"<<n+1<<": "<<gcd_val-mod<<endl;
		}
		else 
			fout<<"Case #"<<n+1<<": "<<"0"<<endl;
	}
n++; 
}
//cout<<gcd(15,1)<<endl;

return 0;
}