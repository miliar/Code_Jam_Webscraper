#include<iostream>
#include<memory>
#include<algorithm>
using namespace std;

int b[128][16];
int d[16];
int c[128];
int len[128];
int n; //品种数
int m; //顾客数

int check(int id_customer,int id_fruil,int mark)
{
	int l,r,mid;
	if(mark==1)
	{
		if(c[id_customer]==id_fruil)
			return 1;
		else return 0;
	}

	l=1;
	r=len[id_customer];
	while(l<=r)
	{
		mid=(l+r)/2;
		if(b[id_customer][mid]==id_fruil)
			return 1;
		else if(b[id_customer][mid]>id_fruil)
			r=mid-1;
		else l=mid+1;
	}
	return 0;
}


int check(int id_customer)
{
	int i;
	for(i=1;i<=n;i++)
	{
		if(check(id_customer,i,d[i]) )
			return 1;
	}
	return 0;
}

int ccount()
{
	int i;
	int temp=0;
	for(i=1;i<=m;i++)
		temp+=check(i);
	return temp;
}



int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("1.out","w",stdout);
	int i,j,k,tempc,mini_temp,mini_mark,cc,seq,num,t,x,y,N,mini_num,temp;
	cin>>num;
	for(seq=1;seq<=num;seq++)
	{
		cin>>n>>m;
		memset(len,0,sizeof(len));
		memset(c,0,sizeof(c));
		for(i=1;i<=m;i++)
		{
			cin>>t;
			for(j=1;j<=t;j++)
			{
				cin>>x>>y;
				if(y==1)
					c[i]=x;
				else b[i][++len[i]]=x;
			}

			sort(b[i]+1,b[i]+len[i]+1);
		}

		N=1;
		for(i=1;i<=n;i++)
			N*=2;

		mini_num=1024;
		mini_mark=0;

		for(i=0;i<N;i++)
		{
			memset(d,0,sizeof(d));

			temp=i;

			for(j=1;j<=n;j++)
			{
				d[j]=temp&1;
				temp>>=1;
				if(temp==0)
					break;
			}
			tempc=0;
			for(j=1;j<=n;j++)
				tempc+=d[j];

			
			if(ccount()==m && ( tempc<mini_num) )
			{
				mini_num=tempc;
				mini_mark=i;
			}
		}
	//	cout<<mini_mark<<' '<<mini_num<<endl;
		cout<<"Case #"<<seq<<":";

		memset(d,0,sizeof(d));
		temp=mini_mark;
		for(j=1;j<=n;j++)
		{
			d[j]=temp&1;
			temp>>=1;
		}

		if(mini_num==1024)
		{
			cout<<" IMPOSSIBLE"<<endl;
		}
		else{ for(i=1;i<=n;i++)
				cout<<' '<<d[i];
		cout<<endl;
		}
	}
	return 0;
}




