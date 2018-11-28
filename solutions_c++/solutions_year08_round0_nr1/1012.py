#include<iostream>
#include<string>

using namespace std;

int main()
{
	int ncases;
	int servers;
	int queries;
	char curr_query[256];
	int curr_serv;
	int answer;
	cin>>ncases;
	for(int itr=0;itr<ncases ; itr++)
	{
		answer=0;
		cin>>servers;
		char used[servers];
		char standard[servers];
		char names[servers][256];
		memset(used,0,servers);
		memset(standard,1,servers);
		char token;
		token=cin.get();
		for(int i=0;i<servers;i++)
		{
//			cin>>names[i];
			cin.getline(names[i],256);
//			cout<<(int)used[i]<<" "<<(int)standard[i]<<" "<<names[i]<<"\n";
		}
		cin>>queries;
		token=cin.get();
		for(int i=0;i<queries;i++)
		{
			cin.getline(curr_query,256);
			string temp1(curr_query);
			for(int j=0;j<servers;j++)
			{
				string temp2(names[j]);
				if(temp1==temp2)
				{
					used[j]=1;
					curr_serv=j;
//					cout<<"j"<<j<<" "<<curr_query<<" "<<(int)used[j]<<" "<<names[j]<<"\n";
					break;
				}
			}
			if(memcmp(used,standard,servers)==0)
			{
				memset(used,0,servers);
				answer++;
				used[curr_serv]=1;
			}
		}
		cout<<"Case #"<<(itr+1)<<": "<<answer<<"\n";
	}
}
