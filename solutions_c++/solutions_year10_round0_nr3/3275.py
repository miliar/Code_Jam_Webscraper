#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <queue>

using namespace std;


int main()
{
	int i=0,c=0,n=0,t=0,r=0;
	int T,R,k,N;
	string s;
	vector<long long int> arr;
	int x=0 ; 
	int toplam=0;

	freopen("small.in","r",stdin);
	freopen("output","w",stdout);

	queue<int> myqueue;
	queue<int> tempqueue;


	cin>>T;
	for(t=0;t<T;t++)
	{
		cin>>R>>k>>N;
		while(!myqueue.empty())
			myqueue.pop();
		for(n=0;n<N;n++)
		{
			cin>>x;
			myqueue.push(x);
		}
		r=0;
		while(r<R)
		{			
			c=k;
			while(!myqueue.empty() && c>=myqueue.front())
			{
				x=myqueue.front();
				myqueue.pop();
				toplam+=x;	
				tempqueue.push(x);
				c-=x;
			}
			while(!tempqueue.empty())
			{
				myqueue.push(tempqueue.front());
				tempqueue.pop();
			}
			r++;
		}
		cout<<"Case #"<<t+1<<": "<<toplam<<endl;
		toplam=0;
	}



}