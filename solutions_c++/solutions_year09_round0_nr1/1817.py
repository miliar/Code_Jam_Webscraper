#include<iostream>
#include<string>
#include<fstream>
#include<vector>
using namespace std;

vector<string> label;
vector<string> box1[2],standard;
string tmp;
bool word[30];
int main()
{
	ofstream fout("out");
	int L,D,N;
	cin >> L >> D >> N;
	for(int i=0;i<D;i++)
	{
		cin >> tmp;
		standard.push_back(tmp);
	}
	int now,old;
	
	int place;
	for(int i=0;i<N;i++)
	{
		box1[0] = standard;
		cin >> tmp;
		now = 0;
		old = 1;
		place = 0;
		for( int i=0;i<tmp.size();i++)
		{
			old^=now^=old^=now;
			if(tmp[i]=='(')
			{
				i++;
				while(tmp[i]!=')')
					word[ tmp[i++]-'a' ] = true;
				for(int j=0;j<box1[old].size();j++)
					if( place < box1[old][j].size() && word[ box1[old][j][place]-'a' ] )
						box1[now].push_back( box1[old][j] );
				for(int k= 0;k<30;k++)
					word[k] = false;
				place ++;
				box1[old].clear();
			}
			else
			{
				for(int j=0;j<box1[old].size();j++)
				{
					if(place< box1[old][j].size() && box1[old][j][place]==tmp[i])
						box1[now].push_back(box1[old][j]);
				}
				place++;
				box1[old].clear();
			}
		}
		fout << "Case #" << i+1 << ": ";
		fout << box1[now].size() << endl;
		box1[now].clear();
	}
}