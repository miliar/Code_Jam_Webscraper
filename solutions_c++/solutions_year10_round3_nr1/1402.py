#include<iostream.h>
#include<fstream.h>
#include <vector>
#include <functional>      //For greater<int>( )

#define int64 __int64

//vector<int64> v1;
//vector<int64>::iterator itr;

int main()
{
	ifstream is;
	ofstream os;
	
	is.open("A-large.in");
	os.open("outputl");
	
	int n,cnt,num;

	
	is>>cnt;
	for(int rc=1; rc<=cnt; rc++)
	{
		is>>num;

		int64 arr[1000][2];

		int64 a,b;
		int y=0;
		for(int i=0; i<num; i++)
		{
			is>>a; is>>b;
			
			for(int j=0; j<i; j++)
			{
				if((a < arr[j][0] && b > arr[j][1]) || (a > arr[j][0] && b < arr[j][1]))
					y++;
			}

			arr[i][0] = a;
			arr[i][1] = b;
		}
		os<<"Case #"<<rc<<": "<<y<<endl;
		//cout<<"Case #"<<rc<<": "<<y<<endl;
	}
	os.flush();

	is.close();
	os.close();
	
	return 0;
}
