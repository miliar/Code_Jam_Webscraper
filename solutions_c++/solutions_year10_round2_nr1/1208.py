#include<iostream>
#include<map>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

vector< vector < pair<string,int> > > dirContents;
vector < pair<string,int> > blank;


void cleanDirs()
{
	//cout<<"here"<<endl;
	dirContents.clear();
	dirContents.push_back(blank);
	
}

int search(vector< pair<string,int> > &v,string s)
{
	for(int i=0;i<v.size();i++)
	{
		if(v[i].first == s)
			return v[i].second;
	}
	return -1;
}


void printDirs()
{
	for(int i=0;i<dirContents.size();i++)
	{
		cout<<i<<"\t";
		for(int j=0;j<dirContents[i].size();j++)
		{
			cout<<dirContents[i][j].first;
		}
		cout<<endl;
	}
}

int addDirs(string s)
{
	int prev = 0;
	int next = 0;
	int count = 0;
	int curLocation = 0;
	int prevLocation = 0;
	string dir;
	next = s.find("/",prev+1);
	while( prev != string::npos )
	{
		dir = s.substr(prev+1,next-prev-1);
//		cout<<dir<<endl;	
		curLocation = search(dirContents[curLocation],dir);
		if(curLocation  == -1)
		{
			count ++;
		//	cout<<"new dir : "<<dir<<endl;
			dirContents[prevLocation].push_back( pair<string,int>(dir,dirContents.size()) );
			dirContents.push_back(blank);
			curLocation = dirContents.size()-1;
		}
		prevLocation = curLocation;
		prev = next;	
		next = s.find("/",prev+1);
	}
//	printDirs();
//	cout<<count<<endl;
	return count;
}


int main()
{
	int N;
	cin >> N;
	
	cleanDirs();
	
	for(int I = 0; I < N; I++)
	{
		int m,n;
		cin>>m>>n;
		
		string ip;
		for(int i=0;i<m;i++)
		{
			cin>>ip;
			addDirs(ip);
		}
		
		int count;
		count = 0;
		for(int i=0;i<n;i++)
		{
			cin>>ip;
			count+=addDirs(ip);
		}
		
		cout<<"Case #"<<I+1<<": "<<count<<endl;
		cleanDirs();
	}
}
