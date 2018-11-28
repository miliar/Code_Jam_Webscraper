#include<iostream>
#include<string>
#include<fstream>
using namespace std;
string Dict[6000];
bool Valid[6000];
int main()
{
	ifstream cin("d:\\CodeJam.in");
	ofstream cout("d:\\CodeJam.out");
	int N,D,L;
	cin>>L>>D>>N;
	for(int i=0;i<D;i++)
		cin>>Dict[i];
	for(int k=0;k<N;k++)
	{
		memset(Valid,-1,sizeof(Valid));
		string Line;
		cin>>Line;
		bool InBrack = 0;
		int Pos = 0;
		int Sol = D;
		for(int i=0;i<Line.length();i++)
		{
			string S = "";
			if(Line[i]=='(')
			{
				while(Line[i]!=')')
				{
					S+=Line[i];
					i++;
				}
			}
			else
				S += Line[i];
			for(int j=0;j<D;j++)
			{
				int T = S.find(Dict[j][Pos]);
				if(T<0 && T>=S.length() && Valid[j])
				{
					Sol--;
					Valid[j]=false;
				}
			}
			Pos++;
		}
		cout<<"Case #"<<k+1<<": "<<Sol<<endl;
	}
}