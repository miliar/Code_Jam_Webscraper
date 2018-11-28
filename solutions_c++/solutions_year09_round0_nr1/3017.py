# include <iostream>
# include <vector>
# include <string>
using namespace std;
int main()
{
	int l,d,n,k,j,cnt,m,i,done,result;
	vector<string> v;
	string inp,str;
	cin>>l>>d>>n;
	for(i=0;i<d;i++)
	{
		cin>>str;
		v.push_back(str);
	}
	for(i=0;i<n;i++)
	{
		cin>>inp;
		k=0;
		done=0;
		result=0;
		int present[26][16]={0};
		for(j=0;j<inp.size();j++)
		{
			if(inp[j]=='(')
				done=1;
			if(inp[j]==')')
				done=0;
			if(inp[j]!=')' && inp[j]!='(')
			{
				present[inp[j]-'a'][k]=1;
			}
			if(!done)
				k++;
		}

		for(k=0;k<v.size();k++)
		{
			cnt=0;
			for(m=0;m<v[k].size();m++)
			{
				if(present[v[k][m]-'a'][m])
					cnt++;
			}
			if(cnt==v[k].size())
				result++;	
		}
		cout<<"Case #"<<i+1<<": "<<result<<endl;
	}
	return 0;
}
