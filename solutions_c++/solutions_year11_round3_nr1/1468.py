#include<iostream>
#include<cmath>
#include<string>
#include<algorithm>
#include<fstream>
#include<vector>
#include<map>
using namespace std;
int main()
{
	ifstream cin("A-large.in");

	ofstream cout("A-small.out");
	int T;
	cin>>T;
	int x=1;
	char grid[51][51];
	while(T--)
	{
		int R,C;
		cin>>R>>C;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
				cin>>grid[i][j];
		}
		bool poss=true;
		for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				if(grid[i][j]=='#')
				{
					grid[i][j]='/';
					if(i==R-1||j==C-1||grid[i+1][j+1]=='.'||grid[i+1][j]=='.'||grid[i][j+1]=='.')
						poss=false;
					grid[i+1][j+1]='/';
					grid[i][j+1]='\\';
					grid[i+1][j]='\\';
				}
			}
		}
		cout<<"Case #"<<x++<<":"<<endl;
		if(!poss)
			cout<<"Impossible"<<endl;
		else
		{
			for(int i=0;i<R;i++)
		{
			for(int j=0;j<C;j++)
			{
				cout<<grid[i][j];
			}
			cout<<endl;
			}
		}
	}
}
/*
int main()
{
	ifstream cin("C-small-attempt0.in");

	ofstream cout("C-small.out");
	int T;
	cin>>T;
	int x=1;
	while(T--)
	{
		int N,L,H;
		cin>>N>>L>>H;
		int freq[10000];
		for(int i=0;i<N;i++)
			cin>>freq[i];
		bool poss;
		int note;
		for(int i=L;i<=H;i++)
		{
			poss=true;
			
			for(int j=0;j<N;j++)
			{
				if(freq[j]%i!=0&&i%freq[j]!=0)
				{
					poss=false;
				}
			}
			if(poss)
			{
				note =i;
				break;
			}

		}

		cout<<"Case #"<<x++<<": ";
		if(poss)
			cout<<note<<endl;
		else
			cout<<"NO"<<endl;
	}
}
*/
/*
int main()
{
	int T;
	cin>>T;
	int x=1;
	while(T--)
	{
		int N;
		cin>>N;
		char win[100][100] ;
		for(int i=0;i<N;i++)
			for(int j=0;j<N;j++)
				cin>>win[i][j];
		double wp [100];
		double owp[100];
		double wpr[100][100];
		int game[100];
		double* oowp = new double[N];
		int play[100][100];
		for(int i=0;i<N;i++)
		{	
			for(int j=0;j<N;j++)
			{
				play[i][j]=-1;
				wpr[i][j]=0;
			}
		}
		for(int i=0;i<N;i++)
		{
			int c=0;
			int d=0;
			for(int j=0;j<N;j++)
			{
				if(win[i][j]=='0'||win[i][j]=='1')
				{
					d++;
					if(win[i][j]=='1')
					{
						c++;
						play[i][j]=1;
						play[j][i]=0;
					}

				}
			}
			wp[i]=c/(double)d;/*
							  for(int j=0;j<N;j++)
							  {
							  if(i==j)
							  continue;
							  if(play[i][j]==1)
							  wpr[j][i]=(c-1)/(double)(d-1);
							  else if(play[i][j]==0)
							  wpr[j][i]=(c)/(double)(d-1);
							  else
							  wpr[j][i]=0;
							  }
			game[i]=d;

		}
		for(int i=0;i<N;i++)
		{
			int count=0;
			for(int j=0;j<N;j++)
			{
				if(i==j)
				{
					wpr[i][j]=-1;
					continue;
				}
				if(win[j][i]=='.')
				{
					wpr[i][j]=-1;
					continue;
				}
				else
					count++;
				int c=0,d=0;
				for(int k=0;k<N;k++)
				{
					if(k!=i&&j!=k)
					{
						if(win[j][k]=='1')
							c++,d++;
						else if(win[j][k]=='0')
							d++;

					}

				}

				wpr[i][j]=c/(double)d;
			}
		}
		for(int i=0;i<N;i++)
		{
			double avg=0;
			int count=0;
			for(int j=0;j<N;j++)
			{
				if(i==j)
					continue;
				if(wpr[i][j]!=-1)
					{
						avg+=wpr[i][j];
						count++;
					}


			}
			owp[i]=avg/count;
		}
		for(int i=0;i<N;i++)
		{
			double avg=0;
			for(int j=0;j<N;j++)
			{
				if(i!=j)
					avg+=owp[j];
			}
			oowp[i]=avg/N-1;

		}
		cout<<"Case #"<<x++<<endl;
		for(int i =0;i<N;i++)
		{
			cout<<.25*wp[i]+.5*owp[i]+.25*oowp[i]<<endl;
		}
	}
	return 0;
}*//*
 int main()
 {
 int T;
 cin>>T;
 int x=1;
 while(T--)
 {
 int N, Pd, Pg;
 cin>>N>>Pd>>Pg;
 bool possible=false;
 for(int i=N;i>-1;i--)
 {
 double a = i*(Pd/100.0);
 int b = a;
 b = (a-b)*100;
 if(b!=0)
 {
 continue;
 }
 int c = i;
 double d = Pg/100.0;
 d=c*d;
 while(d!=floor(d))
 {
 c++;
 d=c*d;
 }


 }
 cout<<"Case #"<<x++;
 }

 return 0;
 }*/
