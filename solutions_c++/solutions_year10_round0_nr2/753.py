#include<iostream>
	using namespace std;
#include<fstream>
long long  gcd(long long  a,long long  b)
{
	if (a<b) return gcd(b,a);
	else if (b==0) return a;
	else return gcd(b,a%b);
}
long long lcm(long long a,long long b)
{
	if (a*b==0) return 0;
	else return a*b/gcd(a,b);
}
int main()
{
	ifstream in;
	ofstream out;
	in.open("B-small-attempt1.in ");
	out.open("out.txt");
	int C,s=0;
    in>>C;
	while (C--)
	{
		int n,T,i,y,j,k=0,common;
		int a[3],d[3];
		long long multi;
		s++;
        in>>n;
		for (i=0;i<n;i++)
			in>>a[i];
		for (i=0;i<n-1;i++)
			for (j=i+1;j<n;j++)
				d[k++]=a[i]-a[j]>0?a[i]-a[j]:a[j]-a[i];
		if (n==3)
			common=gcd(gcd(d[0],d[1]),d[2]);
		else common=d[0];
		for (i=0;i<n;i++)
			a[i]+=common;
		if (a[0]%common==0) y=0;
		else y=common*(a[0]/common+1)-a[0];
			out<<"Case #"<<s<<": "<<y<<endl;
	}
	return 0;
}