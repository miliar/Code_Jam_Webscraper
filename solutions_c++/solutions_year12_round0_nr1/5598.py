#include<iostream>
#include<cstring>
#include<string>
using namespace std;

int main()
{
	freopen("c:\\2.in","r",stdin);
	freopen("c:\\out2.txt","w",stdout);
	
	int T;string s;
	cin>>T;getline(cin,s);
	int i;
	for(i=1;i<=T;i++)
	{
			string str;
			getline(cin,str);

			cout<<"Case #"<<i<<": ";
			int j;
			for(j=0;j<str.length();j++)
			{
				if(str[j]=='a') cout<<"y";
				if(str[j]=='b') cout<<"h";
				if(str[j]=='c') cout<<"e";
				if(str[j]=='d') cout<<"s";
				if(str[j]=='e') cout<<"o";
				if(str[j]=='f') cout<<"c";
				if(str[j]=='g') cout<<"v";
				if(str[j]=='h') cout<<"x";
				if(str[j]=='i') cout<<"d";
				if(str[j]=='j') cout<<"u";
				if(str[j]=='k') cout<<"i";
				if(str[j]=='l') cout<<"g";
				if(str[j]=='m') cout<<"l";
				if(str[j]=='n') cout<<"b";
				if(str[j]=='o') cout<<"k";
				if(str[j]=='p') cout<<"r";
				if(str[j]=='q') cout<<"z";//?
				if(str[j]=='r') cout<<"t";
				if(str[j]=='s') cout<<"n";
				if(str[j]=='t') cout<<"w";
				if(str[j]=='u') cout<<"j";
				if(str[j]=='v') cout<<"p";
				if(str[j]=='w') cout<<"f";
				if(str[j]=='x') cout<<"m";
				if(str[j]=='y') cout<<"a";
				if(str[j]=='z') cout<<"q";//?
				if(str[j]==' ') cout<<" ";



			}
			cout<<endl;

	}

		
	
return 0;
}