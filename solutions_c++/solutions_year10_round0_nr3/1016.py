#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;


int main()
{
	ifstream cin("a.in");
	ofstream cout("a.out");
	
	long long r,k,n;
	long long a[2001];
	long long b[2001][2];//下一个打头和此次人数
	bool c[2001];
	long long d[2001];
	int cir;
	int i;
	int j;
	bool sx;
	long long num;
	int f,f1;
	long long sum;
	int t;
	cin>>t;
	for (i = 0 ; i < t; i++)
	{
		cin>>r>>k>>n;
		for ( j = 0; j < n; j++)
		{
			cin>>a[j];
			c[j] = false;
		}
		
		num = 0;
		f = 0;
		sum = 0;
		sx = true;
		cir = 0;
		while (num < r)
		{
			
			if (c[f])
			{
				if (sx)
				{
					sx = false;
					f1 = f;
					d[0] = b[f][1];
					cir++;
					sum+=b[f][1];
					f = b[f][0];
				}
				else
				{
					if (f==f1)
					{
						break;
					}
					else
					{
						d[cir] = 0;
						
						
						d[cir]+=d[cir-1];
						
						d[cir]+=b[f][1];
						cir++;
						sum+=b[f][1];
						f = b[f][0];
					}
				}
			}
			else
			{
				c[f] = true;
				int temp;
				temp = f;
				temp++;
				if (temp == n)
				{
					temp = 0;
				}
				long long s;
				s =0 ;
				s+=a[f];
				while (1)
				{
					s+= a[temp];
					if (s > k || temp ==f )
					{
						s -=a[temp];
						break;
					}

					temp++;
					

					

					if(temp>=n)
						temp = 0;

				}
				b[f][0] = temp;
				b[f][1] = s;
				sum+=s;
				f = temp;

			}
			num++;
		}

		cout<<"Case #"<<i+1<<": ";
		if (num == r)
		{
			cout<<sum<<endl;
		}
		else
		{
			sum+=(r-num)/cir*d[cir-1];
			if((r-num)%cir > 0)
				sum+=d[(r-num)%cir-1];
			cout<<sum<<endl;

		}

		



	}
	return 0;
}