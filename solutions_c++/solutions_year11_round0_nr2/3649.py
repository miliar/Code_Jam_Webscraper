#include<iostream>
#include<map>
#include<list>
#include<algorithm>

using namespace std;
map <string,char> tlum;
map <char,list<char> > usun;
string out;
void test(char tmp)
{
	int i=0;
	for(list<char>::iterator it = usun[tmp].begin();it!=usun[tmp].end();it++)
	{
		for(int j=0;j<out.size()-1;j++)
		{
			if(out[j]==*it)
			{
				out="";
				return ;
			}
		}
	}
}
int main()
{
	int c;
	cin >> c;
	for(int x=1;x<=c;x++)
	{
		tlum.clear();
		usun.clear();
		int d;
		cin >> d;
		string tmp,temp;
		for(int i=0;i<d;i++)
		{
			cin >> tmp;
			tlum[tmp.substr(0,2)]=tmp[2];
			temp=tmp.substr(1,1)+tmp.substr(0,1);
			tlum[temp]=tmp[2];
		}
		int n;
		cin >> n;
		for(int i=0;i<n;i++)
		{
			cin >> tmp;
			usun[tmp[0]].push_back(tmp[1]);
			usun[tmp[1]].push_back(tmp[0]);
		}
		cin >> n;
		cin >> tmp;
		out="";
		for(int i=0;i<tmp.size();i++)
		{
			if(out=="")
				out = tmp[i];
			else
			{
				//tlum
				string tmp2=out.substr(out.size()-1,1)+tmp[i];
				if(tlum[tmp2])
				{
					out = out.substr(0,out.size()-1)+tlum[tmp2];
				}
				else
				{
					out = out + tmp[i];	
					if(usun.find(tmp[i])!=usun.end())
						test(tmp[i]);
				}
			}


		}
		tmp="";
		for(int i=0;i<out.size();i++)
			tmp = tmp +out[i]+ ", ";
		cout << "Case #" << x<< ": [" << tmp.substr(0,tmp.size()-2) <<"]"<< endl;
	}
}
