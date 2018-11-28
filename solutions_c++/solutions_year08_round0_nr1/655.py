#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <fstream>

int min(int a,int b){return a<b?a:b;}

using namespace std;

int sol(vector<string> se, vector<string>qu,int nq,int ne);
int ult(vector<string> qu,string st,int pos);

void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,s,q,i,nc,m,p,mp,pos;
	vector<string> se,qu;
	char c[100];
	ff>>n;
	for(nc=0;nc<n;nc++)
	{
		se.clear();qu.clear();m=0;
		ff>>s;
		//for(i=0;i<s;i++) {ff>>b;se.push_back(b);}
		ff.getline(c,100);
		for(i=0;i<s;i++) {ff.getline(c,100);se.push_back(c);}
		ff>>q;
		ff.getline(c,100);
		for(i=0;i<q;i++) {ff.getline(c,100);qu.push_back(c);}
		pos=qu.size();
		while(pos>-1)
		{
			p=1000;
			for(i=0;i<s;i++) p=min(p,ult(qu,se[i],pos));
			pos=p; m++;
		}
		//for(i=0;i<s;i++) m=min(m,sol(se,qu,0,i));
		re <<"Case #"<<nc+1<<": "<<m-1<<endl;
	}	
}

int ult(vector<string> qu,string st,int pos)
{
	for(int i=0;i<pos;i++) if(qu[pos-i-1]==st)return pos-i;
	return -1;
}

int sol(vector<string> se, vector<string>qu,int nq,int ne)
{
	int k,i=0,m=1000,t;
	while(nq+i<qu.size() && qu[nq+i]!=se[ne])
		i++;
	if(nq+i==qu.size()) return 0;
	for(k=0;k<se.size();k++)
	{
		if(se[k]!=se[ne])
		{
			t=sol(se,qu,nq+i,k);
			if(t<m)m=t;
		}
	}
	return m+1;
}