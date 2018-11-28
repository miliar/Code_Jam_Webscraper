#include<fstream>
//#include<cmath>
#include<cstring>
#include<iostream>
using namespace std;
ifstream fin("in.txt",ios_base::in);
ofstream fout("out.txt",ios_base::out|ios_base::app);
int save();
int main()
{
	int no_case;
	fin>>no_case;cout<<no_case<<endl;
	fin.ignore(1,'\n');
	while(no_case--)
	{
		save();
		
		//cout<<"hi";
				

	}

	return 0;
}
save()
{
	int no_switch=1;
	static int n=1;
	int no_eng,no_query;
	fin>>no_eng;
	cout<<no_eng<<endl;
	//cout<<no_eng;
	fin.ignore(1,'\n');
	//char **s=new char*[no_eng];
	int *a=new int[no_eng];
	for(int k=0;k<no_eng;k++)
		a[k]=-1;
	char s[101][110],q[1001][110];
	for(int i=0;i<no_eng;i++)
		{	
			fin.get(s[i],105);
			fin.ignore(1,'\n');
			cout<<s[i]<<endl;
		}
	fin>>no_query;
	cout<<no_query<<endl;
	fin.ignore(1,'\n');
	for(i=0;i<no_query;i++)
		{
			fin.get(q[i],105);
			fin.ignore(1,'\n');
			cout<<q[i]<<endl;
		}
	int big=0;
	while(1)
	{
		for(int j=0;j<no_eng;j++)
		for(i=big;i<no_query;i++)
			if(!strcmp(q[i],s[j]))
				{
					a[j]=i;break;
				}
		for(k=0;k<no_eng;k++)
			if(a[k]==-1)
			{fout<<"Case #"<<n<<": "<<no_switch-1<<endl;++n;return 0;}
		//big=a[0];
		for(k=0;k<no_eng;k++)
		if(a[k]>=big)
			big=a[k];
		for(k=0;k<no_eng;k++)
			if(a[k]<big)
				a[k]=-1;
		++no_switch;
				
	}
		
				
}