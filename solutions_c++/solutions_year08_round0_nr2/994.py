#include<fstream>
#include<iostream>
using namespace std;
#include<string>
#include<vector>

int main()
{
	//ifstream fin("A-small.in");
	//ofstream fout("A-small.out");
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("B-large.out");
	
	int n;
	//char src[10000],tar[10000],val[10000];
	int tat,na,nb;
	string arr,dep;
	vector<int> aa,ba,ad,bd;
	
	fin>>n;
	for(int c=1; c<=n; c++)
	{
		fin>>tat;
		fin>>na>>nb;
		cout<<tat<<" "<<na<<" "<<nb<<"\n";
		aa.clear();
		ba.clear();
		ad.clear();
		bd.clear();
		for(int i=0;i<na;i++)
		{
			fin>>arr>>dep;
			int temp=0;
			temp=(((arr[0]-'0')*10)+(arr[1]-'0'))*60 + ((arr[3]-'0')*10)+(arr[4]-'0');
			ad.push_back(temp);
			temp=(((dep[0]-'0')*10)+(dep[1]-'0'))*60 + ((dep[3]-'0')*10)+(dep[4]-'0');
			ba.push_back(temp+tat);
		}			
		
		for(int i=0;i<nb;i++)
		{
			fin>>arr>>dep;
			int temp=0;
			temp=(((arr[0]-'0')*10)+(arr[1]-'0'))*60 + ((arr[3]-'0')*10)+(arr[4]-'0');
			bd.push_back(temp);
			temp=(((dep[0]-'0')*10)+(dep[1]-'0'))*60 + ((dep[3]-'0')*10)+(dep[4]-'0');
			aa.push_back(temp+tat);
		}
		
		sort( aa.begin( ), aa.end( ));
		sort( ad.begin( ), ad.end( ));
		sort( ba.begin( ), ba.end( ));
		sort( bd.begin( ), bd.end( ));
		
		int newa[na+nb],newb[na+nb];
		int i=0,j=0,k=0;
		while(i<nb&&j<na)
		{
			if(aa[i]<=ad[j])
			{
				newa[k++]=1;
				i++;
			}
			
			else
			{
				newa[k++]=-1;
				j++;
			}
		}
		if(i<nb)
		{
			while(i<nb)
			{
				newa[k++]=1;
				i++;
			}
		}
		else
		{
			while(j<na)
			{
				newa[k++]=-1;
				j++;
			}
		}
		i=0,j=0,k=0;
		while(i<na&&j<nb)
		{
			if(ba[i]<=bd[j])
			{
				newb[k++]=1;
				i++;
			}
			
			else
			{
				newb[k++]=-1;
				j++;
			}
		}
		if(i<na)
		{
			while(i<na)
			{
				newb[k++]=1;
				i++;
			}
		}
		else
		{
			while(j<nb)
			{
				newb[k++]=-1;
				j++;
			}
		}	
		
		int cnta=0,mina=0;
		for(i=0;i<na+nb;i++)
		{
			cnta+=newa[i];
			if(mina>cnta)
				mina=cnta;
		}
		int cntb=0;
		int minb=0;
		for(i=0;i<na+nb;i++)
		{
			cntb+=newb[i];
			if(minb>cntb)
				minb=cntb;
		}
		
		
		fout<<"Case #"<<c<<": "<<(-mina)<<" "<<(-minb)<<"\n";
	
	}
	
	return 0;
}

