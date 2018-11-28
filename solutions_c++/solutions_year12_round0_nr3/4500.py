#include<fstream>
#include<iostream>
#include<cmath>
using namespace std;

char st[100];
char st2[100];
ofstream out("output.txt");
int y;
int pow2(int a, int b)
{
	int res=1;
	while(b--)
		res*=10;
	return res;
}
int ncifre(int a)
{
	int c=0;
	while(a!=0)
	{
		c++;
		a/=10;
	}
	y=c;
	return c;
}
bool recycled(int n, int m)
{
	int hashA=0, hashB=0, hashA2=0, hashB2=0;
	sprintf(st, "%d", n);
	sprintf(st2, "%d", m);
	for(int i=0;st[i]!=0;i++)
	{
		hashB=hashB*10+st[i]-'0';
		hashB2=hashB2*10+st2[i]-'0';
	}
	//cout << n << " " << m << " " << hashA2 << endl;
	for(int i=0;st[i+1]!=0;i++)
	{
		hashA=hashA*10+st[i]-'0';
		hashB=hashB-(st[i]-'0')*pow2(10, y-i-1);
		hashA2=hashA2+(st2[y-i-1]-'0')*pow2(10, i);
		hashB2=hashB2/10;
		//cout <<  y << " " << hashA << " " << hashB << " " << hashA2 << " " << hashB2 <<" " << (st2[y-i-1]-'0')*pow(10, i)<< endl;
		if(hashA==hashA2&&hashB==hashB2)
			return true;
	}
	return false;
}
int main(void)
{
	FILE *fp=fopen("input.txt", "r");

	int x;
	fscanf(fp, "%d\n", &x);
	for(int p=1;p<=x;p++)
	{
		int A, B, conta=0;
		fscanf(fp, "%d %d", &A, &B);
		for(int n=A;ncifre(n)==ncifre(A);n++)
			for(int m=n+1;m<=B;m++)
			{
				if(recycled(n, m))
					conta++;
			}
		out << "Case #" << p << ": ";
		out << conta << endl;
	}
	out.close();
	fclose(fp);
}
