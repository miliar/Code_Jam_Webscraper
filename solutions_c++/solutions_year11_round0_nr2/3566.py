#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

#define db(x) cout<< #x << " : " <<x <<endl;
#define pb push_back
#define mp make_pair

typedef unsigned long long ull;
typedef long long ll;
typedef pair<int,int> ii;

void PV(vector<int> v)
{
	cout << "\n";
	for(int i=0; i<v.size(); i++)
		cout << v[i] << " ";
	cout << "\n";
}


int main()
{
	int T;
	cin >> T;
	for(int z=1; z<=T; z++)
	{
		
		int C,D,N;
		cin >> C;
		string Combine[C];
		for(int i=0; i<C; i++)
			cin >> Combine[i];
		
		cin >> D;
		string Oppose[D];
		for(int i=0; i<D; i++)
			cin >> Oppose[i];
		
		cin >> N;
		string str,ans = "";
		cin >> str;
		
		int len = 0;
		ans += str[0];
		bool changed ;
		for(int i=1; i<N; i++)
		{
			changed = false;
			//Combine..
			for(int j=0; j<C; j++)
			{
				if(len >= 0)
				if(Combine[j][0] == ans[len] && Combine[j][1] == str[i] || Combine[j][1] == ans[len] && Combine[j][0] == str[i])
				{
					ans[len] = Combine[j][2];
					changed = true;	
				}
			}
			
			
			if(!changed)
			{	
				//Oppose..
				for(int j=0; j<D; j++)
				{
					
					if(str[i] == Oppose[j][0] && ans.find(Oppose[j][1]) != string::npos) 
					{
						ans = "";
						len = -1;
						changed = true;
					}
					else if(str[i] == Oppose[j][1] && ans.find(Oppose[j][0]) != string::npos)
					{
						ans = "";
						len = -1;
						changed = true;
					}
				}
				
			}
			
			if(!changed)
			{
				ans += str[i];
				len ++;
			}
		}
		
		cout << "Case #" << z << ": [";
		if(len >= 0)
		{
			for(int i=0; i<len; i++)
				cout << ans[i] << ", ";
		
			cout << ans[len];
		}
		cout << "]" << endl;
	}
	
	
	
    return 0;
}
