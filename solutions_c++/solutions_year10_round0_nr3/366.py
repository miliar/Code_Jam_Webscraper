#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	long long int c,r,k,n,i,ij,temp=0,a,j,b;
	long long int gsum=0;
	vector <long long int> gr,chk,sum,fj;
	cin>>c;
	for(i=1;i<=c;i++)
	{
		cin>>r>>k>>n;
		gsum=0;
		gr.clear();
		chk.clear();
		sum.clear();
		fj.clear();
		chk.resize(n);
		sum.resize(n);
		fj.resize(n);
		temp=0;
		for(b=0;b<n;b++)
		{
			cin>>a;
			temp+=a;
			gr.push_back(a);
		}
		if(temp<=k)
			gsum=temp*r;
		else
		{
			j=0;
			while(r>0)
			{
				r--;
				temp=0;
				if(chk[j]==0)
				{
					ij=j;				
					while(temp<=k)
					{
						temp+=gr[j];
						j=(j+1)%n;
					}
					j--;
					if(j==-1)
						j=n-1;
					temp-=gr[j];
					sum[ij]=temp;
					chk[ij]=1;
					fj[ij]=j;
					gsum+=temp;
				}
				else
				{
					gsum+=sum[j];
					j=fj[j];
				}
			}
		}
		cout<<"Case #"<<i<<": "<<gsum<<"\n";
	}
	return 0;
}
