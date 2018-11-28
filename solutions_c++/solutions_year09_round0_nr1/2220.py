#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#include<string.h>
using namespace std;

int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	char** words;
	words=(char**) malloc(d*sizeof(char*));
	for(int i=0;i<d;i++)
	{
		words[i]=(char*) malloc(l*sizeof(char*)+1);
		scanf("%s",words[i]);
	}
	int dfa[l][26];
	for(int j=0;j<n;j++)
	{
		int answer=0;
		string pattern;
		for(int i=0;i<l;i++)
		{
			memset(dfa[i],0,26*sizeof(int));
		}
		cin>>pattern;
		int itr=0;
		for(int i=0;i<l;i++)
		{
			if(pattern.at(itr)!='(')
			{
				dfa[i][pattern.at(itr)-(int)'a']=1;
				itr++;
			}
			else
			{
				itr++;
				while(pattern.at(itr)!=')')
				{
					dfa[i][pattern.at(itr)-(int)'a']=1;
					itr++;
				}
				itr++;
			}
		}
		for(int i=0;i<d;i++)
		{
			for(int k=0;k<l;k++)
			{
				if(dfa[k][words[i][k]-(int)'a']==0)
					break;
				if(k==l-1)
					answer++;
			}
		}
		cout<<"Case #"<<j+1<<": "<<answer<<"\n";
	}
}
