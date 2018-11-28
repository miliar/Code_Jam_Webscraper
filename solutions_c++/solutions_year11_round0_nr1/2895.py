#include <iostream>
using namespace std;
int main()
{
	int t,n,temp,k;
	int cnt,cnto,cntb;
	int poso,posb;
	char c[2];
	cin>>t;
	for (int i=1;i<=t;i++)
	{
		cin>>n;
		cnt=cnto=cntb=0;
		poso=posb=1;
		for (int j=0;j<n;j++)
		{
			cin>>c;
			cin>>temp;
			if (c[0]=='O')
			{
				k=abs(temp-poso)-(cnt-cnto);
				if (k>0)
					cnt+=k;
				cnt++;
				poso=temp;
				cnto=cnt;
			}
			else
			{
				k=abs(temp-posb)-(cnt-cntb);
				if (k>0)
					cnt+=k;
				cnt++;
				posb=temp;
				cntb=cnt;
			}
		}

		cout<<"Case #"<<i<<": "<<cnt<<endl;
	}
	return 0;
}