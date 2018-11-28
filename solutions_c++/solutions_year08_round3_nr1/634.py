#include<iostream>
#include<string>
#include<list>
using namespace std;

int main()
{
	int ncases;
	int p,k,l;
	cin>>ncases;
	int answer=0;
	list<int>::iterator repsitr;
	for(int itr=1;itr<=ncases;itr++)
	{
		cin>>p>>k>>l;
		int temp;
		list<int> reps;
		for(int i=0;i<l;i++)
		{
			cin>>temp;
			reps.push_back(temp);
		}
		reps.sort();
		reps.reverse();
		int index=1;
		temp=1;
		answer=0;
		for(repsitr=reps.begin();repsitr!=reps.end();repsitr++,temp++)
		{
			//cout<<(*repsitr)<<" ";
			answer+=(*repsitr)*index;
			if(temp%k==0)
				index++;
		}
		cout<<"Case #"<<itr<<": "<<answer<<"\n";
	}
	return 0;
}
