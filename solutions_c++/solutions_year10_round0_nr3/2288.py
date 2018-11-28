#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include <queue>

using namespace std;


int main()
{
	int cases;
	cin >> cases;
	
	int Round, Cap, Group;
	int temp;

	for (int i=0; i<cases; i++){
		int count=0;

		cin>>Round>>Cap>>Group;
		
		queue<int> gc; // group composition
		for (int j=0; j<Group; j++)
		{
			cin>>temp;
			gc.push(temp);
		}
		
		
		queue<int> used;
		while (Round> 0)
		{
			
			int n=0; // actual number of riders
			
			//cout<<"size is "<<gc.size()<<endl;
			while (!gc.empty()) {
				int token = gc.front();
			//	cout<<"token "<<token<<" Cap "<<Cap<<endl;
				
				if (n+token>Cap)
					break;

				
				used.push(token);
			//					cout<<"used "<<used.back()<<endl;
				n+=token;
				gc.pop();
			}
			
		//	cout << "used size is "<<used.size()<<endl;
			
			// adds back to queue
			int usedsize=used.size();
			for (int i=0; i<usedsize; i++)
			{
				gc.push(used.front());
				//cout<<"pushing back "<<used.front();

				used.pop();
			}
	

			count+=n;
			Round--;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}

	
	return 0;
}