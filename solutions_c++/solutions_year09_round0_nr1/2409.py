#include <vector>
#include <string>
#include <iostream>
#include <list>
using namespace std;
list <int> K;
vector <string> W;
vector<vector<vector<int > > > T;
vector<int> R;
int L,D,N;

void Check(string);
void MakeTable();
int main()
{
	cin>>L>>D>>N;
	W.resize(D);
	R.resize(D,0);
	for(int i=0;i<D;i++)	cin>>W[i];
	MakeTable();
	for(int i=0;i<D;i++) Check(W[i]);
	for(int i=0;i<N;i++)
		cout<<"Case #"<<i+1<<": "<<R[i]<<endl;
	return 0;
}
void MakeTable()
{
	T.resize(N);
	for(int i=0;i<N;i++)
	{
		string in;
		int wsk=0;
		T[i].resize(L);
		for(int j=0;j<L;j++) 
				T[i][j].resize(26,0);
		cin>>in;
		for(int j=0;j<L;j++)
		{
			if(in[wsk]!='(')
				T[i][j][in[wsk]-'a']=1;
			else
			for(wsk++;in[wsk]!=')';wsk++)
				T[i][j][in[wsk]-'a']=1;
			wsk++;
		}
/*		for(int j=0;j<L;j++)
		{
			for(int k=0;k<26;k++) cout<<T[i][j][k]<<" ";
			cout<<endl;
		}
		cout<<endl;*/
	}
}
void Check(string s)
{
//	cout<<s<<endl;
	for(int i=0;i<N;i++)
	{
		bool tmp=true;
		for(int j=0;j<L;j++)
			if(T[i][j][s[j]-'a']==0)
			{
				tmp=false;
				break;
			}	
		if(tmp) R[i]++;
	}

}

