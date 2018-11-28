#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <sstream>
#include <map>
#include <algorithm>
#include <fstream>
using namespace std;
int n,s,q;
map<string,int> mp;
const int MAX = 1 << 30;

vector<string> vec;

const int N = 1003;
int a[N][N];
int b[N];
ofstream out("A-largest.out");
ifstream in("A-largest.in");
#define cout out
//#define cin in


int main()
{
	cin >> n;
	for(int i = 0;i < n;i ++)
	{
		
		mp.clear();
		vec.clear();


		cin >> s;
		string st;
		getline(cin,st);
		st.clear();
		for(int j = 0;j < s;j ++)
		{
			getline(cin,st);
			mp.insert(map<string,int>::value_type(st,j));
			st.clear();
		}
		cin >> q;
	    //memset(a,MAX,sizeof(a));
		for(int j = 0;j < N;j ++)
		{
			for(int k = 0;k < N;k ++)
			{
				if(j == 0)
                  a[j][k] = 0;
				else
					a[j][k] = MAX;
			}
		}
		
		getline(cin,st);
		st.clear();
		for(int j = 0 ;j < q;j ++)
		{
			getline(cin,st);
			b[j + 1] = mp[st];
			st.clear();
		}
		for(int j = 1;j <= q;j ++)
		{
			for(int k = 0;k < s;k ++)
			{
				if(k != b[j])
				{
					a[j][k] = a[j - 1][k];

				    for(int t = 0;t < s;t ++)
				   {
					   if(a[j - 1][t] + 1 < a[j][k])
						   a[j][k] = a[j - 1][t] + 1;
					}
				}
			}
		}
		int mmin = MAX + 1;
		for(int j = 0;j < s;j ++)
		{
			if(a[q][j] < mmin)
				mmin = a[q][j];
		}
		cout << "Case #"<<i + 1 <<": ";
		cout << mmin << endl;
	}




        


			
	return 0;
}