#include <iostream>
#include <cstring>
#include <vector>

using namespace std;


vector<string> alienwords;
int pattern[20][40];

bool matchaa(string &a)
{
	for(int i = 0; i < a.length(); i++)
	{
		if(pattern[i][a[i]-'a'])
			continue;
		else
			return false;
	}
	return true;
}

int main()
{
	int l,d,n;
	cin>>l>>d>>n;
	
	for(int i = 0; i < d; i++)
		{
			char buff[512];
			cin>>buff;
			alienwords.push_back(buff);
		}
	
	for(int i = 0; i < n; i++)
	{
		char buff[512];
		cin>>buff;
		string patterni = buff;
		memset(pattern,0,sizeof(pattern));
		
		int indeksi = 0;
		int indeksi2 = 0;
		while(indeksi < patterni.length())
		{
			if(patterni[indeksi] <= 'z' && patterni[indeksi] >= 'a')
			{
				pattern[indeksi2][patterni[indeksi]-'a']=1;
				indeksi++;
				indeksi2++;
			}
			else
			{
				indeksi++;
				while(patterni[indeksi] != ')')
				{
					pattern[indeksi2][patterni[indeksi]-'a']=1;
					indeksi++;
				}
				indeksi++;
				indeksi2++;
			}
			
			
		}
		
		int lkm = 0;
		for(int j = 0; j < d; j++)
		{
			if(matchaa(alienwords[j]))
				lkm++;
		}
		
		cout<<"Case #"<<(i+1)<<": "<<lkm<<endl;
	}
	
}
