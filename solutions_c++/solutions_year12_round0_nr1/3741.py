#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a[27];
char w[101];
int i,t,j,c;
void initialize()
{
	a[6]=3;
	a[7]=22;
	a[8]=24;
	a[9]=4;
	a[10]=21;
	a[11]=9;
	a[12]=7;
	a[13]=12;
	a[14]=2;
	a[15]=11;
	a[16]=18;
	a[17]=26;
	a[18]=20;
	a[19]=14;
	a[20]=23;
	a[21]=10;
	a[22]=16;
	a[23]=6;
	a[24]=13;
	a[25]=1;
	a[26]=17;
	a[1]=25;
	a[2]=8;
	a[3]=5;
	a[4]=19;
	a[5]=15;
}
void f()
{
	if(w[i]<123 && w[i]>96)
			{
				printf("%c",a[w[i]-96]+96);
			}
			else
				cout<<w[i];
}

int main()
{
	
	initialize();
	cin>>t;
	j=1;
	for(i=0;i<1000;i++)
		;
	while(j<=t)
	{
		cout<<"Case #"<<j<<": ";
		scanf(" %[^\n]",w);
		i=0;
		for(;i<strlen(w);)
		{
			f();
			i++;
		}
		cout<<endl;
		j++;
	}
	return 0;
}
