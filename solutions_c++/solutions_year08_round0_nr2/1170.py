#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>

using namespace std;

vector <int> depa;
vector <int> arra;
vector <int> depb;
vector <int> arrb;

ofstream fout("output.txt");

int curr[3600];

int main(void)
{
	int N,S,Q,i,j,k,T;
	char c;
	int x,y;
	cin >> N;
	string s;
	int ct=0;
	while(N>0)
	{
		ct++;
		N--;
		cin >> T;
		int mina,minb;
		mina = minb = 0;
		depa.resize(0);
		arra.resize(0);
		depb.resize(0);
		arrb.resize(0);
		int ka,kb;
		cin >> ka >> kb;
		for(i=0; i<ka; i++)
		{
			cin >> x >> c >> y;
			depa.push_back(60*x+y);
			cin >> x >> c >> y;
			arrb.push_back(60*x+y+T);
		}
		
		for(i=0; i<kb; i++)
		{
			cin >> x >> c >> y;
			depb.push_back(60*x+y);
			cin >> x >> c >> y;
			arra.push_back(60*x+y+T);
		}
		sort(arra.begin(),arra.end());
		sort(arrb.begin(),arrb.end());
		sort(depa.begin(),depa.end());
		sort(depb.begin(),depb.end());
		/*for(i=0; i<depa.size(); i++)
		{
			cout << depa[i] << endl;
		}
		cout << endl;
		for(i=0; i<depb.size(); i++)
		{
			cout << depb[i] << endl;
		}
		cout << endl;
		for(i=0; i<arra.size(); i++)
		{
			cout << arra[i] << endl;
		}
		cout << endl;
		for(i=0; i<arrb.size(); i++)
		{
			cout << arrb[i] << endl;
		}
		cout << endl;*/
		i=j=0;
		for(int z=0; z<24*60; z++)
		{
			while(i<depa.size() && depa[i]==z)
				i++;
			while(j<arra.size() && arra[j]==z)
				j++;
			if(i-j > mina)
			{
				mina=i-j;
				//cout << mina << " " << i << " " << j << " " << z << endl;
			}
		}
		i=j=0;
		for(int z=0; z<24*60; z++)
		{
			while(i<depb.size() && depb[i]==z)
				i++;
			while(j<arrb.size() && arrb[j]==z)
				j++;
			if(i-j > minb)
				minb=i-j;
		}
		cout << "Case #" << ct << ": " << mina << " " << minb << endl;
fout << "Case #" << ct << ": " << mina << " " << minb << endl;
			
	}
	return 0;
}

		