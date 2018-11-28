#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<numeric>
#include<cmath>

#include<fstream>

using namespace std;


double WP(string s)
{
	int win=0,game=0,i;

	for(i=0;i<s.size();++i)
	{
		if(s[i]!='.')
			++game;
		if(s[i]=='1')
			++win;
	}

	return (double)win/game;
}

double NWP(string s,int idx)
{
	int win=0,game=0,i;

	for(i=0;i<s.size();++i)
	{
		if(i!=idx && s[i]!='.')
			++game;
		if(i!=idx && s[i]=='1')
			++win;
	}

	return (double)win/game;
}

double OWP(vector<string> &s,int idx)
{
	int i;
	double ret=0,n=0;

	for(i=0;i<s[0].size();++i)
		if(s[idx][i]!='.')
			++n;

	for(i=0;i<s.size();++i)
		if(i!=idx && s[i][idx]!='.')
			ret+=NWP(s[i],idx);

	return ret/n;
}

double OOWP(vector<string> &s,int idx)
{
	int i;
	double ret=0,n=0;

	for(i=0;i<s[0].size();++i)
	{
		if(s[idx][i]!='.')
		{
			ret+=OWP(s,i);
			++n;
		}
	}

	return ret/n;
}

vector<double> f(vector<string> s)
{
	int i;
	double wp,owp,oowp,dt;
	vector<double> ret;

	for(i=0;i<s.size();++i)
	{
		wp=WP(s[i]);
		owp=OWP(s,i);
		oowp=OOWP(s,i);

		dt=0.25*wp+0.5*owp+0.25*oowp;
		ret.push_back(dt);
	}


	return ret;
}

void main()
{
	int i,j,num,n;
	string s,ret;
	vector<double> r;
	vector<string> vs;
	ifstream fin("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\Google code jam\\A-large\\A-large.in");
	ofstream fout("C:\\Documents and Settings\\Administrator\\×ÀÃæ\\Google code jam\\A-large\\A-small.txt");
	
	fin>>num;

	for(i=1;i<=num;++i)
	{
		fin>>n;
		vs.clear();

		for(j=1;j<=n;++j)
		{
			fin>>s;
			vs.push_back(s);
		}

		r=f(vs);

		//Case #1: OFF
		char number[100];
		itoa(i,number,10);
		string nn(number);

		ret="Case #"+nn+": ";
		fout<<ret<<endl;
		for(j=0;j<r.size();++j)
			fout<<r[j]<<endl;
	}

/*	int i;
	string s[]={".11.","0.00","01.1",".10."};
	vector<string> vs(s,s+4);

	vector<double> vd=f(vs);
	for(i=0;i<vd.size();++i)
		cout<<vd[i]<<endl;*/
}
