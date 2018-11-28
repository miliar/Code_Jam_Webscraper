#include<iostream>
using namespace std;
struct s
{
	int a,b,c;
};
int main()
{
	int n,cnt;
	cin>>n;

	s a[31][2];
	int j,i;
	//struct s[200];
	a[0][0].a=a[0][0].b=a[0][0].c=a[0][1].a=a[0][1].b=a[0][1].c=0;
	for(j=2;j<31;j++)
	{
		i=j/3;
		if(j%3==0)
		{
			a[j][0].a=a[j][0].b=a[j][0].c=i;

			a[j][1].a=i-1;
			a[j][1].b=i;
			a[j][1].c=i+1;


		}
		else if(j%3==2)
		{

			a[j][0].a=i;
			a[j][0].b=a[j][0].c=i+1;
			a[j][1].a=a[j][1].b=i;
			a[j][1].c=i+2;


		}
		else
		{
			a[j][0].a=a[j][0].b=i;
			a[j][0].c=i+1;

			a[j][1].a=i-1;
			a[j][1].b=a[j][1].c=i+1;

		}
		//cout<<j<<' '<<a[j][0].a<<a[j][0].b<<a[j][0].c<<' '<<a[j][1].a<<a[j][1].b<<a[j][1].c<<endl;
	}
	a[29][1]=a[29][0];
	a[30][1]=a[30][0];
	//a[0][0].a=a[0][0].b=a[0][0].c=0;
	//a[0][1]=a[0][0];
	a[1][0].a=a[1][0].b=0;
	a[1][0].c=1;
	a[1][1]=a[1][0];
	//cin>>n;
	for(i=0;i<n;i++)
	{


		int k,m,l;
		cin>>j>>k>>l;
		int p,q,r;
		cnt=0;
		int*b=new int[j];

		s*c=new s[j];
		for(m=0;m<j;m++)
		{
			cin>>b[m];
			c[m]=a[b[m]][0];
			//cout<<a[b[m]][1].c<<endl;
			if((a[b[m]][1].c>=l)&&(a[b[m]][0].c<l)&&(k--)>0)
			{


				c[m]=a[b[m]][1];
//				cout<<"k="<<k--<<endl;;
			}
//			cout<<c[m].a<<' '<<c[m].b<<' '<<c[m].c<<' '<<endl;
			if(c[m].c>=l)
			{
				cnt++;
			}



		}
		cout<<"Case #"<<i+1<<": "<<cnt<<endl;



	}
	//cout<<cnt<<endl;
	return 0;
}
