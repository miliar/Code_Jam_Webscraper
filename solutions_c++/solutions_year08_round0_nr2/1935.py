#include<stdio.h>
#include<iostream>
#include<fstream>
#include<string.h>
#include<utility>
#include<vector>
#include<algorithm>

using namespace std;
bool comparex(pair<int,int> const& x, pair<int,int> const& y);

void display(int a, int b, int c)
{
	fstream f;
//	char *ch;
	f.open("answer.out",fstream::app|fstream::out);
	/*ch = strtok(str," ");
	while(ch)
	{
		f<<ch<<" ";
		ch = strtok(NULL," ");
	}*/
	f<<"Case #"<<c<<": ";
	f<<a<<" "<<b<<"\n";
	f.close();
}

int main()
{
	fstream f;
	char str[102];
	int l,n,m,w,x,y,z,a,b,c,d,t;
	int *k;
	int na,nb;

	vector< pair<int,int> > va,vb,fr;
	vector< int> ta,tb;


	f.open("B-small-attempt1.in",fstream::in);
	f.getline(str,102);
	sscanf(str,"%d",&a);
	l=1;
	while(l<=a)
	{
		//cout<<"case #"<<l<<":\n";
		f.getline(str,102);
		sscanf(str,"%d",&t);
		cout<<"t:"<<t<<endl;
		f.getline(str,102);
		sscanf(str,"%d %d",&na,&nb);

		for(m=1;m<=na;m++)
		{
			f.getline(str,102);
			sscanf(str,"%d:%d %d:%d",&w,&x,&y,&z);
			va.push_back(pair<int,int>(100*w+x,100*y+z));
		}

		for(m=1;m<=nb;m++)
		{
			f.getline(str,102);
			sscanf(str,"%d:%d %d:%d", &w,&x,&y,&z);
			vb.push_back(pair<int,int>(100*w+x,100*y+z));
		}
		
		sort(va.begin(),va.end(),comparex);
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
		while(x<va.size() || y<vb.size())
		{
			if(y>=vb.size())
			{
				if(ta.size())
				{
					if(va[x].first < (ta[0]+t))
						c++;
					else
						ta.erase(ta.begin());
				}
				else
					c++;
				x++;
			
			}
			else if(x>=va.size())
			{
				if(tb.size())
				{
				//	cout<<"(vb[y].first+t )"<<(vb[y].first+t )<<"tb[0]"<<tb[0]<<endl;
					if(vb[y].first < (tb[0]+t))
						d++;
					else
						tb.erase(tb.begin());
				}
				else
					d++;
				y++;
			}
			else
			{
				if(comparex(va[x],vb[y]))
				{	
					if(ta.size())
					{
						if(va[x].first < (ta[0]+t))
							c++;
						else
							ta.erase(ta.begin());
					}
					else
						c++;

					tb.push_back(va[x].second);
					sort(tb.begin(),tb.end());
					x++;
				}
				else
				{
					if(tb.size())
					{
						if(vb[y].first < (tb[0]+t))
							d++;
						else
							tb.erase(tb.begin());
					}
					else
						d++;
					ta.push_back(vb[y].second);
					sort(ta.begin(),ta.end());
					y++;
				
				}

			}
			
		}
		
		display(c,d,l);
		va.clear();
		vb.clear();
		ta.clear();
		tb.clear();
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
		return x.second<=y.second;
}