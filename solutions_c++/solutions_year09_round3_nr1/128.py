#include<iostream>
#include<string>
#include<map>
#include<fstream>
using namespace std;
int Solve(string &S)
{
	map<char,int> Dict;
	int Max = 3;
	Dict[S[0]]=2;
	bool doZero=true;
	for(int i=1;i<S.length();i++)
	{
		if(Dict[S[i]]==0)
		{
			if(doZero)
			{
				Dict[S[i]]=1;
				doZero = false;
			}
			else
			{
				Dict[S[i]]=Max;
				Max++;
			}
		}
	}
	int Base = Dict.size();
	if(Base == 1)
		Base++;
	int Num = 0;
	int P = 1;
	for(int i=S.length()-1;i>=0;i--)
	{
		Num += P*(Dict[S[i]]-1);
		P*=Base;
	}
	return Num;
}
int main()
{
	ifstream cin("d:\\codejam.in");
	ofstream cout("d:\\codejam.out");
	int T;
	cin>>T;
	for(int Case= 1;Case<=T;Case++)
	{
		string S;
		cin>>S;
		cout<<"Case #"<<Case<<": "<<Solve(S)<<endl;
	}
}