#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>

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

template <class T>
inline std::string to_string (const T& t)
{
std::stringstream ss;
ss << t;
return ss.str();
}

int main()
{
	int i=0,k=1,t=0,n=0;
	int N,K,T;
	map<string,bool> cache;
	string s;

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
		n=2;
		for(i=1;i<N;i++)
			n*=2;
		if(K%n==n-1)
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
