#include<iostream>
#include<fstream>
#include<string>
using namespace std;


class num
{
public:
	int dig[100];
	int length;

	num(){length=0;}
	void input(ifstream &fin);
	num jian(num A,num B);
	num mod(num A,num B);
	bool dayu(num A,num B);
};

void num::input(ifstream &fin)
{
	string s;
	fin>>s;
	length=s.size();
	for (int i=0;i<length;i++)
		dig[length-i-1]=s[i]-'0';
}

num num::jian(num A,num B)
{
	if (dayu(B,A))
	{
		num tmp;
		tmp=A;
		A=B;
		B=tmp;
	}
	int j,r=0;
	for (int i=0;i<=A.length;i++)
	{
		j=A.dig[i]-B.dig[i]+r;
		if (j<0)
		{
			j+=10;
			r=-1;
		}
		dig[i]=j;
	}
	length=A.length;
	while ((length>0)&&(dig[length]==0)) length--;
	return *this;
}

bool num::dayu(num A,num B)
{
	if (A.length>B.length) return 1;
	if (A.length<B.length) return 0;
	for (int i=A.length;i>0;i--)
	{
		if (A.dig[i]>B.dig[i]) return 1;
		if (A.dig[i]<B.dig[i]) return 0;
	}
	return 0;
}

num num::mod(num A,num B)
{
while (dayu(A,B)) 
A.jian(A,B);
return A;
}

num a[10];
num cha[100];
int c,n,m;

num gcd(num a,num  b)
{
	num  r;
	r.mod(a,b);
	while (r.length!=0)
	{
		a=b;
		b=r;
		r.mod(a,b);
	}
	return b;
}



int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B.in");
	fout.open("B.out");
	fin>>c;
	for (int i=1;i<=c;i++)
	{
		fin>>n;
		for (int j=1;j<=n;j++)
			a[j].input(fin);
		m=0;
		for (int j=1;j<=n;j++)
			for(int k=j+1;k<=n;k++)
			{
				//if (a[j]-a[k]!=0)
				{
				m++;
				cha[m].jian(a[j],a[k]);
				if (cha[m].length==0) m--;
				}
			}
		num ans;
		ans=cha[1];
		for (int j=2;j<=m;j++)
			ans=gcd(ans,cha[j]);
		num x,y,z;
		x.mod(a[1],ans);
		y.jian(ans,x);
		z.mod(y,ans);
		fout<<"Case #"<<i<<": ";
		for (int j=z.length;j>0;j--)
			fout<<z.dig[j];
		fout<<"x"<<endl;
	}
	fout.close();
	//system("pause");
	return 0;
}


