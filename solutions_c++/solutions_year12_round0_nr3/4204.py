#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <conio.h>

using namespace std;

int check(int n,int m)
{
	int d=m,res=0;
	//cout<<n<<m;
	//while(d>0)
	//{
	//	d=d/10;
	//	i++;
	//}
	d=n;
	while(d<=m)
	{
		int x=d;
		int k,t=x,l=0;
		while(t>0)
		{
			t=t/10;
			l++;
		}
		for(int j=1;j<l;j++)
		{
			
			int m1=x%10;
			x=x/10;
			int a=1;
			for(k=0;k<l-1;k++)
				a=a*10;
			x=x+m1*a;
			if((x>d) && (x<=m)&&(x/a)!=0) 
			{
					res++;
					//cout<<x<<"if\n";
			}
		}
		d++;
	}
	return res;
}

void main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);
	int K,num=0,x,y;
	char *cstr;
	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &K);
	for (int c = 0; c < K; ++c) 
	{
		int a[2], i=0;
		a[0]=0;
		getline(cin, s);
		string t;
		stringstream ss(s);
		while (ss >> t)
		{
			int temp=0;
			cstr = new char [t.size()+1];
			strcpy (cstr, t.c_str());
			int l=strlen(cstr);
			for(int i=0;i<l;i++)
			{
				temp=temp*10 + (cstr[i]-'0');
			}
			a[i]=temp;
			i++;
		}
		cout<<"Case #"<<c+1<<": "<<check(a[0],a[1])<<'\n';
	}
}