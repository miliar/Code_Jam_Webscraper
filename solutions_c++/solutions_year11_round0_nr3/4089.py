#include<iostream>
unsigned long values[100],xora,xorb,xorsum,currentPermutation;
using namespace std;
int main()
{
	long pow2[25],range,suma,sumb;
	pow2[0]=1;
	int testCases,digit;
	long N,max;
	cin >> testCases;
	for(int i = 1 ; i <= 20 ; i++)
	{pow2[i]=2*pow2[i-1];};
	
	for(int ctr = 1 ; ctr <= testCases ; ctr++)
	{	
		cin >> N ;
		for(int i = 0 ; i < N ; i++)cin  >> values[i];
		// test permutation
		xorsum=0;
		for(int i = 0 ; i < N ; i++)xorsum = xorsum ^ values[i];
		if(xorsum!=0)
		{
			cout <<"Case #"<<ctr<<": "<<"NO\n";
		}
		else
		{
			range = pow2[N]-1;
			//cout << "Range : " << range << "::"<<N<<"\n";
			max = -1 ;
			for(currentPermutation=0;currentPermutation<=range;currentPermutation++)
			{
				suma=0,sumb=0,xora=0,xorb=0;
				//cout << " Looping : " << currentPermutation << "\n";
				for(int element=0;element<N;element++)
				{
					digit = (currentPermutation >> element) & 1;
					if(digit==1)
					{
						xora = xora ^ values[element];
						suma = suma + values[element];
					}
					else
					{
						xorb = xorb ^ values[element];
						sumb = sumb + values[element];
					}	

				}
				//cout << suma << " \t " << sumb << " \t " << xora << " \t " << xorb << "\n";
				if(xora==xorb)
				{
					if(suma > max && sumb > 0) max = suma;
					if(sumb > max && suma > 0) max = sumb;
					//cout << " YES " << max << "\n";
				}
			}
			if(max>0)
			cout <<"Case #"<<ctr<<": "<<max<<"\n";
			else
			cout <<"Case #"<<ctr<<": NO\n";
		}
	}
}
