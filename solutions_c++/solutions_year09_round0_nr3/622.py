#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
#define MOD 10000

int main()
{
string w="welcome to code jam";
int state[19];
int N;
string str;
cin>>N;
getline(cin,str);

for(int i=0;i<N;i++)
	{
	getline(cin,str);
	//cout<<str<<endl;
	int l=str.length();
	for(int i1=0;i1<19;i1++) state[i1]=0;
	
	for(int i1=0;i1<l;i1++)
		{
		state[0]%=MOD;
		if(str[i1]==w[0]) state[0]++;
		for(int j=1;j<19;j++)
			{
			if(str[i1]==w[j])  state[j]+=state[j-1];
			state[j]%=MOD;
			}		
		
		}
	printf("Case #%d: %.4d\n",i+1,state[18]);
	}

return 0;
}
