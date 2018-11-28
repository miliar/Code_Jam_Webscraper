#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;
bool comparex(int const& x, int const& y);
void display2(int l);
void display(int c,int l)
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
	f<<"Case #"<<l<<": ";
	f<<c;
	f<<endl;
	f.close();
}

void display2(int l)
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
	f<<"Case #"<<l<<": ";
	
	f<<endl;
	f.close();
}


int main()
{
	fstream f;
	char str[10000];
	int l,n,m,w,x,y,z,a,b,c,d,t;
	int *k;
	int na,nb,nc;
	char *str2;

	vector<int> ta,tb;


	f.open("A-small-attempt0.in",fstream::in);
	f.getline(str,102);
	sscanf(str,"%d",&a);
	l=1;
	while(l<=a)
	{
		//cout<<"case #"<<l<<":\n";
		f.getline(str,10000);
		sscanf(str,"%d %d %d",&na,&nb,&nc);

		cout<<endl<<"na:"<<na<<"nb:"<<nb<<"nc:"<<nc<<endl;
		if((na*nb) < nc)
		{
			display2(l);
			continue;
		}
		k = (int *)malloc(nb*sizeof(int));

		for(m=0;m<nb;m++)
		{
			k[m]=na;
		}

		f.getline(str,10000);
		b =0;
		str2 = strtok(str," ");
		while(b != nc)
		{
			sscanf(str2,"%d",&c);
			ta.push_back(c);
			str2 = strtok(NULL," ");
			b++;
		}
		sort(ta.begin(),ta.end(),comparex);		

		//cout<<"size:"<<ta.size()<<endl;
		
	/*	for(m=0;m<x;m++)
		{
			cout<<ta[m]<<" ";
		}*/
		cout<<endl<<"ta:";
		for(m=0;m<nc;m++)
		{
			cout<<ta[m];
		}
		
		sort(ta.begin(),ta.end(),comparex);	
		y=0;
		z=0;
		for(m=0;m<nc;m++)
		{
			if(k[y]!=0)
			{
				z=z+(na-k[y]+1)*ta[m];
				k[y]--;
				y++;
			}
			if(y==nb)
				y=0;
		}

		cout<<endl<<"ans:"<<z<<endl;
		display(z,l);

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
		ta.clear();
		l++;
	}

	f.close();
	return 0;
}

bool comparex(int const& x, int const& y)
{
	return x>y;
}