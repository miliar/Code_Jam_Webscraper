#include<iostream>
#include<vector>
using namespace std;

int main()
{
	int t,r,k,n;;
	int c,flag;
	int i,j;
	long long int val,tc,rv;
	int grp[1001];
	vector <int> prf;
	int rn;
	long long int fval=0;
	cin>>t;
	c=0;
	while(c++<t)
	{
		cin>>r>>k>>n;
		i=0;
		while(i<n)
			cin>>grp[i++];

		val=0;
		j=0;
		for(i=0;i<r;i++)
		{	tc=0;
			flag=n;
			while(flag && ((tc + grp[j]) <= k))
			{
				tc += grp[j++];
				if(j==n) j=0;
				flag--;
			}
			prf.push_back((int) tc);
			val+=tc;
			if(j==0)
			{
			         rn=i+1;
				 r -=rn;
				 if(!r) break;
				 val += ((r/rn) * val);
				 for(int l=0,m= r%rn; l < m; l++)	 
				 val += prf[l];

				 break;
			}
		}	
		cout<<"Case #"<<c<<": "<<val<<endl;
		prf.erase(prf.begin(), prf.end());		
	}

	return 0;
}
