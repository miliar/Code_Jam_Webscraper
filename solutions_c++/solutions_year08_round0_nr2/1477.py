#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <valarray>
#include <bitset>
#include <iostream>
#include <cctype>

using namespace std;

#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()

void suma_hora(string &tiempo, int min)
{
	int hora,minu;
	tiempo[2]=' ';
	stringstream is(tiempo);
	is >> hora >> minu;
	{
		minu+=min;
		hora+=(minu/60);
		minu%=60;
	
	}
	stringstream os;
	os<<hora<<":"<<minu;
	string cad=os.str();
	tiempo=cad;
	if(hora<10)
		tiempo="0"+tiempo;
	if(minu<10)
		tiempo.insert(3,"0");
}
string sacapar(string cad)
{
return cad.substr(0,5);	

}
string sacalle(string cad)
{

return cad.substr(6,5);
}

int main()
{

int n,T,aux=1;
	cin>>n;
	while(n)
	{int a,b;
	cin>>T>>a>>b;
	string cad;
	
	getline(cin,cad);
	vector <string> carrA,carrB,llegaA,llegaB,parA,parB;
	while(a)
	{
	getline(cin,cad);
	
	carrA.push_back(cad);
	a--;
	}

	while(b)
	{
	getline(cin,cad);

	carrB.push_back(cad);
	b--;
	}
	int conta=0,contb=0;
	for(int i=0;i<carrA.size();i++)
	{
		string cad2=sacapar(carrA[i]);
		string cad3=sacalle(carrA[i]);
		suma_hora(cad3,T);
		parA.push_back(cad2);
		llegaA.push_back(cad3);
	}
	for(int i=0;i<carrB.size();i++)
	{
		string cad2=sacapar(carrB[i]);
		string cad3=sacalle(carrB[i]);
		suma_hora(cad3,T);
		parB.push_back(cad2);
		llegaB.push_back(cad3);
	}
	sort(all(parA));
	sort(all(parB));
	sort(all(llegaA));
	sort(all(llegaB));
	vector <int> v1(llegaB.size(),0);
	vector <int> v2(llegaA.size(),0);
	for(int i=0;i<parA.size();i++)
	{
		for(int j=0;j<llegaB.size();j++)
		{
			if(parA[i]>=llegaB[j]&&v1[j]==0)
			{
			conta++;
			v1[j]++;
			break;
			}
		
		}
	
	}

	conta=parA.size()-conta;
	for(int i=0;i<parB.size();i++)
	{
		for(int j=0;j<llegaA.size();j++)
		{
			if(parB[i]>=llegaA[j]&&v2[j]==0)
			{
			contb++;
			v2[j]++;
			break;
			}
		
		}
	
	}
	contb=parB.size()-contb;

	cout<<"Case #"<<aux<<": "<<conta<<" "<<contb<<endl;
	aux++;
	n--;
	}





return 0;
}
