#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");


int triples[36][3];
int pairs[28][2];

int currents[26];

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		
		memset(currents,0,sizeof(currents));
		
		int numt, nump;
		
		char c;
		
		fin >> numt;
		
		for(i=0; i<numt; i++)
		{
			fin >> c;
			triples[i][0]=c-'A';
			fin >> c;
			triples[i][1]=c-'A';
			fin >> c;
			triples[i][2]=c-'A';
		}
		
		fin >> nump;
		
		for(i=0; i<nump; i++)
		{
			fin >> c;
			pairs[i][0]=c-'A';
			fin >> c;
			pairs[i][1]=c-'A';
		}
		
		vector<int> ans;
		
		fin >> n;
		
		for(i=0; i<n; i++)
		{
			fin >> c;
			k = c-'A';
			if(ans.size()>=1)
			{
				int l = ans[ans.size()-1];
				for(j=0; j<numt; j++)
				{
					if(k==triples[j][0] && l==triples[j][1])
						break;
					if(k==triples[j][1] && l==triples[j][0])													  
						break;
				}
				if(j<numt)
				{
					currents[l]--;
					ans[ans.size()-1]=triples[j][2];
					continue;
				}
			}
			ans.push_back(k);
			currents[k]++;
			
			for(j=0; j<nump; j++)
			{
				if(currents[pairs[j][0]]>0 && currents[pairs[j][1]]>0)
				{
					break;
				}
			}
			if(j<nump)
			{
				ans.clear();
				memset(currents,0,sizeof(currents));
			}
		}
		
		
		cout << "Case #" << ct << ":" << " [";
		fout << "Case #" << ct << ":" << " [";
		
		for(i=0; i<ans.size(); i++)
		{
			char c = 'A' + ans[i];
			cout << c;
			fout << c;
			if(i<ans.size()-1)
			{
				cout << ", ";
				fout << ", ";
			}
			

			
		}
		
			cout << "]" << endl;
			fout << "]" << endl; 				
		
		
	}
	
	
	return 0;
}

