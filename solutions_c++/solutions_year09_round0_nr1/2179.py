#include<iostream>
#include<string>
#include<vector>
using namespace std;
int A[100][1000];
int main()
{
	vector<string> T;
	int L,D,N;
	cin>>L>>D>>N;
	string s;
	for(int i=0;i<D;++i)
	{
		cin>>s;
		T.push_back(s);
	}
	int P=0,Z=0;
	while(Z<N)
	{
	    P=0;
		memset(A,-1,sizeof(A));
		cin>>s;
		Z++;
		printf("Case #%i: ",Z);
		for(int i=0;i<s.size();++i)
		{
			if(s[i]=='(')
			{
				while(s[i]!=')')
				{
					i++;
					if(s[i]!=')');
						A[P][s[i]]=1;
				}
				P++;
			}
			else if(s[i]!=')')
			{
				A[P][s[i]]=1;
				P++;
			}
			
		}
		int count=0,b=1;
		for(int i=0;i<T.size();++i)
		{
			b=1;
			for(int k=0;k<T[i].size();++k)
				if(A[k][T[i][k]]!=1)
					b=0;
			if(b==1)	
				count++;
		}
		cout<<count<<"\n";
	}
}