#include<iostream>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
	long t,c,d,n,cnt_c=0,i,j,k;
	string s;
	vector<string> clist1,clist2,nlist;
	vector<char> dlist1,dlist2;
	cin>>t;
	while(t--)
	{
		clist1.clear();
		clist2.clear();
		dlist1.clear();
		dlist2.clear();
		nlist.clear();
		cnt_c++;
		cin>>c;
		while(c--)
		{
			cin>>s;
			clist1.push_back(s.substr(0,2));
			clist2.push_back(s.substr(2));
		}
		cin>>d;
		while(d--)
		{
			cin>>s;
			dlist1.push_back(s[0]);
			dlist2.push_back(s[1]);
		}
		cin>>n;
		cin>>s;
		nlist.push_back(s);
		for(i=1;i<s.size();i++)
		{
				string temp=s.substr(i-1,2);
				string temp2=temp;
				reverse(temp2.begin(),temp2.end());
				for(k=0;k<clist1.size();k++)
				{
//					cout<<temp<<" "<<temp2<<" "<<clist1[k]<<endl;
					if(clist1[k].compare(temp)==0 || clist1[k].compare(temp2)==0)
					{
					//	cout<<i<<" "<<temp<<endl;
						s.replace(i-1,2,clist2[k]);
						i--;
						break;
					}
					
				}
//				cout<<s<<endl;
			for(j=0;j<i;j++)
			{
				for(k=0;k<dlist1.size();k++)
				{
					if(s[i]==dlist1[k])
					{
						if(s[j]==dlist2[k])
						{
							s.replace(0,i+1,"");
							i=0;
						}
					}
					else if(s[i]==dlist2[k])
					{
						if(s[j]==dlist1[k])
						{
							s.replace(0,i+1,"");
							i=0;
						}
					}
				}
			}
		}
		//print values now
		cout<<"Case #"<<cnt_c<<": "<<"[";
		for(i=0;i<s.size();i++)
		{
			cout<<s[i];
			if(i!=s.size()-1)
				cout<<", ";
		}
		cout<<"]"<<endl;
	}
}
