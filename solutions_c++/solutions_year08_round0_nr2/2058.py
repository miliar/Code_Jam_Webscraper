#include<iostream>
#include<algorithm>
using namespace std;
int a1[100],a2[100],b1[100],b2[100],a[100],b[100],flag=0;
int main()
{
	int n,na,nb,t;
	int i,j,k,l;
	int cnt1=0,cnt2=0;
	char s1[6],s2[6];
	cin>>n;
	int m=1;
	while(m<=n)
	{
		cin>>t;
		cin>>na>>nb;
		cnt1=cnt2=0;
		//s1="00:00";
		for(i=0;i<na;i++)
		{
			cin>>s1>>s2;
			a1[i]=a2[i]=0;
			a1[i]=s1[0]%48;
			a1[i]=(a1[i]*10)+(s1[1]%48);
			a1[i]*=60;
			a1[i]+=(s1[3]%48)*10+(s1[4]%48);/**/
			//cout<<a[i][0];
			a2[i]=s2[0]%48;
			a2[i]=(a2[i]*10)+(s2[1]%48);
			a2[i]*=60;
			a2[i]+=(s2[3]%48)*10+(s2[4]%48);
		}
		for(i=0;i<nb;i++)
		{
			cin>>s1>>s2;
			b1[i]=b1[i]=0;
			b1[i]=s1[0]%48;
			b1[i]=(b1[i]*10)+(s1[1]%48);
			b1[i]*=60;
			b1[i]+=(s1[3]%48)*10+(s1[4]%48);/**/
			//cout<<a[i][0];
			b2[i]=s2[0]%48;
			b2[i]=(b2[i]*10)+(s2[1]%48);
			b2[i]*=60;
			b2[i]+=(s2[3]%48)*10+(s2[4]%48);
		}
		//for(i=0;i<na;i++)
		//	cout<<i<<" "<<a1[i]<<" "<<a2[i]<<endl;
		sort(a1,a1+na);
		sort(a2,a2+na);
		sort(b1,b1+nb);
		sort(b2,b2+nb);
		flag=0;
		for(i=0;i<100;i++) a[i]=b[i]=0;
		for(i=0;i<na;i++)
		{	
			flag=0;
			for(j=0;j<nb;j++)
			{
				if((a1[i]>=(b2[j]+t))&&(b[j]!=1))
				{
					k=j;
					flag=1;
				}
			}
			if(flag)
			{
				b[k]=1;
			}
			else
				cnt1++;
		}
		flag=0;
		for(i=0;i<nb;i++)
		{	
			flag=0;
			for(j=0;j<na;j++)
			{
				if((b1[i]>=(a2[j]+t))&&(a[j]!=1))
				{
					k=j;
					flag=1;
				}
			}
			if(flag)
			{
				a[k]=1;
			}
			else
				cnt2++;
		}
		/*for(i=0;i<na;i++)
			cout<<i<<" "<<a1[i]<<" "<<a2[i]+t<<endl;
		for(i=0;i<nb;i++)
			cout<<i<<" "<<b1[i]<<" "<<b2[i]+t<<endl;/**/
				cout<<"Case #"<<m<<": "<<cnt1<<" "<<cnt2<<endl;
		m++;
	}
}
