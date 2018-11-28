#include <iostream>
#include <string>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	FILE *ofp=fopen("A-small-attempt2.txt", "w");
	int a[26]={24,7,4,18,14,2,16,23,3,20,8,6,11,1,10,17,25,19,13,22,9,15,5,12,0,21};
	int T;
	cin>>T;
	fscanf(stdin,"\n");
	for(int i=1;i<=T;i++)
	{
		string s;
		getline(cin,s);
		
		for(int j=0;j<s.size();j++)
		{
			if(isspace(s[j]))continue;
			s[j]=a[s[j]-'a']+'a';
		}
		fprintf(ofp,"Case #%d: ",i);
		for(int j=0;j<s.size();j++)
			fprintf(ofp,"%c",s[j]);
		fprintf(ofp,"\n");

	}
}

