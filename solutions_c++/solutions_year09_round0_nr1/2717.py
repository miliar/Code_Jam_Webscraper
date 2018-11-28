#include<iostream>
#include<fstream>
using namespace std;
int main(void)
{
	string s;
	int l,d,n,w1,loc,cntr;
	int i1,i2,j1,j2,j3,k1;
	ifstream in;
	in.open("A-large.in",ios::in);
	ofstream out;
	out.open("A.out",ios::out);
	in>>l>>d>>n;
	char lang[d][l];
	for(i1=0;i1<d;i1++)
		in>>lang[i1];
	int pattern[d];
	for(i2=0;i2<n;i2++)
	{
		for(j2=0;j2<d;j2++)
			pattern[j2]=0;
		in>>s;
		w1=0;
		loc=0;
		while(s[w1]!='\0')
		{
			if(s[w1]=='(')
			{
				w1++;
				while(s[w1]!=')')
				{
			        	for(k1=0;k1<d;k1++)
					{
						if(lang[k1][loc]==s[w1])
							pattern[k1]++;
					}
					w1++;	
				}
				loc++;
				w1++;
			}
			else
			{
				for(k1=0;k1<d;k1++)
				{
					if(lang[k1][loc]==s[w1])
					{
						pattern[k1]++;
					}
				}
				loc++;
				w1++;
			}
		}
		cntr=0;
		for(j3=0;j3<d;j3++)
			if(pattern[j3]==l)
			{
				cntr=cntr+1;
			}
		out<<"Case #"<<i2+1<<": "<<cntr<<'\n';
	}
	return 1;
}
