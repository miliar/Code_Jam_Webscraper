
#include <iostream>
#include <string>
using namespace std;

bool isopp[200][200];
char iscom[200][200];
int main()
{
	int t,c,d,n;
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>t;
	int cnt=0;
	while(t--)
	{
		memset(isopp,0,sizeof(isopp));
		memset(iscom,0,sizeof(iscom));
		cin>>c;
		string com;
		for(int i=0;i<c;i++)
		{
			cin>>com;
			iscom[com[0]-'A'][com[1]-'A']=com[2];
			iscom[com[1]-'A'][com[0]-'A']=com[2];
		}
		cin>>d;
		for(int i=0;i<d;i++)
		{
			cin>>com;
			isopp[com[0]-'A'][com[1]-'A']=1;
			isopp[com[1]-'A'][com[0]-'A']=1;
		}
		cin>>n;
		string str;
		cin>>str;
		for(int i=1;i<str.length();i++)
			if((int)iscom[str[i-1]-'A'][str[i]-'A']!=0)
			{
				str[i-1]=(char)iscom[str[i-1]-'A'][str[i]-'A'];
				str.erase(str.begin()+i);
				i--;
			}
			else
			{
				for(int j=0;j<i;j++)
					if(isopp[str[i]-'A'][str[j]-'A']!=0)
					{
						str.erase(str.begin(),str.begin()+i+1);
						i=-1;
						break;	
					}
			}					
		cnt++;
		cout<<"Case #"<<cnt<<": "<<"[";
		if(str.length()!=0)
		{
			cout<<str[0];
			for(int i=1;i<str.length();i++)
				cout<<", "<<str[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

/*
Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
*/
