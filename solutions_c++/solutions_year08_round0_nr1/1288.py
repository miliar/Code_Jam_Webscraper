#include<iostream>
#include<vector>
#include<algorithm>
#include<cstdlib>

using namespace std;


void func(int casen)
{
	string a,b,temp;
	vector<string> quer;
	int nq,answers=0;

	getline(cin,a,'\n');
	getline(cin,b,'\n');
	
	cin >> nq;
	getline(cin,temp,'\n');
	for(int i=0;i<nq;i++)
	{
		getline(cin,temp,'\n');
		quer.push_back(temp);
	}
	
	for(int i=0;i<nq-1;i++)
	{
		if( quer[i]!= quer[i+1]) answers++;
	}
	cout<<"Case #"<<casen<<": "<<answers<<'\n';
}
		

main()
{
	int cases,nse,nq,counter,answers,remain;
	vector<string> se;
	vector<int> state(100);
	string temp;
	vector<string>::iterator iter;

	getline(cin,temp,'\n');
	cases=atoi(temp.c_str());

	for(int i=0;i<cases;i++)
	{
		se.clear();
		for(int j=0;j<100;j++)state[j]=0;

		
		getline(cin,temp,'\n');
		nse=atoi(temp.c_str());
		
		if(nse==2)
		{
			func(i+1);
			continue;
		}		

		for(int j=0;j<nse;j++)
		{
			getline(cin,temp,'\n');
			se.push_back(temp);
		}

		sort(se.begin(),se.end());

		counter=0;
		answers=0;
		remain=nse;

		getline(cin,temp,'\n');
		nq=atoi(temp.c_str());
		while(counter < nq)
		{
			getline(cin,temp,'\n');
			counter++;
			iter=find(se.begin(),se.end(),temp);
			
			if(state[iter-se.begin()] == 0) 
			{
				remain--;
				state[iter-se.begin()] = 1;

				if(remain == 1)
				{
					int j;
					for( j=0;j<nse;j++) 
					{
						if(state[j] == 0)
						{
							break;
						}	
					}
					while(counter < nq)
					{
						getline(cin,temp,'\n');
						counter++;
						if(temp == se[j])
						{
							for(int k=0;k<nse;k++)
							{
								state[k]=0;
							}
							state[j]=1;
							answers++;
							remain=nse-1;
							break;
						}
					}
				}

			}


		}

		cout<<"Case #"<<i+1<<": "<<answers<<'\n';
	}
}












