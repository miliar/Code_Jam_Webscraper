#include <map>
#include <string>
#include <list>
#include <iostream>
#include <algorithm>
using namespace std;

int doUsuniecia(list<char> kolejka ,map< pair<char,char>,bool  > clear, char znak)
{
	list<char>::iterator itList;

	int out = 0;
	for(itList = kolejka.begin() ; itList!= kolejka.end() ; itList++)
	{
		char tmp = *itList;
		if( clear[make_pair(tmp,znak)] ==true )
		{
			return 1;
		}

	}

return 0;
}

string exec(map< pair<char,char>,char  > transform, map< pair<char,char>,bool  > clear, string slowo)
{
	list<char> kolejka;
	char last =' ';
	char current = ' ';

	for(int i = 0 ; i< slowo.size() ; i++)
	{
		if(kolejka.size())
		{
			last = kolejka.front();
			current = slowo[i];
			
			if(transform.count(make_pair(last,current))!=0 )
			{
				kolejka.pop_front();
				kolejka.push_front(transform[make_pair(last,current)]);
			}
			else if(doUsuniecia(kolejka,clear,current))
			{
				kolejka.clear();
			}
			else
			{
				kolejka.push_front(slowo[i]);
			
			}
		
		}
		else
		{
			kolejka.push_front(slowo[i]);
		}

	}

	list<char>::iterator itList;

	string omg="";
	int out = 0;
	for(itList = kolejka.begin() ; itList!= kolejka.end() ; itList++)
	{
		omg+= (*itList);
	}

	reverse(omg.begin(),omg.end());
	return omg;
}

#define LARGE
int main(int argc, char* argv[])
{
	map< pair<char,char>,char  > transform;
	map< pair<char,char>,bool  > clear;
	

#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif




	int T=0;
	int C=0;
	int D = 0;
	string tmpSlowo="";
	cin >> T;

	for(int i = 0 ;i < T ; i++)
	{
		cin >> C;
		while(C--)
		{
			cin >> tmpSlowo;
			transform[make_pair(tmpSlowo[0],tmpSlowo[1])] = tmpSlowo[2];
			transform[make_pair(tmpSlowo[1],tmpSlowo[0])] = tmpSlowo[2];


		}

		cin >> D;
		while(D--)
		{
			cin >> tmpSlowo;
			clear[make_pair(tmpSlowo[0],tmpSlowo[1])] = true;
			clear[make_pair(tmpSlowo[1],tmpSlowo[0])] = true;


		}

		cin >> D;
		cin >>tmpSlowo;

		tmpSlowo = exec(transform,clear,tmpSlowo);


		cout<<"Case #"<<i+1<<": [";

		for(int j = 0 ; j< tmpSlowo.size() ; j++)
		{
			cout<<tmpSlowo[j];
			if(j != (tmpSlowo.size()-1) )cout<<", ";
		}
		cout<<"]"<<endl;

		transform.clear();
		clear.clear();
	}


	return 0;
}

