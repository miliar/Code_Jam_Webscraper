#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(void)
{
	int numofcase;
	cin>>numofcase;
	string temp;
	for(int i=0; i<numofcase ; i++)
	{
		int N,S,p,t,result=0,left;
		cin>>N>>S>>p;
		vector <int> array ;
		left = S;
		for( int j = 0 ; j<N ;j++)
		{
			int t;
			cin>>t;
			array.push_back(t);
			
		}
			for(int k=0;k<N;k++)
			{
				

				int elem = array[k];
				if(elem >= (3*p-2))
				{
					result++;
				}
				else if((elem >=(3*p-4))&&(left>=1))
				{
					if((p-1)>0)
					{
					result++;
					left--;}
				}
			}
		cout<<"Case #"<<(i+1)<<": "<<result<<endl;
	}
return 0;
}	















