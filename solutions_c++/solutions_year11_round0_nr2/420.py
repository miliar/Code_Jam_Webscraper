#include <iostream>
#include <fstream>
#include <string>
#include <deque>

using namespace std;

int main()
{
	int T;
	ifstream fin("input.txt");
	ofstream fout("ouput.txt");
	fin >> T;
	for(int ca=0;ca<T;ca++)
	{
		int c,d,n;
		char cc[40][40]={0};
		bool dd[40][40]={false};
		fin >> c;
		for(int i=0;i<c;i++)
		{
			string t;
			fin >> t;
			cc[t[0]-'A'][t[1]-'A']=t[2]-'A'+1;
			cc[t[1]-'A'][t[0]-'A']=t[2]-'A'+1;
		}
		fin >> d;
		for(int i=0;i<d;i++)
		{
			string t;
			fin >> t;
			dd[t[0]-'A'][t[1]-'A']=true;
			dd[t[1]-'A'][t[0]-'A']=true;
		}
		fin >> n;
		string s;
		fin >> s;
		deque <char> end;
		int has[40]={0};
		for(int i=0;i<n;i++)
		{
			char nowc=s[i];
			has[nowc-'A']++;
			end.push_back(nowc);
			bool combine=false;
			while (end.size()>1)
			{
				char sec=end[end.size()-2];
				char first=end[end.size()-1];
				if (cc[first-'A'][sec-'A']!=0)
				{
					char add=cc[first-'A'][sec-'A']-1+'A';
					has[end.back()-'A']--;
					end.pop_back();
					has[end.back()-'A']--;
					end.pop_back();
					has[add-'A']++;
					end.push_back(add);
					combine=true;
				}
				else
					break;
			}
			if (!combine)
				for(int i=0;i<40;i++)
				{
					if (has[i] && dd[nowc-'A'][i])
					{
						for(int j=0;j<40;j++)
							has[j]=false;
						end.clear();
						break;
					}
				}
		}
		fout << "Case #" << ca+1 << ": [";
		for(int i=0;i<end.size();i++)
		{
			fout << end[i];
			if (i<end.size()-1)
				fout << ", ";
		}
		fout << "]\n";
	}
	return 0;
}