#include<iostream>
#include<sstream>
using namespace std;

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		int A,B,ans=0;
		cin >> A; 
		cin >> B;
		for(int j=A;j<=B;j++)
		{
			int cmp;
			std::stringstream ss;
			std::string str;
			ss << j;
			ss >> str;
			do // won't repeat?
			{
				std::rotate(str.begin(), str.begin()+1, str.end());
				cmp = atoi(str.c_str());
				if(j < cmp && cmp <= B) ans++;
			} while(cmp!=j);
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}

