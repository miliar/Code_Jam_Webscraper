#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin("A-large.in");
	ofstream fout("A.out");
	int L;
	int D;
	int N;
	int i,j,k;
	char c;
	int tmp;
	fin>>L>>D>>N;
	//cout<<L<<" "<<D<<" "<<N<<endl;
	int dict[5000][15];
	int pattern[15];
	for(i=0;i<D;++i)
	{
		for(j=0;j<L;++j)
		{
			fin>>c;
			tmp=(c-'a');
			dict[i][j]=(1<<tmp);
		}
	}
	
	bool flag=false;
	string s;
	int len;
	int pos;
	for(i=0;i<N;++i)
	{
		fin>>s;
		len=s.length();
		pos=0;
		for(j=0;j<15;++j)
			pattern[j]=0;
		for(j=0;j<len;++j)
		{
			if(s[j]=='(')
			{
				flag=true;
				continue;
			}
			if(s[j]==')')
			{
				++pos;
				flag=false;
				continue;
			}
			//s[i] is a char.
			tmp=s[j]-'a';
			pattern[pos]|=(1<<tmp);
			if(!flag)
				++pos;
		}
		//cout<<pos<<endl;
		int count;
		bool match;
		count=0;
		for(j=0;j<D;++j)
		{
			match=true;
			for(k=0;k<L;++k)
			{
				//cout<<i<<" "<<j<<" "<<k<<" "<<pattern[k]<<" "<<dict[j][k]<<endl;
				if((pattern[k]&dict[j][k])==0)
				{
					match=false;
					break;
				}
			}
			if(match)
			{
				++count;
			}
		}
		fout<<"Case #"<<(i+1)<<": "<<count<<endl;
	}
	return 0;
}
			
			
			
	
	
