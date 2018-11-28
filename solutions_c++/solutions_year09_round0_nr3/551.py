#include<vector>
#include<iostream>
#include<string>

using namespace std;

const int BUFOR=600;
const int MOD=10000;

const string wzor="welcome to code jam";

int policz(string P,string T)
{
	vector<vector<int> > A(P.size()+1,vector<int>(T.size()+1,0));
	
	for(int i=0;i<T.size()+1;i++)
		A[0][i]=1;
	for(int i=1;i<P.size()+1;i++)
		A[i][0]=0;
	
	for(int i=0;i<P.size();i++)
		for(int j=0;j<T.size();j++)
			if(P[i]==T[j])
				A[i+1][j+1]=(A[i][j]+A[i+1][j])%MOD;
			else
				A[i+1][j+1]=A[i+1][j];
	return A[P.size()][T.size()];
}

int main ()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		if(i==0)
			cin.get();
		char tmp[BUFOR];
		
		cin.getline(tmp,BUFOR);
		
		string napis(tmp);
		
		int wynik=policz(wzor,napis);
		
		cout<<"Case #"<<i+1<<": ";
		if(wynik<1000)
			cout<<0;
		if(wynik<100)
			cout<<0;
		if(wynik<10)
			cout<<0;
		cout<<wynik<<endl;
	}
}
