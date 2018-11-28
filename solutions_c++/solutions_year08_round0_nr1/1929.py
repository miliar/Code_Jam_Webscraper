#include <iostream>
#include <hash_map>
#include <vector>
#include <string>
using namespace std;
using namespace stdext;

const int S = 100;
const int N = 20;
const int Q = 1000;

hash_map<string, int> se_name; //search engine name
int si[S];  //search engine index flag
int count;

int query[Q]; 

int n; //test cases
int s;
int q;

int switch_count;

void switch_engine()
{
	switch_count ++;
	for(int i=0; i<s; i++)
	{
		si[i] = 1;
	}
	count = s;
}


int main()
{
	int i, k;
	string name;
	cin >> n;
	for(k=1; k<=n; k++)
	{		
		switch_count = 0;
		se_name.clear();
		cin >>s;
		getchar();
		for(i=0; i<s; i++)
		{
			getline(cin, name, '\n');
			se_name.insert(pair<string, int>(name, i));
			si[i] = 1;
		}
		count = s;
		cin >> q;
		getchar();
		for(i=0; i<q; i++)
		{
			getline(cin, name, '\n');			
			query[i] = se_name[name];			
		}
		for(i=0; i<q; i++)
		{			
			if(si[query[i]] == 1)
			{
				si[query[i]] = 0; //set as visit
				count -- ;
			}
			if(count == 0)
			{
				switch_engine();	
				si[query[i]] = 0; //set as visit
				count -- ;
			}
		}
		cout << "Case #" << k << ": " << switch_count << endl;
	}
	return 0;
}