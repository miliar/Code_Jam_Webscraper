#include<iostream>
#define SIZE 100
using namespace std;
class Mat
{
	char Nodes[SIZE][SIZE];
	float rpi;
	float OOP[SIZE];
	int teams;
	bool flag;
	int final[SIZE];
	int t1,t2;
	public:
	void read(int);
	void calculate(int);
	void oop();
	void print();
};
int main()
{
	int tt;
	cin>>tt;
	int i;
	Mat a;
	for(i=0;i<tt;i++)
	{
		a.read(i);
	}
}
void Mat::oop()
{
	int i,j;
	float ans;
	int total,win;
	int oppteam;
	for(i=0;i<teams;i++)
	{
		ans=0;
		oppteam=0;
		OOP[i]=0;
		for(j=0;j<teams;j++)
		{
			if(Nodes[i][j]=='.')
				continue;
				
				oppteam++;
				total=0;
				win=0;
				int k;
				for(k=0;k<teams;k++)
				{
					if(k==i)
						continue;
					if(Nodes[j][k]=='.')
						continue;
					total++;
					if(Nodes[j][k]=='1')
						win++;
				}
				ans+=(win/(float)total);
		}
		ans/=(float)oppteam;
		OOP[i]+=ans;
		//cout<<"\nans:"<<ans;
	}
}
void Mat::calculate(int tno)
{
	rpi=0;
	//stage1
	int total=0;
	int win=0,i;
	float wp,oop,ooop;
	for(i=0;i<teams;i++)
	{
		if(Nodes[tno][i]=='.')
			continue;
		total++;
		if(Nodes[tno][i]=='1')
				win++;
	}
	wp=win/(float)total;
	//cout<<"  wp:"<<wp;
	//stage2
	oop=OOP[tno];
	//cout<<"  oop:"<<oop;
	//stage3
	ooop=0;
	int c=0;
	for(i=0;i<teams;i++)
	{
		if(Nodes[i][tno]=='.')
			continue;
			ooop+=OOP[i];
			c++;
	}
	ooop/=c;
	//cout<<"  ooops:"<<ooop<<"  ans:";
	cout<<(0.25*wp+0.50*oop+0.25*ooop)<<"\n";
}
void Mat::read(int no)
{
	int i,j;
	cin>>teams;
	for(i=0;i<teams;i++)
	{
		for(j=0;j<teams;j++)
		{
			cin>>Nodes[i][j];
		}
	}
	oop();
	if(no==0)
	cout<<"\n";
	cout<<"Case #"<<no+1<<":\n";
	for(i=0;i<teams;i++)
	{
		calculate(i);
		
		//print();
	}
}
void Mat::print()
{
	int i;
	for(i=0;i<teams;i++)
	{
		cout<<final[i]<<"\n";
	}
}
