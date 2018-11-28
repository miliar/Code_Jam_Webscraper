#include<iostream>
#include<string>

using namespace std;


char mas[510];
int b [510][3];
int output_answer;
int length;
string s = "welcome to code jam";
int slength=19;


void funct_go()
{
	int i,j;
	for(i=0;i<length;++i)
		b[i][0]=b[i][1]=b[i][2]=0;
	output_answer=0;
	for(i=0;i<length;++i)
	{
		if(mas[i]=='w')
		{
			b[i][0]=1;
			continue;
		}
		if(mas[i]=='e')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='w')
					b[i][0]+=b[j][0];
				if(mas[j]=='m')
					b[i][1]+=b[j][0];
				if(mas[j]=='d')
					b[i][2]+=b[j][0];
			}
		}
		if(mas[i]=='l')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='e')
					b[i][0]+=b[j][0];
			}
		}
		if(mas[i]=='c')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='l')
					b[i][0]+=b[j][0];
				if(mas[j]==' ')
					b[i][1]+=b[j][1];
			}
		}
		if(mas[i]=='o')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='t')
					b[i][1]+=b[j][0];
				if(mas[j]=='c')
				{
					b[i][0]+=b[j][0];
					b[i][2]+=b[j][1];
				}
			}
		}
		if(mas[i]=='m')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='a')
					b[i][1]+=b[j][0];
				if(mas[j]=='o')
					b[i][0]+=b[j][0];
			}
		}
		if(mas[i]==' ')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='o')
					b[i][1]+=b[j][1];
				if(mas[j]=='e')
				{
					b[i][0]+=b[j][1];
					b[i][2]+=b[j][2];
				}
			}
		}
		if(mas[i]=='t')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]==' ')
					b[i][0]+=b[j][0];
			}
		}
		if(mas[i]=='d')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='o')
					b[i][0]+=b[j][2];
			}
		}
		if(mas[i]=='j')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]==' ')
					b[i][0]+=b[j][2];
			}
		}
		if(mas[i]=='a')
		{
			for(j=i-1;j>=0;--j)
			{
				if(mas[j]=='j')
					b[i][0]+=b[j][0];
			}
		}
		b[i][0]=b[i][0]%10000;
		b[i][1]=b[i][1]%10000;
		b[i][2]=b[i][2]%10000;
	}
	for(i=0;i<length;++i)
		if(mas[i]=='m')
			output_answer=(output_answer+b[i][1])%10000;
	
}

void print ( int x )
{
	if(x<1000)
		cout<<'0';
	if(x<100)
		cout<<'0';
	if(x<10)
		cout<<'0';
	cout<<x<<endl;
}


int main()
{
	freopen("output.txt","w",stdout);
	int n;
	cin>>n;
	char zibil;
	cin.get(zibil);
	int i;
	for(i=0;i<n;++i)
	{
		cin.getline(mas,510,'\n');
		length=strlen(mas);
		cout<<"Case #"<<i+1<<": ";
		funct_go();
		print(output_answer);
	}
	return 0;
}