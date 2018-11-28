#include<iostream>
#include<string>
#include<list>
using namespace std;

string engine[100];
int count;
list <string> valid;

int main()
{
	int N,N2,S,Q,i,j,count;
	string name;
	cin>>N;
	//cout<<"N = "<<N<<endl;
	N2 = N;
	while(N--)
	{
		valid.clear();
		count=0;
		cin>>S;
		//cout<<"S = "<<S<<endl;
		getline(cin,name);
		for(i=0; i<S; i++)
		{
			getline(cin,name);
			engine[i]=name;
			//cout<<"engine # "<<i<<" = "<<engine[i]<<endl;
			valid.push_back(name);
		}
		cin>>Q;
		//cout<<"Q = "<<Q<<endl;
		getline(cin,name);
		for(i=0; i<Q; i++)
		{
			getline(cin,name);
			//cout<<"input = "<<name<<endl;
			valid.remove(name);
			if(valid.size()==0)
			{
				count++;
				for(j=0; j<S; j++)
					valid.push_back(engine[j]);
				valid.remove(name);
			}
			//cout<<"valid = ";
			//for(list<string>::iterator j=valid.begin(); j!=valid.end(); j++)
			//	cout<<(*j)<<' ';
			//cout<<endl;
		}
		cout<<"Case #"<<N2-N<<": "<<count;
		if(N)
			cout<<endl;
	}
}
