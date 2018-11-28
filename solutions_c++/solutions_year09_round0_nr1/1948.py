//Alien Language
#include<iostream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	freopen("1.in","rt",stdin);
	freopen("1.out","w",stdout);
	int l,d,n;
	vector<string> w;
	string str,s;
	
	cin >> l >> d >> n;
	
	while( d-- )
	{
		cin >> str;
		w.push_back(str);
	}
	
	for( int t = 0 ; t < n ; t++ )
	{
		vector<string> v;
		
		cin >> str;
		
		for( int j = 0 ; j < str.size() ; j++ )
		{
			if( str[j] == '(' )
			{
				s = "";
				for( ; j < str.size() && str[j] != ')' ; j++ )
					s += str[j];
					
				v.push_back(s);
				continue;
			}
			
			v.push_back(string(1,str[j]));
		}
		
		int count = 0;

		for( int i = 0 ; i < w.size() ; i++ )
		{
			bool flag = true;
			for( int j = 0 ; j < v.size() && j < w[i].size() ; j++ )
			{
				if( v[j].find(w[i][j]) == string::npos )
				{
					flag = false;
					break;
				}
			}

			count += flag;
		}
		
		cout << "Case #" << t+1 << ": " << count << endl;
	}
	
	return 0;
}