/*
int main()
{
ifstream cin("B-large.in");

ofstream cout("B-small.out");
int T;
cin>>T;
int x=1;
while(T--)
{
int C;
cin>>C;
map<string,char> nonB;
for(int i=0;i<C;i++)
{
string el;
cin>>el;
string sEl = el.substr(0,2);
if(sEl[0]>sEl[1])
swap(sEl[0],sEl[1]);
nonB[sEl]=el[2];
}
int D;
cin>>D;
map<char,string> opp;
for(int i=0;i<D;i++)
{
string op;
cin>>op;
if(opp[op[0]].empty())
{
opp[op[0]]="";

}
opp[op[0]].push_back(op[1]);
if(opp[op[1]].empty())
{
opp[op[1]]="";

}
opp[op[1]].push_back(op[0]);
}
int N;
cin>>N;
string list="";
for(int i=0;i<N;i++)
{
char e;
cin>>e;
if(list=="")
{
list.push_back(e);
continue;
}
string com = "";
com.push_back(e);
com+=list[list.size()-1];
if(com[0]>com[1])
swap(com[0],com[1]);
if(nonB[com]!=0)
{
list.pop_back();
list.push_back(nonB[com]);
}
else
{
for(int j=0;j<list.size();j++)
{
if(opp[e].find(list[j])!=list.npos)
{
list.clear();
break;
}
}
if(!list.empty())
list.push_back(e);
}
}
cout<<"Case #"<<x++<<": [";
for(int j=0;j<list.size();j++)
{
if(j!=list.size()-1)
cout<<list[j]<<", ";
else
cout<<list[j];
}
cout<<"]"<<endl;
}
return 0;

}*/
/*
Problem 1: Bot Trust
int main()
{ifstream cin("A-large.in");
int T;
cin>>T;
int x=1;

ofstream cout("A-small.out");
while(T--)
{
int N,t=0;
cin>>N;

vector<pair<char,int> > seq;
for(int i=0;i<N;i++)
{
pair<char,int> p;
cin>>p.first;
cin>>p.second;
seq.push_back(p);
}
int blueP = 1;
int orangeP = 1;
for(int i=0;i<N;i++)
{
if(seq[i].first=='O')
{

int firstB = 0;
for(int j=i+1;j<N;j++)
{
if(seq[j].first=='B')
{
firstB=j;
break;
}
}

while(orangeP<seq[i].second)
{
orangeP++;
t++;
if(seq[firstB].second>blueP)
blueP++;
else if(seq[firstB].second<blueP)
blueP--;

}
while(orangeP>seq[i].second)
{
orangeP--;
t++;
if(seq[firstB].second>blueP)
blueP++;
else if(seq[firstB].second<blueP)
blueP--;

}
t++;
if(seq[firstB].second>blueP)
blueP++;
else if(seq[firstB].second<blueP)
blueP--;
}
else
{

int firstB = 0;
for(int j=i+1;j<N;j++)
{
if(seq[j].first=='O')
{
firstB=j;
break;
}
}
while(blueP<seq[i].second)
{
blueP++;
t++;
if(seq[firstB].second>orangeP)
orangeP++;
else if(seq[firstB].second<orangeP)
orangeP--;

}
while(blueP>seq[i].second)
{
blueP--;
t++;
if(seq[firstB].second>orangeP)
orangeP++;
else if(seq[firstB].second<orangeP)
orangeP--;

}
t++;
if(seq[firstB].second>orangeP)
orangeP++;
else if(seq[firstB].second<orangeP)
orangeP--;
}

}
cout<<"Case #"<<x++<<": "<<t<<endl;

}
return 0;
}
*/