#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<queue>
using namespace std;
struct train
{
	string s,e;
	int p;
	bool operator <(const train aaa)
	{
		if(s==aaa.s)return e<aaa.e;
		return s<aaa.s;
	}
}t[205];
bool flag[205];
int time;
string ch(string a)
{
	string i;
	i+=a[0];
	i+=a[1];
	i+=a[3];
	i+=a[4];
	i+='\0';
	return i;
}

bool cmp(string a,string b)
{
	int x=((a[0]-'0')*10+(a[1]-'0'))*60+((a[2]-'0')*10+a[3]-'0');
	int y=((b[0]-'0')*10+(b[1]-'0'))*60+((b[2]-'0')*10+b[3]-'0');
	int z=time;
	return (x-y-z>=0);
}


int main()
{
	ifstream cin("B-large.in");
    ofstream cout("abcd");
	int c;
	cin>>c;
	int die;
	int na,nb;
	int i;
	int a;
	int ans[2];
	train temp;
	int j;
	int t_s;
	string	tt;
	string x,y;
	for(die=1;die<=c;die++)
	{
		memset(flag,0,sizeof(flag));
		cin>>time;
		cin>>na>>nb;
		ans[0]=ans[1]=0;
		for(i=0;i<na;i++)
		{
			cin>>x>>y;
			t[i].s=ch(x);t[i].e=ch(y);
			t[i].p=0;
		}
		for(j=i;j<i+nb;j++)
		{
			cin>>x>>y;
			t[j].s=ch(x);t[j].e=ch(y);
			t[j].p=1;
		}
        sort(t,t+na+nb);
		for(i=0;i<na+nb;i++)
		{
			if(!flag[i])
			{
				ans[t[i].p]++;
				t_s=t[i].p;
				tt=t[i].e;
				j=i;
				flag[i]=1;
				while(j<na+nb)
				{
					if(flag[j]==0&&t[j].p!=t_s&&cmp(t[j].s,tt))
					{
					    	flag[j]=1;
							tt=t[j].e;
						    t_s=t[j].p;
							j=i;
							continue;
					}
					j++;
				}
			}
		}
		cout<<"Case #"<<die<<":"<<" "<<ans[0]<<" "<<ans[1]<<endl;
	}
	return 0;
}

		
		
