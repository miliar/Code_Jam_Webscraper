#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

void main()
{
	ifstream infile("input.txt");
	ofstream outfile("output.txt");
	long t,a,b;
	float x,p;
	infile>>t;
	for (int i=0;i<t;i++)
	{
		x=1;
		float s1=0,s2=0,s3=0,ans=0;
		infile>>a>>b;
		for (int j=0;j<a;j++)
		{
			float temp=x*(a-j+b-a+a-j+1)+(1-x)*(a-j+b-a+a-j+1+b+1);
			if (((temp-s2<1e-6)||(s2-0<1e-6))) s2=temp;
			infile>>p;
			x=x*p;
		}
		s1=(b+1-a)*x+(b+1+(b-a+1))*(1-x);
		s3=b+2;
		ans=s1;
		if (ans-s2>1e-6) ans=s2;
		if (ans-s3>1e-6) ans=s3;
		outfile.setf(ios::fixed, ios::floatfield);  // 设定为 fixed 模式，以小数点表示浮点数
		outfile.precision(6);  
		outfile<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	infile.close();
	outfile.close();
}
