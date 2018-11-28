#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<cstdlib>

using namespace std;


main()
{
	int cases,T,na,nb,hrs,mins,flag,min,index;
	string temp;
	vector< vector<int> > trains;
	vector<int> v,aa,ab;

	cin >> cases;

	for(int i=0;i<cases;i++)
	{
		trains.clear();
		aa.clear();
		ab.clear();
		cin >> T;
		
		cin >> na;
		cin >> nb;
		getline(cin,temp,'\n');

		for(int j=0;j<na+nb;j++)
		{
			v.clear();
			
			getline(cin,temp,':');
			hrs=atoi(temp.c_str());
			getline(cin,temp,' ');
			mins=atoi(temp.c_str());
			
			v.push_back(60*hrs + mins);
			
			getline(cin,temp,':');
			hrs=atoi(temp.c_str());
			getline(cin,temp,'\n');
			mins=atoi(temp.c_str());
			
			v.push_back(60*hrs + mins + T);

			if(j < na) v.push_back(1);
			else v.push_back(2);
			
			trains.push_back(v);
		}

		sort(trains.begin(),trains.end());

		/*for(int j=0;j<na+nb;j++)
		{
			cout<<trains[j][0]<<' '<<trains[j][1]<<' '<<trains[j][2]<<'\n';
		}*/	
		
		int nta=0,ntb=0;

		for(int j=0;j<na + nb;j++)
		{
			if(trains[j][2]==1)
			{
				flag=0;
				min=1500;
				for(int k=0;k<aa.size();k++)
				{

					if(aa[k] <= trains[j][0])
					{
						flag=1;
						if(aa[k]< min)
						{
							min=aa[k];
							index=k;
						}	
					}
				}

				if(flag==0)
				{
					nta++;
				}
				else
				{
					aa.erase(aa.begin() + index);
				}
				ab.push_back(trains[j][1]);
			}
			else if(trains[j][2] ==2)
			{
				flag=0;
				min=1500;
				for(int k=0;k<ab.size();k++)
				{

					if(ab[k] <= trains[j][0])
					{
						flag=1;
						if(ab[k]< min)
						{
							min=ab[k];
							index=k;
						}	
					}
				}

				if(flag==0)
				{
					ntb++;
				}
				else
				{
					ab.erase(ab.begin() + index);
				}
					aa.push_back(trains[j][1]);
			}

			//if(flag==0) cout<<"train assigned\n";
			//else cout<<"not assigned\n";
		}
		cout<<"Case #"<<i+1<<": "<<nta<<' '<<ntb<<'\n';
	}
}	









		


