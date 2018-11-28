
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;


int main()
{
	int N,M;
	int T,Case=1;

	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);


	cin>>T;
	while(T--)
	{
		cin>>N>>M;

//		cout<<N<<M<<endl<<"CASE "<<Case<<endl;
		int i;
		vector<string> dict;
		for(i=0;i<N;i++)
		{
			string str;
			cin>>str;
			dict.push_back(str);
		//	cout<<str<<endl;
		}
		sort(dict.begin(),dict.end());

//		cout<<endl;

		vector<string> create;
		for(i=0;i<M;i++)
		{
			string str;
			cin>>str;
			create.push_back(str);
		//	cout<<str<<endl;
		}
		sort(create.begin(),create.end());


		char path[150];
		for(i=0;i<M;i++)
		{
			int size = create[i].size();
			string str="\0";
			path[0] = create[i][0];
			path[1] = '\0';
			int k=1;
			int j=1;
			while(j<=size)
			{
				if(create[i][j]=='/' || j==size)
				{
					path[k] = '\0';
					str += path;
					bool flag = false;
					for(int l=0;l<dict.size();l++)
					{
						if(str==dict[l])
						{
							flag = true; break;
						}
					}
					if(!flag)
					{
						dict.push_back(str);
					}
					path[0] = create[i][j];
					path[1] = '\0';
					k = 1;
				}
				else 
				{
					path[k] = create[i][j];
					k++;
				}
				j++;
			}
		}

		printf("Case #%d: %d\n",Case++,dict.size()-N);

		
	//	cout<<endl<<endl;
	}

	return 0;
}





