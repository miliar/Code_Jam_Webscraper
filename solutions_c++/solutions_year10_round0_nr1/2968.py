#include<fstream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<math.h>

int div(int n)
{       int sum=0;
	for(int i=0;i<n;i++)
	{	sum=sum+pow(2,i);
	}
	return sum;
}

void main()
{	int t,n,k;
	//long int ;
	//char ;
	int chs;
	//long long int chl;
	//char chstr;
	fstream f,o;

	clrscr();
	f.open("inputa.in",ios::in);
	o.open("output.out",ios::out|ios::app);

	f>>chs;
	cout<<chs<<endl;
	t=chs;
	int d,cnt=0;

	for(int i=1;i<=t;i++)
	{       f>>chs;
		n=chs;
		cout<<n<<" ";
		f>>chs;
		k=chs;
		cout<<k<<" ";
		d=div(n);
		cout<<d<<endl;
		o<<"Case #"<<i<<": ";
		if(k<d)
		{	o<<"OFF"<<endl;
		}
		else if(k==d)
		{	o<<"ON"<<endl;
		}
		else if(k>d)
		{	while(k>=d)
			{	k=k-d;
				k--;
				cnt++;
			}
			if(k+1==0)
			{	o<<"ON"<<endl;
			}
			else
			{	o<<"OFF"<<endl;
			}
		}

		//o<<endl;
	}

	getch();
}