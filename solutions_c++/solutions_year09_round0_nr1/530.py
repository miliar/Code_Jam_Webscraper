#include<iostream>
#include<string>
#include<vector>

using namespace std;

const int ILOSCLITER=30;
const int BRAK=-1;

struct node
{
	int znak;
	int syn[ILOSCLITER];
};

int root=0;
vector<node> T(1);

void dodajDoSlownika(string& wyraz,int L)
{
	int obecny=root;
	for(int i=0;i<L;i++)
	{
		int tmp=T[obecny].syn[wyraz[i]-'a'];
		if(tmp==BRAK)
		{
			tmp=T.size();
			T.resize(tmp+1);
			T[obecny].syn[wyraz[i]-'a']=tmp;
			obecny=tmp;
			
			for(int j=0;j<ILOSCLITER;j++)
				T[obecny].syn[j]=BRAK;
		}
		else
			obecny=tmp;
	}
	
}

int policzMozliwosci(int wsk,string wyraz,int L)
{
	if(L==1)
	{
		if(wyraz[0]=='(')
		{
			int wynik=0;
			for(int j=1;wyraz[j]!=')';j++)
				if(T[wsk].syn[wyraz[j]-'a']!=BRAK)
					wynik++;
			return wynik;
		}
		else
			return T[wsk].syn[wyraz[0]-'a']==BRAK ? 0 : 1;
	}
	
	if(wyraz[0]=='(')
	{
		int wynik=0;
		
		int j=0;
		while(wyraz[++j]!=')');
		
		for(int i=1;wyraz[i]!=')';i++)
		{
			if(T[wsk].syn[wyraz[i]-'a']!=BRAK)
				wynik+=policzMozliwosci(T[wsk].syn[wyraz[i]-'a'],wyraz.substr(j+1,wyraz.size()-j),L-1);
		}
		return wynik;
	}
	else
	{
		if(T[wsk].syn[wyraz[0]-'a']==BRAK)
			return 0;
		
		return policzMozliwosci(T[wsk].syn[wyraz[0]-'a'],wyraz.substr(1,wyraz.size()-1),L-1);
	}
}

int main ()
{
	ios_base::sync_with_stdio(false);
	T[root].znak=BRAK;
	for(int i=0;i<ILOSCLITER;i++)
		T[root].syn[i]=BRAK;
	
	int L,D,N;
	
	cin>>L>>D>>N;
	
	//BUDOWA SLOWNIKA
	
	for(int i=0;i<D;i++)
	{
		string tmp;
		cin>>tmp;
		dodajDoSlownika(tmp,L);
	}
	
	
	//OBLICZANIE MOZLIWOSCI
	for(int i=0;i<N;i++)
	{
		string tmp;
		cin>>tmp;
		
		cout<<"Case #"<<i+1<<": "<<policzMozliwosci(root,tmp,L)<<endl;
	}
	
	
	return 0;
}
