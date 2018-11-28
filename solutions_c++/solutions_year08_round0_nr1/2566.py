#include<iostream>
#include<string>
#include<vector>
using namespace std;
int getindex(string str, vector<string> vec); 
int getno(int *list, int i, int n);
int senext(vector<string> query, vector<string> searchengine, int curquery);
int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-out.txt", "w", stdout);
	int *list;	
	int n, s, q, count=0, switches=0;
	char ch;
	cin>>n;
//	cout<<n<<endl;
	while(n--)
	{
		vector<string> searchengine, query;
		count++;
		switches = 0;
		cin>>s;
//		cout<<s<<endl;
		cin.get();
		while(s)
		{
			string temp;
			getline(cin, temp, '\n');
//			cout<<temp<<endl;
			searchengine.push_back(temp);
			s--;
		}
		cin>>q;
//		cout<<q<<endl;
		cin.get();
		while(q)
		{
			string temp;
			getline(cin, temp, '\n');
//			cout<<temp<<endl;
			query.push_back(temp);
			q--;
		}
		list = new int[s];
		for(int i=0;i<s;i++)
		{
			list[i] = 0;
		}
		int curquery = 0, seused = 0;
		seused = senext(query, searchengine, curquery);
		curquery = 1;
		for(;curquery<query.size();curquery++)
		{
			//cout<<"cur se is "<<searchengine[seused]<<endl;
			if(query[curquery].compare(searchengine[seused]) == 0)
			{
			//	cout<<"query is "<<query[curquery];
				switches++;
				seused = senext(query, searchengine, curquery);
			//	cout<<"switch to search engine "<<searchengine[seused]<<endl;
			}
		}
		cout<<"Case #"<<count<<": "<<switches<<endl;
					
	}
	return 0;
}
int getindex(string str, vector<string> vec)
{
	for(int i = 0;i<vec.size();i++)
	{
		if(str.compare(vec[i]) == 0) return i;
	}
	return -1;
}

int getno(int *list, int i, int n)
{
	for(int j=0;j<n;j++)
	{
		if(list[j] == i) return j;
	}
	return -1;
}
int senext(vector<string> query, vector<string> searchengine, int curquery)
{
	int *list;
	list = new int[searchengine.size()];
	int last;
	for(int i=0;i<searchengine.size();i++)
	{
		list[i]=0;
	}
	int temp;
	for(int i=curquery;i<query.size();i++)
	{
		temp = getindex(query[i], searchengine);
		if(list[temp] == 0)
			last = temp;
		list[temp] = 1;
	}
	for(int i=0;i<searchengine.size();i++)
	{
		if(list[i] == 0)
			last = i;
	}
	return last;
}