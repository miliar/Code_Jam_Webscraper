#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
#define sz size()

int main()
	{
	int T;
	cin>>T;
	for(int z=1;z<=T;z++)
		{
		string a;
		cin>>a;
		int f=0;
		while(next_permutation(a.begin(),a.end()))
			{
			cout<<"Case #"<<z<<": "<<a<<endl;

			f=1;
						break;
			}
		if(!f)
			{
			string temp=a;
			
			sort(a.begin(),a.end());
			reverse(temp.begin(),temp.end());
			string t;
			t = a[0];
			t = t + '0';
			for(int i=1;i<a.sz;i++)
				t = t+a[i];
			if(t[0] != '0')
				cout<<"Case #"<<z<<": "<<t<<endl;
			else
				{
				string zzz,zeros;
				sort(temp.begin(),temp.end());
				int y=0,indx;
				while(temp[y]=='0')
					{
					zeros+='0';
					y++;
					}
				zeros+='0';
				zzz = temp[y];
				zzz = zzz+zeros;
				for(int ss=y+1;ss<temp.sz;ss++) zzz = zzz+temp[ss];
				/*zzz = temp[0];
				zzz  = zzz+'0';
				for(int y=1;y<temp.sz;y++)
					zzz = zzz+temp[y];*/
				cout<<"Case #"<<z<<": "<<zzz<<endl;
				}
			}
		}	
	return 0;
	}
