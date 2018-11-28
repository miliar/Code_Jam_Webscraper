#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

double pi=2*acos(0.0);

int main()
{
	FILE* fin=freopen ("in.txt","r",stdin);
	FILE* fout=freopen("out.txt","w",stdout);

	int n=0;
	cin >> n;
	for (int j=0;j<n;++j)
	{
		char s1[80];
		cin >> s1;
		string s(s1);
		int c=0;
		int num[100];
//	cout << s.size() << "\n";

		for(int q=0;q<s.size();++q)
			if(s[q]!=' ')
			{
				num[q]=c;
				for(int k=q+1;k<s.size();++k)
				{
					char c1=s[k],c2=s[q];
					if(c1==c2)
					{
						num[k]=num[q];
						s[k]=' ';
					}
				}
				s[q]=' ';
				++c;
			}

		for(int i=0;i<s.size();++i)
		{
			if(num[i]==0) num[i]=1;
			else {if(num[i]==1) num[i]=0;}
		}

		long long m=0;
		if(c==1)c=2;
		for(int i=0;i<s.size();++i)m=m*c+num[i];
		cout << "Case #" << j+1 << ": ";
		cout << m <<"\n";
	}
	fclose(fin);fclose(fout);
	return 0;
}