#include <cstdio>
#include <map>
#include <iostream>
using namespace std;

void CheckTest(int);
int main()
{
	int p;
	cin>>p;
	for(int i=0;i<p;i++) CheckTest(i+1);
	return 0;
}
void CheckTest(int z)
{
	map <string,int> Bufor;
	int s,q;
	scanf("%d\n",&s);
	for(int i=0;i<s;i++)
	{
		string we;
		getline(cin,we);
		Bufor[we]=-1;
	}
	scanf("%d\n",&q);
	if(q==0)
	{
		printf("Case #%d: %d\n",z,0);
		return;
	}
//	cout<<q<<endl;
	string Zapytania[q];
	int TablicaSkokow[q];
	for(int i=0;i<q;i++)
	{
		getline(cin,Zapytania[i]);
//		cout<<Zapytania[i]<<endl;
	}
	for(int i=q-1;i>=0;i--)
	{
		int max=-1;
		Bufor[Zapytania[i]]=i;
		for(map<string,int>::iterator j=Bufor.begin();j!=Bufor.end();j++)
			if(j->second==-1) 
			{
				max=-1;
				break;
			}
			else if(j->second>max) max=j->second;
		TablicaSkokow[i]=max;
	}
	int k=0;
	for(int i=0;TablicaSkokow[i]!=-1;i=TablicaSkokow[i],k++);
	printf("Case #%d: %d\n",z,k);
}
