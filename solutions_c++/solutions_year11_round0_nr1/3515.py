#include<iostream>
#include<fstream>
#include<cmath>
#include<conio.h>
#include<string>
using namespace std;
class button
{
public:
	int a;
	char c;
};
int time(int * orange,int sizeo,int * blue,int sizeb,button seq[],int size)
{
	bool flag=true;
	int blueb=1,orangeb=1;
	int Time=0;
	int i=0,j=0,k=0; 
	while(k<size)
	{
		if(i<sizeo)
		{
			if(orangeb>orange[i])
			{
				orangeb--;

			}
			else if(orangeb<orange[i] )
			{
				orangeb++;
				
			}
			else if(orangeb==orange[i])
			{
				if((seq[k].c=='O' || seq[k].c=='o') && seq[k].a==orangeb)
				{
					k++;
					i++;
					flag=false;
				}		
			}
		}
		if(j<sizeb)
		{
			if(blueb>blue[j] )
			{
				blueb--;

			}
			else if(blueb<blue[j])
			{
				blueb++;
			}
			else if(blueb==blue[j])
			{
				if((seq[k].c=='B' || seq[k].c=='b') && seq[k].a==blueb)
				{
					if(flag==true)
					{
						k++;
						j++;
					}
				}		
			}
		}
		flag=true;
		Time++;
	}
	return Time;
	
}
void main ()
{
	int T,n,bu,oi=0,ob=0,k=0;
	int o[100],b[100];
	char ch;
	button seq[100];
	ifstream in("A-large.in");
	ofstream out("output.txt");
	in>>T;
	for(int i=0; i<T; i++)
	{
		oi=0;
		ob=0;
		k=0;
		in>>n;
		in.get(ch);
		for(int j=0; j<n; j++)
		{
			in.get(ch);
			in>>bu;
			if(ch=='O' || ch=='o')
			{
				o[oi]=bu;
				seq[k].c='O';
				oi++;
			}
			else
			{
				b[ob]=bu;
				seq[k].c='B';
				ob++;
			}
			seq[k].a=bu;
			k++;
			in.get(ch);
		}
		int ans=time(o,oi,b,ob,seq,k);
		out<<"Case #"<<i+1<<": "<<ans;
		if(i+1!=T)
		{
			out<<endl;
		}
	}
}