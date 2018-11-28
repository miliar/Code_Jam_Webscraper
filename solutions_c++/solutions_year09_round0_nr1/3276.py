#include<iostream>
#include<math.h>
#include<cmath>
#include<string>
#include<vector>
#include<list>
#include<fstream>
using namespace std;
int main()
{
	int l,d,n,i,j,num,k,sum,a[15][27],m;
	string s[5000],s1;
	ofstream outfile;
	ifstream infile;
	infile.open ("A-small-attempt4.in");
	outfile.open ("f.out");
	infile>>l>>d>>n;
	for(i=0;i<d;i++)
		infile>>s[i];
	for(i=0;i<n;i++)
	{
		for(k=0;k<15;k++)
			for(j=0;j<27;j++)
			a[k][j]=0;
		infile>>s1;
		j=0;
		for(m=0;m<s1.length ();m++)
		{
			if(s1[m]=='(')
			{
				while(s1[m]!=')')
					a[j][s1[m++]-'a']=1;
				j++;
				continue;
			}
			else
				a[j++][s1[m]-'a']=1;
		}
		/*for(m=0;m<j;m++)
		{
			for(k=0;k<26;k++)
				cout<<a[m][k];
			cout<<endl;
		}*/
		sum=0;
		for(m=0;m<d;m++)
		{
			num=0;
			for(k=0;k<j;k++)
				if(a[k][s[m][k]-'a']!=1)
					num=1;
			if(num==0)
				sum++;
		}
		outfile<<"Case #"<<i+1<<": "<<sum<<endl;
	}
	infile.close ();
	outfile.close ();
	return 0;
}