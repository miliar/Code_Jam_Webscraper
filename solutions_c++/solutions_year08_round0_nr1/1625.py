#include<iostream>
#include<string>
using namespace std;
int main()
{
	int i,j,k;
	int cases;
	cin>>cases;
	for(k=0;k<cases;k++)
	{
		string *engine, *query;
		bool *test;
		int ne,nq,swich=0;
		cin>>ne;
		engine = new string[ne];
		test = new bool[ne];
		getline(cin,engine[0],'\n');
	
		for(i=0;i<ne;i++)
		{
			getline(cin,engine[i],'\n');
			test[i] = false;
		}
	
		cin>>nq;
		if(nq>0)
		{
		query = new string[nq];
		getline(cin,query[0],'\n');
		for(i=0;i<nq;i++)
			getline(cin,query[i],'\n');
	
		bool result;
		for(i=0;i<nq;i++)
		{
			for(j=0;j<ne;j++)
			{
				if(query[i] == engine[j])
					test[j] = true;
			}
			result = true;
			for(j=0;j<ne;j++)
				result = result && test[j];

			if(result == true)
			{	
				swich++;
				i--;
				for(j=0;j<ne;j++)
					test[j] = false;
			}
		}
		}
		cout<<"Case #"<<k+1<<": "<<swich<<endl;
	}
	return 0;
	
}
