#include<iostream>
#include<fstream>
using namespace std;
int add(int a,int b)
{
	int c;
	c=(a+b)%1000;
	return c;	
}

int subseq(string s1, string s2, int l1, int l2)
{
	if(s2[l2+1]=='\0')
	{
		int a=0;
		if(s1[l1]==s2[l2])
		{
			a=1;
		}
		if(s1[l1+1]=='\0')
		{
			return a;
		}	
		return add(a,subseq(s1,s2,l1+1,l2));
	}
	if(s1[l1+1]=='\0')
	{
		int a=0;
		return a;
	}
	if(s1[l1]==s2[l2])
	{
		return add(subseq(s1,s2,l1+1,l2+1),subseq(s1,s2,l1+1,l2));
	}	
	return subseq(s1,s2,l1+1,l2);
} 

int main(void)
{
	ifstream in;
	in.open("C-small-attempt0.in",ios::in);
	ofstream out;
	out.open("C.out",ios::in);
	int n;
	string s2="welcome to code jam";
	string s1;
	in>>n;
	int result;
	int i1,j1;
	int r[4];
	for(i1=0;i1<=n;i1++)
	{
		getline(in, s1);
		result=subseq(s1,s2,0,0);
		for(j1=0;j1<3;j1++)
		{
			r[3-j1]=result%10;
			result=result/10;
			if(result==0)
			{
				for(int k=0;k<3-j1;k++)
					r[k]=0;
			}
		}
		if(i1!=0)
			out<<"Case #"<<i1<<": "<<r[0]<<r[1]<<r[2]<<r[3]<<'\n';
	}
	return 0;
}
