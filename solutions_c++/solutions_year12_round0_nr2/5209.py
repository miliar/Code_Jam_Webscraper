#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>

//char convert(char ch);

void main()
{
	clrscr();
	ifstream a("inputb.txt");
	ofstream b("outputb2.txt");
	int t,n,s,p,x[100];
	int count = 1;
	int size;
	if(!a)
		cout<<"unable to open file";
	a>>t;
	while(count<=t)
	{
		int res=0;
		a>>n>>s>>p;
		//cout<<n<<s<<p<<endl;
		for(int k=0;k<n;k++)
		{
			a>>x[k];
			//cout<<x[k];
		}
		for(int j=0;j<k;j++)
		{
			if(x[j] == 0 && p !=0)
				break;
			if(x[j]>=(p*3))
				res++;
			else if(x[j]>=(p*3)-2)
				res++;
			else if(s!= 0 && x[j]>=(p*3)-4)
			{
			    res++;
			    s--;
			}
		}
		b<<"Case #"<<count<<": "<<res;
		b<<endl;
		//cout<<count<<endl;
		count++;
	}
	getch();
}