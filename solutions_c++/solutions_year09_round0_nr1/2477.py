#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <queue>
#include <vector>

using namespace std;

int L, D, N;
struct words
{
	words** letters;
} *pwords;

string *cases;

void read()
{
	ifstream o("A-small-attempt3.in");
	o>>L>>D>>N;
	cout<<L<<endl<<D<<endl<<N<<endl;
	int i, j;
	string temp;
	pwords = new words;
	pwords->letters = new words*[26];
	for(i=0; i<26; i++)
		pwords->letters[i] = NULL;
	for(i=0; i<D; i++)
	{
		o>>temp;
		cout<<temp<<endl;
		words* ptemp = pwords;
		words* ptemp2;
		for(j=0; j<L; j++)
		{
			if(ptemp->letters[temp.at(j)-'a'] == NULL)
			{
				ptemp2 = new words;
				ptemp2->letters = new words*[26];
				for(int k=0; k<26; k++)
					ptemp2->letters[k] = NULL;
				ptemp->letters[temp.at(j)-'a'] = ptemp2;
				ptemp = ptemp2;
			}
			else
				ptemp = ptemp->letters[temp.at(j)-'a'];
		}
	}
	cases = new string[N];
	for(i=0; i<N; i++)
	{
		o>>cases[i];
		cout<<cases[i]<<endl;
	}
}

int onecase(int n)
{
	int i, j;
	words* ptemp = pwords->letters['f'-'a'];
	
	ptemp = pwords;
	queue<words*> q;
	q.push(ptemp);
	i=0;
	vector<char> v;
	while(i<cases[n].length())
	{
		cout<<"start size:"<<q.size()<<" ";
		v.clear();
		if(cases[n].at(i) =='(')
		{
			i++;
			while(cases[n].at(i) != ')')
			{
				v.push_back(cases[n].at(i));
				i++;
			}
		}
		else 
		{
			v.push_back(cases[n].at(i));
			cout<<" /"<<cases[n].at(i)<<"/ ";
		}
		i++;
		int ll=q.size();
		for(j=0; j<ll; j++)
		{
			words* temp = q.front();
			q.pop();
			if(temp == NULL)
				continue;
			for(int k=0; k<v.size(); k++)
			{
				if(temp->letters[v[k]-'a'] != NULL)
				{
					cout<<"push "<<v[k]<<";";
					q.push(temp->letters[v[k]-'a']);
				}
			}
		}
		cout<<q.size()<<endl;
	}
	
	return q.size();
}

int main()
{
	ofstream oo("b.out");
	int result;
	read();
	cout<<"HALF!"<<endl;
	for(int i=0; i<N; i++)
	{
		cout<<"case "<<i+1<<": "<<cases[i]<<"......"<<endl;
		result = onecase(i);
		oo<<"Case #"<<i+1<<": "<<result<<"\n";
		cout<<"Case #"<<i+1<<": "<<result<<"\n";
	}
	oo.close();
	return 0;
}
