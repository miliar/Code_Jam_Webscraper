#include<iostream>
#include<algorithm>
#include<sstream>
#include<string>

using namespace std;


int main()
{

	int cases,caseNo=1;
	cin>>cases;
	while(cases--)
	{
		int A,B;
		cin>>A>>B;
		int total=0;
		for(int it=A; it<=B; it++)
		{
			stringstream ss;
			ss<< it;

			string tempStr=ss.str();
			int size = tempStr.size();
			char arr[size];

			int temp;
		
			for(int i=1; i<size ; i++)
			{
				int y=0;
				for(int j=i, x=i; j <= (size + i -1) ; x=(++j)%(size))
				{
					arr[y++]=tempStr[x];
				}
				temp=atoi(arr);
				if(temp>it)
				{
					if(temp >= A && temp <=B)
						total++;
				}
			}
		}
		cout<<"Case #"<<caseNo<<": "<<total<<endl;
		caseNo++;	
	}

	return 0;
}
