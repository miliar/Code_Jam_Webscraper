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
	FILE* fin=fopen("in.txt","r");
	FILE* fout=fopen("out.txt","w");
	int n=0;
	fscanf(fin,"%d",&n);
	for (int j=0;j<n;++j)
	{
		int t=0;
		string s;
		fscanf(fin,"%s",s.data());
		for(int i=0;i<s.size();++i) 
			t=t*10+s[i]-'0';
		
		int t1=t;
		string s1(s.data());
		do
		{
			t1=0;
			if(!next_permutation(s1.begin(),s1.end())) s1.insert(0,"0");
			else 
				for(int i=0;i<s1.size();++i) t1=t1*10+s1[i]-'0';
		}while (s1[0]=='0' || t1<=t);
		fprintf(fout, "Case #%d: %d\n", j+1, t1);
		printf("Case #%d: %d\n", j+1, t1);
	}
	fclose(fin);fclose(fout);
	return 0;
}