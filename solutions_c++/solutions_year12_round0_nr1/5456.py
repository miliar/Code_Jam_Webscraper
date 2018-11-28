#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <memory.h>
#include <set>
#include <algorithm>

using namespace std;
					//	"abcdefghijklmnopqrstuvwxyz"
unsigned char arar[] =	"yhesocvxduiglbkrztnwjpfmaq";


//a -> y
//b -> h
//c -> e
//d -> s
//e -> o
//f -> c
//g -> l
//h -> x
//i -> d
//j -> u
//k -> i
//l -> g
//m -> l
//n -> b
//o -> e
//p -> r
//q -> z
//r -> t
//s -> n
//t -> w
//u -> j
//v -> p
//w -> f
//x -> m
//y -> a
//z -> q

int main()
{

	freopen("A.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int n;
	char c;
	//cin>>n;
	char line[2000];
	scanf("%d%c", &n, &c);
	vector<string> in,out;
	for(int i =0 ;i < n; i++)
	{
		cin.getline(line, 200);
		in.push_back(line);
	}
	//for(int i =0 ;i < n;i++)
	//{
	//	cin.getline(line, 200);
	//	out.push_back(line+9);
	//}
	for(int i =0 ;i < n;i++)
	{
		string s;
		for(int j =0 ;j< in[i].size();j++)
		{
			if(in[i][j] >= 'a' && in[i][j] <= 'z')
				s.push_back(arar[in[i][j] - 'a']);
			else
				s.push_back(in[i][j]);
		}
		out.push_back(s);
	}

	/*for(int i =0 ;i<255; i++)
	{
		cout<<(unsigned char)i<<" -> "<<arar[i]<<endl;
	}*/
	//in.clear();
	//for(int i =0 ;i < n; i++)
	//{
	//	cin.getline(line, 200);
	//	in.push_back(line+9);
	//}
	int i;
	for( i= 0; i < n-1 ;i++)
	{
	/*	for(int j =0 ;j< in[i].size();j++)
		{
			if(in[i][j]!=out[i][j])
			{
				cout<<in[i][j]<<" "<<out[i][j]<<endl;
			}
		}*/
		printf("Case #%d: %s\n",i+1, out[i].c_str());
	}
	printf("Case #%d: %s",i+1, out[n-1].c_str());
	return 0;
}