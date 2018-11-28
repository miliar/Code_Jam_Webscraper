#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <conio.h>
using namespace std;

int main() 
{
	freopen("B-small-attempt8.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int K,num=0,y;
	char *cstr;
	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d", &K);
	for (int c = 0; c < K; ++c) 
	{
		int a[3], res=0, n=0,z=0;
		cout<<"Case #"<<c+1<<": ";
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
		//	cout<<temp<<'\n';

			if(n<3)
			{
				switch(n)
				{
				case 0:
					a[0]=temp;
					n++;
				//	temp=0;
					break;
				case 1:
					a[1]=temp;
					z=a[1];
					n++;
			//		temp=0;
					break;
				case 2:
					a[2]=temp;
					n++;
			//		cout<<"a2"<<a[2];
			//		temp=0;
					break;
				}
			}
			else
			{
			if(temp==0&&a[2]==0)
			{
				res++;
				continue;
			}
			else if(temp==0)
				continue;

			if(temp==1&&a[2]==1)
			{
				res++;
				continue;
			}
			else if(temp==1)
				continue;

			if(temp%3==0)
				y=temp/3;
			else
				y=temp/3+1;

			if(y>=a[2])
			{
				res++;
			}
			else if(z>0&&++y>=a[2])
			{
				res++;
				z--;
			}
			}
			}
	cout<<res<<'\n';
	////	res=0;
	}
}