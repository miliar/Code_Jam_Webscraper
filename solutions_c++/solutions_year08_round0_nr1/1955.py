#include <iostream>
#include <map>
using namespace std;
int main()
{
	int n,s,q;
	string str[1001],t;
	map<string,int>m,mt;
	scanf("%d\n",&n);
	for(int i=0;i<n;i++)
	{
		m.clear();
		int sw=0,nr,r;
		bool found=false;
		scanf("%d\n",&s);
		for(int j=0;j<s;j++)
		{
			getline(cin,t);
			m.insert(pair<string,int>(t,0));
		}
		scanf("%d\n",&q);
		for(int j=0;j<q;j++)
		{
			getline(cin,str[j]);
			m[str[j]]++;
		}
		mt=m;
		for(nr=q-1,r=-1;nr!=r && !found;nr--)
		{
			for(map<string,int>::iterator it=m.begin();it!=m.end() && !found;it++)
				if(it->second==0)
				{
					sw++;
					found=true;
//					cout<<it->first;
					break;
				}
			if(!found && mt[str[nr]]==1)
			{
//				cout<<str[nr]<<" "<<1<<" "<<r<<endl;
				for(r++;r<nr;r++)
					m[str[r]]--;
				r=nr-1;
				sw++;
				nr=q;
				mt=m;
			}
			else
			{
//				cout<<str[nr]<<" "<<mt[str[nr]]<<endl;
				mt[str[nr]]--;
			}
		}
//		cout<<nr;
		sw--;
		if(sw==-1)
			sw=0;
		cout<<"Case #"<<i+1<<": "<<sw<<endl;
	}
	return 0;
}
