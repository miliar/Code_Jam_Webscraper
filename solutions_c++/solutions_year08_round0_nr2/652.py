#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
#include <fstream>

using namespace std;

int min(int a,int b){return a<b?a:b;}

int hora(string s)
{
	return ((s[0]-48)*10+s[1]-48)*60+10*s[3]+s[4]-480-48;
};

void main()
{
	ifstream ff("datos.txt");
	ofstream re("res.txt");
	int n,i,j,t,a,b,nc,ha,nta,ntb,pa,pb,na,nb,lisa[1000],lisb[1000];
	string s;
	vector<int> sa,la,sb,lb,tda,tdb;
	ff>>n;
	for(nc=0;nc<n;nc++)
	{
		for(i=0;i<1000;i++) lisa[i]=lisb[i]=0;
		ha=0;nta=0;ntb=0;
		tda.clear();tdb.clear();
		sa.clear();sb.clear();la.clear();lb.clear();
		ff>>t;
		ff>>a;
		ff>>b;
		for(i=0;i<a;i++)
		{
			ff>>s; sa.push_back(hora(s));
			ff>>s; la.push_back(hora(s));
		}
		for(i=0;i<b;i++)
		{
			ff>>s; sb.push_back(hora(s));
			ff>>s; lb.push_back(hora(s));
		}
		while(ha<24*60)
		{
			pa=24*60;pb=24*60;
			for(i=0;i<sa.size();i++) if(pa>sa[i] && sa[i]>=ha &&lisa[i]==0) {pa=sa[i];na=i;}
			for(i=0;i<sb.size();i++) if(pb>sb[i] && sb[i]>=ha &&lisb[i]==0) {pb=sb[i];nb=i;}
			if (pa==1440 && pb==1440) break;
			if(pa<pb)
			{
				sort(tda.begin(),tda.end());
				if(tda.size()==0 ||tda[0]>pa) nta++;else tda[0]=2000;
				tdb.push_back(t+la[na]);
				lisa[na]=1;
				ha=pa;
			}
			else
			{
				sort(tdb.begin(),tdb.end());
				if(tdb.size()==0 ||tdb[0]>pb) ntb++;else tdb[0]=2000;
				tda.push_back(t+lb[nb]);
				lisb[nb]=1;
				ha=pb;
			}
		}
		re <<"Case #"<<nc+1<<": "<<nta<<" "<<ntb<<endl;
	}	
}
