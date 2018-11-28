#include <iostream>
#include <string>
#include <set>
using namespace std;
char lt[20][30];
int lc[20];
int stoc(string s)
{
	bool pa;
	int i,j;
	for (i=0;i<20;i++) lc[i]=0;
	pa=false; j=0;
	for (i=0;i<s.length();i++)
	{
		if (s[i]=='(') pa=true;
		if (s[i]==')') pa=false;
		if (s[i]>='a' && s[i]<='z') lt[j][lc[j]++]=s[i];
		if (!pa) j++;
	}
	return 0;
}
int main()
{
	set <int> st,nt;
	set <int>::iterator si;
	int l,n,d,i,ri,j;
	string wd[5000],t;
	cin>>l>>d>>n;
	for (i=0;i<d;i++) 
	{
		cin>>wd[i];
		nt.insert(i);
	}
	for (ri=0;ri<n;ri++)
	{
		st=nt;
		//cout<<st.size()<<endl;
		cin>>t;
		stoc(t);
		/*for (i=0;i<l;i++)
		{
			for (j=0;j<lc[i];j++)
				cout<<lt[i][j];
			cout<<endl;
		}*/
		for (i=0;i<l;i++)
		{
			int er[5000],ec=0;
			for (si=st.begin();si!=st.end();++si)
			{
				for (j=0;j<lc[i];j++)
				{
					if (wd[*si][i]==lt[i][j]) break;
				}
				if (j==lc[i]) 
				{
				//	cout<<"i="<<i<<"  "<<wd[*si]<<endl;
					er[ec++]=*si;
				}
			}
			for (j=0;j<ec;j++)
			{
				st.erase(st.find(er[j]));
			}
		}
		cout<<"Case #"<<ri+1<<": "<<st.size()<<endl;
	}
	//cout<<"OK"<<endl;
	return 0;
}

