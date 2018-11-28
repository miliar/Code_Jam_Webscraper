#include<iostream>
#include<cstdio>
#include<string>
#include<map>
#include<set>
#include<vector>
#include<utility>

using namespace std;

void solve()
{	
	string str;
	vector<string> vstr;
	vector< pair<int,int> > vwp;
	vector<double> voowp,vowp;	
	int n,num,den,i,j;


	cin>>n;
	for(i=1;i<=n;i++){cin>>str;vstr.push_back(str);}


	//calc vwp

	for(i=0;i<vstr.size();i++)
	{
		num=den=0;
		for(j=0;j<vstr[i].size();j++)
		{
			if(vstr[i][j]=='1'){num++;den++;}
			else if(vstr[i][j]=='0')den++;
		}
		pair<int,int> pp(num,den);
		vwp.push_back(pp);
	}

	//calc vowp

	for(i=0;i<vstr.size();i++)
	{
		double x=0;int count=0;
		for(j=0;j<vstr.size();j++)
		{
			if(vstr[i][j]=='0'){count++;x=x+(double)(vwp[j].first-1)/(double)(vwp[j].second-1);}
			else if(vstr[i][j]=='1'){count++;x=x+(double)(vwp[j].first)/(double)(vwp[j].second-1);}
		
		}
		if(count>0)x/=(double)count;
		vowp.push_back(x);
	}
	
	//calc voowp

	for(i=0;i<vstr.size();i++)
	{
		double x=0;int count=0;

		for(j=0;j<vstr.size();j++)
		{
			if(i==j || vstr[i][j]=='.')continue;
			x+=vowp[j];
			count+=1;
		}
		if(count>0)x/=(double)count;
		voowp.push_back(x);
	}

	for(i=0;i<vstr.size();i++)
	{
		double x=0;
		
		if(vwp[i].second!=0)
			x=x+((double)vwp[i].first/(double)vwp[i].second)/4.0;
		//if(vowp[i].second!=0)
                //        x=x+((double)vowp[i].first/(double)vowp[i].second)/2.0;
		//if(voowp[i].second!=0)
                //        x=x+(double)(0.25*(double)((double)voowp[i].first/(double)voowp[i].second));
		
		x+=(vowp[i]/2.0);
		x+=(voowp[i]/4.0);
		//printf("%f\n",x);
		cout.precision(10);
		cout<<x<<endl;
	}
	return;
}

int main()
{
	int t,i;
	for(cin>>t,i=1;i<=t;i++)
	{
		printf("Case #%d:\n",i);

		solve();
	}

	return 0;
}
