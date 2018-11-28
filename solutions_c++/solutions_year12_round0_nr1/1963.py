#include <iostream>

using namespace std;

int main()
{
	char table[]={'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };
	freopen("A-small-attempt0.in","r",stdin);
	freopen("output.txt","w",stdout);
//	char table[27];
	char str[101],out[101];

	int tc;
	cin >>tc;cin.ignore();
	for (int i=0;i<tc;i++)
	{
		cin.getline(str,101);
		int k=strlen(str);
		int j;
		for (j=0;j<k;j++)
		{
			if (str[j]==' ') {out[j]=' ';}
			else out[j]=table[str[j]-'a'];
		};
		out[j]='\0';
		printf("Case #%d: %s\n",i+1,out);
	};

	return 0;
	//below is the code for finding out the translation table
	//char str1[3][101],str2[3][101];
	//int tc;
	//cin >> tc;cin.ignore();
	//for (int i=0;i<tc;i++)
	//	cin.getline(str1[i],101);
	//for (int i=0;i<tc;i++)
	//	cin.getline(str2[i],101);

	//for (int i=0;i<tc;i++)
	//{
	//	int len=strlen(str1[i]);
	//	for (int j=0;j<len;j++)
	//		if (str1[i][j]!=' ') table[str1[i][j]-'a']=str2[i][j];
	//};
	//table['q'-'a']='z';
	//table['z'-'a']='q';
	//cout<< '{';
	//for (int i=0;i<26;i++)
	//	cout <<'\'' <<table[i] <<"\', ";
	//cout<<'}';
	////cout<<str1[2];
	//return 0;
};