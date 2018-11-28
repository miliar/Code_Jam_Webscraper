#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
using namespace std;

int howmuch (int i)
{
	if(i/10 == 0)
		return 1;
	if(i/100 == 0)
		return 2;
	if(i/1000 == 0)
		return 3;
	if(i/10000 == 0)
		return 4;
	if(i/100000 == 0)
		return 5;
	if(i/1000000 == 0)
		return 6;
	return 7;
}

bool find(vector<int >vec,int i)
{
	for(int k=0;k<vec.size();k++)
	{
		if(vec[k] == i)
			return false;
	}
	return true;
}

int main()
{

	int array[7]= {1,2,3,4,5,6,7};
	ofstream outfile("C://Users//fog//Desktop//1.txt");
	if(!outfile)
		cout<<"dslf"<<endl;
	int T,i,j;
	cin>>T;
	int a,b;
	for(i=0;i<T;i++)
	{
		cin>>a>>b;
		int sum = 0;
		for(;a<b;a++)
		{
			int length = howmuch(a);
			vector<int>vec;
			for(j=1;j<=length;j++)
			{
				int tempme = pow((double)10,(double)j);
				int change = a/tempme+(a%tempme)*pow((double)10,howmuch(a/tempme));
				
				if(change>a&&change<=b)
					if(find(vec,change))
						sum++;
				vec.push_back(change);
			}
		}
		outfile<<"Case #"<<i+1<<": "<<sum<<endl;

	}

	return 0;
}