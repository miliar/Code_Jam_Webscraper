#include<iostream>
#include<set>
#include<string>
#include<vector>
#include<sstream>
using namespace std;

struct node
{
	string nazwa;
	double wart;
	int l,p;	
};

const int BRAK=-1;

double praw;

double dajDouble(string tmp)
{
	stringstream stm;
	stm<<tmp;
	double tmp2;
	stm>>tmp2;
	return tmp2;

}

void parsujDrzewo(vector<node>& T,int n)
{
	string tmp;
	cin>>tmp;
	if(tmp=="(")
	{
		string tmp2;
		cin>>tmp2;
		tmp+=tmp2;
	}
	if(tmp[tmp.size()-1]!=')')
	{
		char c;
		cin>>c;
		if(c==')')
			tmp+=c;
		else
			cin.putback(c);
	}
	if(tmp[tmp.size()-1]==')')
	{
		
		T[n].wart=dajDouble(tmp.substr(1,tmp.size()-2));
		T[n].l=BRAK;
		T[n].p=BRAK;
	}
	else
	{
		T[n].wart=dajDouble(tmp.substr(1,tmp.size()-1));
		cin>>T[n].nazwa;
		
		T.resize(T.size()+2);
		T[n].l=T.size()-2;
		T[n].p=T.size()-1;
		parsujDrzewo(T,T[n].l);
		parsujDrzewo(T,T[n].p);
		char c;
		cin>>c;
	}
	
}

void wypisz(vector<node>& T,int n)
{
	cout<<T[n].wart<<" "<<T[n].nazwa<<endl;
	if(T[n].l!=BRAK)
	{
		wypisz(T,T[n].l);
		wypisz(T,T[n].p);
	}
}

void policz(vector<node>& T,set<string>& S,int n)
{
	praw*=T[n].wart;
	if(T[n].l==BRAK)
		return;
	
	if(S.count(T[n].nazwa)>0)
	{
		policz(T,S,T[n].l);
	}
	else
	{
		policz(T,S,T[n].p);
	}
}

int main ()
{
	ios_base::sync_with_stdio(false);
	
	int t;
	cin>>t;
	for(int d=0;d<t;d++)
	{
		int L;
		cin>>L;
		
		praw=1;
		cout<<"Case #"<<d+1<<":"<<endl;
		
		vector<node> T(1);
		
		parsujDrzewo(T,0);
	
		
		int il;
		cin>>il;
		while(il--)
		{
			praw=1;
			string naz;
			cin>>naz;
			int ilC;
			cin>>ilC;
			set<string> S;
			for(int l=0;l<ilC;l++)
			{
				string tmp3;
				cin>>tmp3;
				S.insert(tmp3);
			}
			policz(T,S,0);
			cout.precision(7);
			cout<<fixed<<praw<<endl;
			
		}
	}
	
	return 0;
}
