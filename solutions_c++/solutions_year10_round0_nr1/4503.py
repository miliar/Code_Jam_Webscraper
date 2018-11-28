#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

typedef struct Node
{
	int index;
	bool power;
	bool onOff;
	Node() { }
	Node(int i,bool p,bool o):index(i),power(p),onOff(o)
	{}
} _Node;


int main()
{
	int i=0,k=1,t=0,n=0;
	int N,K,T;

	Node *arr=new Node[30];
	for(int i=0;i<30;i++)
	{
		arr[i]=Node(i,false,false);
	}
	arr[0].power=true;
	


	freopen("small.in","r",stdin);
	freopen("output","w",stdout);

	

	cin>>T;
	while(t<T)
	{
		cin>>N>>K;
		for(int i=0;i<N;i++)
		{
			arr[i].onOff=false;
			arr[i].power=false;
		}
		arr[0].power=true;
		for(k=0;k<K;k++)
		{
			arr[0].onOff=!arr[0].onOff;
			for(n=1;n<N;n++)
			{
				if(arr[n].power)
					arr[n].onOff=!arr[n].onOff;		
				arr[n].power=arr[n-1].power && arr[n-1].onOff;
			}
			if(arr[0].onOff)
				arr[1].power=true;
		}

		if(arr[N-1].power && arr[N-1].onOff)
		{
			cout<<"Case #"<<t+1<<": "<<"ON"<<endl;
		}
		else 
		{
			cout<<"Case #"<<t+1<<": "<<"OFF"<<endl;
		}
		t++;
	}


	return 0;
}
