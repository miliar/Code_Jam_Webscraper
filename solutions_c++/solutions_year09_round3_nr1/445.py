#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<string>
using namespace std;
int m;
struct Vect
{
	int a,b;
};
vector<Vect> Mass;
vector<Vect> X;
vector<Vect> Y;
char read[100];
bool Read()
{
	
	fgets(read,99,stdin);
	if(read[0]=='\n') 
		fgets(read,99,stdin);
	if(read[strlen(read)-1]=='\n') read[strlen(read)-1]='\0';
	return true;
}

void Work()
{
	vector<char> dif;
	int i,j;
	for(i=0;read[i]!='\0';++i)
	{
		bool have = false;
		for(j=0;j<dif.size();++j)
			if( dif[j]==read[i] ) have = true;
		if( !have )
			dif.push_back(read[i]);
	}
	int k = dif.size();
	char out[10000];
	out[0] = '1';
	//strcpy(out,read);
	out[0] = 1;
	for(i=1;read[i]!='\0';++i)
	{
		if( read[i]==dif[0] )
		{
			out[i] = 1;
			continue;
		}
		if( read[i]==dif[1] )
		{
			out[i] = 0;
			continue;
		}
		for(j=2;j<dif.size();++j)
			if( read[i]==dif[j] )
				out[i] = j;
	}
	if(k==1)
	{
		k=2;
	}
	long long A = 0;
	long long sys = k;
	int S = strlen(read)-1;
	A = out[S];
	for(--S;S>=0;--S)
	{
		long long tmp = sys;
		tmp*=out[S];
		A+=tmp;
		sys*=k;
	}
	printf("%I64d\n",A);
}

void Write()
{
}

int main()
{
	int i=1,n;
scanf("%d",&n);
for(i=0;i<n;++i)
{
	Read();
	printf("Case #%d: ",i+1);
	Work();
	Write();
}
return 0;
}

