#include <iostream>
using namespace std;

#define MAX_N 100
#define abs(n) (((n)>0) ? (n) : -(n))

void input(int d[],char r[],int &n2);
void process(int d[],char r[],int &n2,int &sec);
void output(int i,int sec);

void main()
{
	int n,d[MAX_N];
	char r[MAX_N+1];
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int sec=0;
		int n2;
		input(d,r,n2);
		process(d,r,n2,sec);
		output(i,sec);
	}
}

void input(int d[],char r[],int &n2)
{
	cin >> n2;
	for(int i=0;i<n2;i++)
		cin >> r[i] >> d[i];
}

void process(int d[],char r[],int &n2,int &sec)
{
	int o_t=0,o_p=1,b_t=0,b_p=1;
	for(int i=0;i<n2;i++)
	{
		if(r[i]=='O')
		{
			int t=o_t+abs(o_p-d[i]);
			if(t>sec)
				sec=t;
			sec++;
			o_p=d[i];
			o_t=sec;
		}
		if(r[i]=='B')
		{
			int t=b_t+abs(b_p-d[i]);
			if(t>sec)
				sec=t;
			sec++;
			b_p=d[i];
			b_t=sec;
		}
	}
}

void output(int i,int sec)
{
	cout << "Case #" << i+1 << ": " << sec << endl;
}