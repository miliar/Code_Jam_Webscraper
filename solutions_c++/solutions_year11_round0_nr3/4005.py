#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

string B[1000001];
void suma(int i)
{
	B[i]=B[i-1];
	int tam=B[i-1].size();
	
	if(B[i-1][tam-1]=='0')
		B[i][tam-1]='1';
	else
	{
		int q=0;	
		while(B[i][tam-1-q]=='1')
		{
			B[i][tam-1-q]='0';
			q++;
		}
		if(tam-1-q<0)
			B[i].insert(0,"1");
		else
			B[i][tam-1-q]='1';
	}
}
string sum(string a,string b)
{
	string tmp=b;
	if(a.size()>b.size())
	{
		b=a;
		a=tmp;
	}	

	int tam=a.size();
	for(int i=0;i<a.size();i++)
	{
		if(b[b.size()-1-i]=='0')
			b[b.size()-1-i]=a[a.size()-1-i];
		else
		{
			if(a[a.size()-1-i]=='1')
				b[b.size()-1-i]='0';
			else
				b[b.size()-1-i]='1';
		}
	}
	while(b[0]=='0')
		b.erase(0,1);
	
	if(b.empty())
		b="0";	
	return b;
}


int busc(int C[1005],int n)
{

	if(n==2 && C[0]==C[1])
		return C[0];
		
	
	string ST="0";
	for(int i=0;i<n;i++)
		ST=sum(ST,B[C[i]]);
		
	if(ST!="0")
		return -1;
	

	int r=-1;
	for(int k=1;k<n-1;k++)			//cuando agarro k candys para 1
	{
	
		for(int i=0;i<n;i++)		//agarrando el candy i
		{
			int r1=0;
			string S1="0",S2="0";
			
			for(int j=i;j<k;j++)
			{
				S1=sum(S1,B[C[i+j]]);
			}
			
			for(int j=i+k;j<n;j++)
			{
				S1=sum(S1,B[C[i+j]]);
			}
			if(S1==S2)
			{
				for(int j=i;j<k;j++)
					r1+=C[i+j];
				r=max(r,r1);
				r1=0;
				for(int j=i+k;j<n;j++)
					r1+=C[i+j];
				r=max(r,r1);
			}
		}
	}

	return r;
}


int main()
{
	B[0]="0";
	for(int i=1;i<1000001;i++)   //binary
		suma(i);


	int t,n,c,iter=1;
	
	scanf("%d",&t);
	while(iter<=t)
	{
		int C[1005]; //numeros a usar
		
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%d",&C[i]);
			
		sort(C,C+n);
		
		int res=busc(C,n);
		
		if(res==-1)
			printf("Case #%d: NO\n",iter);
		else
			printf("Case #%d: %d\n",iter,res);
		iter++;
	}
}
