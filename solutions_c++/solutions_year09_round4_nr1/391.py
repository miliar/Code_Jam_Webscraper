#include <iostream>  
#include <string>  
#include <vector>  
#include <set>  
#include <map>  
#include <algorithm>  
#include <math.h>  
#include <sstream>  
#include <ctype.h>  
#include <queue>  
#include <stack>  
#include <fstream>
using namespace std;  

template<class Item>  
void display(vector<Item> v)  
{  
  for(int i=0; i<v.size(); i++)  
    cout << v[i] << ' ';  
  cout << '\n';  
}   


int main()
{

int L, D, N;

fstream In("a-large.in", ios::in);
fstream Out("a-large.out", ios::out);

int T;

In >> T;

for(int h=0; h<T; h++)
{
Out << "Case #" << h+1 << ": ";

In >> N;

vector<string> v(N);

for(int i=0; i<N; i++) In >> v[i];

int ret = 0;

for(int i=0; i<N; i++)
{
	int j;
	for(j=i; j<N; j++)
	{
		int k;
		for(k=i+1; k<N; k++)
			if(v[j][k]=='1') break;
		if(k==N) break;
	}
	//cout << i << ' ' << j << endl;	
	for(int k=j; k>i; k--)
	{
		swap(v[k], v[k-1]);
		ret++;
	}

	//for(int j=0; j<N; j++) cout << v[j] << endl;

}



Out << ret << endl;

}
In.close();

Out.close();

return 0;

}
