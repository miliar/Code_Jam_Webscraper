#include<iostream>
#include <set>
using namespace std;

void main()
{
	int T;

	cin>>T;
	for(int i=0;i<T;i++)
	{
		int n;
		cin >> n;
		multiset<int> vx,vy;
		for (int a=0;a<n;a++)
		{
			int x;
			cin>>x;
			vx.insert(x);
		}
		for (int a=0;a<n;a++)
		{
			int y;
			cin>>y;
			vy.insert(y);
		}
		multiset<int>::iterator vxit = vx.begin();
		multiset<int>::reverse_iterator vyit = vy.rbegin();
		int kekka=0;
		while(vxit!=vx.end()||vyit!= vy.rend())
		{
			kekka+=(*vxit)*(*vyit);
			//cout << kekka<<endl;
			++vxit;
			++vyit;
		}
		cout << "Case #" <<  i+1 << ": " << kekka << endl;
		vx.clear();
		vy.clear();


	}
}