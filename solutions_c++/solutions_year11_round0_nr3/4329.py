#include<iostream>
#include<string>
#include<bitset>
#include<vector>

using namespace std;

int main()
{
	freopen("C-small-attempt6.in", "r", stdin);
	freopen("out.in", "w", stdout);
	int T;
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		vector < int > vecto;
		int adad;
		cin >> adad;
		int num;
		for(int j = 0; j < adad; j++)
		{
			cin >> num;
			vecto.push_back(num);
		}
		vector < string > vect;
		for(int j = 0 ; j < vecto.size(); j++)
		{
			bitset<21> mybit1 (vecto[j]);
			vect.push_back(mybit1.to_string<char,char_traits<char>,allocator<char> >());
		}
		bool yes = false;
		int max = 0;
		for(int g = 0; g < vect.size(); g++)
		{
			string sum1(21, '0');
			int s1 = 0;
			for(int j = g; j < vect.size()-1; j++)
			{
				s1 += vecto[j];
				for(int m = vect[j].size()-1; m >= 0; m--)
				{
					if(sum1[m] == vect[j][m])
						sum1[m] = '0';
					else
						sum1[m] = '1';
				}
				string sum2(21, '0');
				int k = j+1;
				int s = 0;
				while(k != g)
				{
					s += vecto[k];
					for(int m = vect[k].size()-1; m >= 0; m--)
					{
						if(sum2[m] == vect[k][m])
							sum2[m] = '0';
						else
							sum2[m] = '1';
					}
					k++;
					if(k == vect.size())
						k = 0;
				}
				if(sum1 == sum2)
				{
					/*for(int l = j+1; l < vecto.size(); l++)
						s += vecto[l];*/

					if(max < s)
						max = s;
					if(max < s1)
						max = s1;
					yes = true;
					//break;
				}
			}
		}
		if(yes == true)
			cout << "Case #" << i+1 << ": " << max << endl;
		else
			cout << "Case #" << i+1 << ": NO" << endl;
	}
}