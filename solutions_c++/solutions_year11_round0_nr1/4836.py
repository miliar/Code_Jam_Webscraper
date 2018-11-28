#include <iostream>
#include <string>
#include <queue>
#include <vector>

using namespace std;


int main(){

	int i,j,k,t,n,r,num=1;
	string p;

	for(i=0,cin>>t;i<t;i++)
	{
		vector<string> l;
		queue<int> O;
		queue<int> B;
		int op=1,bp=1,time=0;
		bool clear=false;
		
		for(j=0,cin>>n;j<n;j++)
		{
			cin>>p;
			cin>>r;

			p=="O"?O.push(r):B.push(r);
			l.push_back(p);
		}

		for(k=0;k<n;)
		{
			if(!O.empty())
			{
				if(op==O.front() && l[k]=="O")
				{
					O.pop();
					clear=true;
				}
				else if(op!=O.front())
					op<O.front()?op++:op--;
			}
			if(!B.empty())
			{
				if(bp==B.front() && l[k]=="B")
				{
					B.pop();
					clear=true;
				}
				else if(bp!=B.front())
					bp<B.front()?bp++:bp--;
			}

			if(clear)
			{
				clear=false;
				k++;
			}
			time++;

		}

		cout << "Case #" << num << ": " << time << endl;
		num++;
	}
}
