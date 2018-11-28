#include <iostream>
#include <string>
#include <climits>
#include <vector>
using namespace std;
int main (int argc, char **argv)
{
	int num;
	cin>>num;
	//cin.clear(); 
	//cin.ignore(INT_MAX,'\n'); 
	//string str;
	for (int i=0;i<num;i++)
	{
		cout<<"Case #"<<i + 1<<": ";
		int no,p,surp;
		cin>>no;
		cin>>surp;
		cin>>p;
		int ideal = 3 * p;
		int result=0;
		if ( p == 0)
		{
			for (int j=0;j<no;j++)
			{

				int curr;
				cin>>curr;
				if ( curr >= 0)
				{
					result ++;
				}
			}
			cout<<result<<endl;
			continue ;

		}
		for (int j=0;j<no;j++)
		{
			int curr;
			cin>>curr;
			if ( (0 < ideal-2)&&(curr>= (ideal -2)))
			{
				result ++;
			}
			else if  ((0 < ideal -4) &&(curr >= ideal -4) && surp)	
			{
				result++;
				surp--;
			}

		}
			cout<<result<<endl;
	}
		return 0;

}

