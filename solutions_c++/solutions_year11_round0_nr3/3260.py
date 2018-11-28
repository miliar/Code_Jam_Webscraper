#include<iostream>

using namespace std;
unsigned long long int arr[15],lim;
unsigned long long int mx;
bool flag;

void splic(unsigned long long int n,unsigned long long int sump,unsigned long long int cntp,unsigned long long int sums,unsigned long long int cnts,unsigned long long int vals)
{
	if(n==lim)
	{
		if(sump == sums && cntp!=0 && cnts!=0)
		{
			flag = true;
			if(vals > mx)
				mx = vals;
		}
	}
	else
	{
		splic(n+1,sump^arr[n],cntp+1,sums,cnts,vals);
		splic(n+1,sump,cntp,sums^arr[n],cnts+1,vals+arr[n]);
	}
}

int main()
{
	int t,tbc;
	cin>>t;
	tbc = t;
	while(t--)
	{
		for(int i=0;i<15;i++)
			arr[i] = 0;
		cin>>lim;
		mx = 0;
		flag = false;	

		for(int i=0;i<lim;i++)
		{
			cin>>arr[i];
		}

		splic(0,0,0,0,0,0);

		if(flag)	
			cout<<"Case #"<<tbc-t<<": "<<mx<<endl;
		else
			cout<<"Case #"<<tbc-t<<": NO"<<endl;
	}
	return 0;
}
