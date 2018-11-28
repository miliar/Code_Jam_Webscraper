#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;



int main()
{

	int T;
	cin >> T;
	for(int test = 0; test < T;test++)
	{
		string x;
		cin >> x;
		string y = x;
		//sort(x.begin(),x.end());
		//while(x != y)
		//{
			//next_permutation(x.begin(),x.end());
		//}
		if( next_permutation(x.begin(),x.end()) == false)
		{
			sort(x.begin(),x.end());
			string t;
			t.push_back(x[0]);
			t.push_back('0');
			for(int i = 1; i < x.size();i++)
			{
				t.push_back(x[i]);
			}
			x = t;
			for(int i = 0; i < x.size();i++)
			{
				if(x[i] != '0')
				{
					char c = x[0];
					x[0] = x[i];
					x[i] = c;
					break;
				}
			}
			//while(x[0] == '0')
				//next_permutation(x.begin(),x.end());
		}
		cout << "Case #" << test+1 << ": " << x << endl;
	}


}