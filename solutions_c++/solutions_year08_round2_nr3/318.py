#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;
bool comparex(pair<int,int> const& x, pair<int,int> const& y);

void display(int *a, vector<int> b, int c,int l)
{
	fstream f;
	int i;
//	char *ch;
	f.open("answer.out",fstream::app|fstream::out);
	/*ch = strtok(str," ");
	while(ch)
	{
		f<<ch<<" ";
		ch = strtok(NULL," ");
	}*/
	f<<"Case #"<<l<<":";
	for(i=0;i<b.size();i++)
	{
		f<<" "<<a[b[i]];
	}
	f<<endl;
	f.close();
}

int main()
{
	fstream f;
	char str[3000];
	int l,n,m,w,x,y,z,a,b,c,d,t;
	int *k;
	int na,nb;
	char *str2;

	vector<int> ta,tb;


	f.open("C-small-attempt1.in",fstream::in);
	f.getline(str,102);
	sscanf(str,"%d",&a);
	l=1;
	while(l<=a)
	{
		//cout<<"case #"<<l<<":\n";
		f.getline(str,3000);
		sscanf(str,"%d",&na);

		f.getline(str,3000);
		sscanf(str,"%d",&nb);
		cout<<"str"<<str;
		str2 = strtok(str," ");
		str2 = strtok(NULL," ");
		cout<<endl<<"str2:"<<str2<<endl;
		cout<<endl<<"na:"<<na<<"nb:"<<nb<<endl;

		k= (int*)malloc((na+1)*sizeof(int));
		x=nb;
		
		while(nb)
		{
			sscanf(str2,"%d",&t);
			//cout<<t;
			ta.push_back(t);
			str2= strtok(NULL," ");
			nb--;
		}
		cout<<"size:"<<ta.size()<<endl;
		
	/*	for(m=0;m<x;m++)
		{
			cout<<ta[m]<<" ";
		}*/
		for(m=1;m<=na;m++)
		{
			k[m]=0;
		}
		y=1;
		z=1;
		b=1;
		m=1;
		while(z<=na)
		{
			while(1)
			{
				if(k[m]==0)
				{
					if(y==z)
					{
						k[m]=z;
						y++;
						break;
					}
					y++;
				}
				m++;
				if(m>na)
					m=1;
			}
			b=m;
			y=1;

			z++;
		}
		cout<<endl<<"ans:";
		display(k,ta,na,l);
	/*	for(m=1;m<=na;m++)
		{
			cout<<k[m]<<" ";
		}
	*/	
	/*	sort(va.begin(),va.end(),comparex);
		sort(vb.begin(),vb.end(),comparex);
		cout<<"va:\n";
		for(m=0;m<na;m++)
		{
			cout<<va[m].first<<"<->"<<va[m].second<<endl;
		}
		cout<<"vb:\n";
		for(m=0;m<nb;m++)
		{
			cout<<vb[m].first<<"<->"<<vb[m].second<<endl;
		}

		x=0;y=0;c=0;d=0;
	


		
		display(c,d,l);
		va.clear();
		vb.clear();
		ta.clear();
		tb.clear();*/
		free(k);
		ta.clear();
		l++;
	}

	f.close();
	return 0;
}

bool comparex(pair<int,int> const& x, pair<int,int> const& y)
{
	if(x.first<y.first)
		return true;
	else if(x.first>y.first)
		return false;
	else
		return x.second<y.second;
}