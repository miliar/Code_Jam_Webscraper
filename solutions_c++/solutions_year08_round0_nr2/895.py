#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <algorithm>

using namespace std;

#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

int main()
{
	int nt,num=0;
	scanf("%d\n",&nt);
	while (num++<nt)
	{
		int t,na,nb,ansa=0,ansb=0,hh,mm,dp,lv,tmp;
		int d[202],l[202],wh[202];// wh[i] = 1 - from A, 2 - from B
		vector<int> ta,tb;
		string s;

		memset(d,0,sizeof(d));
		memset(l,0,sizeof(l));
		memset(wh,0,sizeof(wh));
		ta.clear();
		tb.clear();

		scanf("%d\n",&t);
		scanf("%d %d\n",&na,&nb);
		for(int i=0;i<na;i++)
		{
			getline(cin,s);
			hh=(s[0]-'0')*10+(s[1]-'0');
			mm=(s[3]-'0')*10+(s[4]-'0');
			dp=hh*60+mm;
			hh=(s[6]-'0')*10+(s[7]-'0');
			mm=(s[9]-'0')*10+(s[10]-'0');
			lv=hh*60+mm;		
			d[i]=dp;
			l[i]=lv;
			wh[i]=1;
		}
		for(int i=0;i<nb;i++)
		{
			getline(cin,s);
			hh=(s[0]-'0')*10+(s[1]-'0');
			mm=(s[3]-'0')*10+(s[4]-'0');
			dp=hh*60+mm;
			hh=(s[6]-'0')*10+(s[7]-'0');
			mm=(s[9]-'0')*10+(s[10]-'0');
			lv=hh*60+mm;		
			d[na+i]=dp;
			l[na+i]=lv;
			wh[na+i]=2;
		}
		for(int i=0;i<na+nb;i++)
			for(int j=i+1;j<na+nb;j++)
				if((d[i]>d[j])||(d[i]==d[j]&&l[i]>l[j]))
				{
					tmp=d[i];
					d[i]=d[j];
					d[j]=tmp;
					tmp=l[i];
					l[i]=l[j];
					l[j]=tmp;
					tmp=wh[i];
					wh[i]=wh[j];
					wh[j]=tmp;
				}
		for(int i=0;i<na+nb;i++)
		{
			//deb(d[i]);
			//deb(l[i]);
			//deb(wh[i]);
			if(wh[i]==1)
			{
				if(ta.size()>0&&ta[0]<=d[i])
				{
					ta.erase(ta.begin());
				}
				else
				{
					ansa++;
				}
				tb.push_back(l[i]+t);
				sort(tb.begin(),tb.end());
			}
			else
			{
				if(tb.size()>0&&tb[0]<=d[i])
				{
					tb.erase(tb.begin());
				}
				else
				{
					ansb++;
				}
				ta.push_back(l[i]+t);
				sort(ta.begin(),ta.end());
			}
		}

		cout<<"Case #"<<num<<": "<<ansa<<" "<<ansb<<endl;
	}
	return 0;	
}
