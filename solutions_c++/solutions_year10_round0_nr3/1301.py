#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;

int main()
{
	int ie2;
	cin>>ie2;
	for(int ie=1;ie<=ie2;ie++)
	{
		int r,k,n;
		cin>>r>>k>>n;
		string str="";
		while(n--)
		{
			int in;
			cin>>in;
			str.push_back(in);
		}
		map<string,int> dic;
		int gain[2000];
		gain[0]=0;
		int loop=-1;
		int tot=1;
		dic.insert(pair<string,int>(str,0));
		for(int i=1;;i++)
		{
			int pos=0;
			int cnt=0;
			for(;pos<str.length();pos++)
			{
				if(cnt+str[pos]>k)
				{
					pos--;
					break;
				}
				cnt+=str[pos];
			}
			if(pos!=str.length())
				str=str.substr(pos+1,str.length()-pos-1)+str.substr(0,pos+1);
			map<string,int>::iterator it=dic.find(str);
			gain[tot]=gain[tot-1]+cnt;
			tot++;
			if(it!=dic.end())
			{
				loop=it->second;
				break;
			}
			else
			{
				dic.insert(pair<string,int>(str,i));
			}
		}
		cout<<"Case #"<<ie<<": ";
		//r--;
		if(r<tot)
			cout<<gain[r]<<endl;
		else
		{
			int body=r-tot+1;
			int mul=gain[tot-1]-gain[loop];
			int l=tot-loop-1;
			int base=0;
			if(loop>0)
				base=gain[loop];
			int cost=(body/l)*mul+gain[tot-1];
			if(body%l!=0)
				cost+=gain[loop+body%l]-base;
			cout<<cost<<endl;
				

		}
	}
	return 0;
}