#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int find_ans(vector <pair <int,int>> vo , vector< pair <int,int>> vb)
{
	int ans;
	int first_robo = 1,	second_robo = 1;
	for (ans = 0 ; vo.size() || vb.size(); ans++)
	{
		bool flag = false;
		int s1 = vo.size();
		int s2 = vb.size();
		if (s1)
			if (vo[s1 - 1].first < first_robo)
				first_robo--;
			else
				if (vo[s1 - 1].first > first_robo)
					first_robo++;
				else
					if (first_robo == vo[s1 - 1].first && (s2 == 0 || vo[s1 - 1].second < vb[s2 - 1].second))
						flag = true;
		if (s2)
			if (vb[s2 - 1].first < second_robo)
				second_robo--;
			else
				if(vb[s2 - 1].first > second_robo)
					second_robo++;
				else
					if (second_robo == vb[s2 - 1].first &&(s1 == 0 || vb[s2 - 1].second < vo[s1 - 1].second))
						flag = true;
		if (flag)
			if (s2 == 0 || (s1 && vo[s1 - 1].second < vb[s2 - 1].second))
				vo.pop_back();
			else
				vb.pop_back();		
	}
	return ans;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int i = 0 ; i < t; i++)
	{
		vector < pair <int,int>> v1 , v2;
		int n; cin >> n;
		for(int j = 0 ; j < n; j++)
		{
			char ch; 
			int k;
			cin >> ch >> k;
			if (ch =='O')
			v1.push_back(make_pair(k,j));
			else
			v2.push_back(make_pair(k,j));
		}
		reverse(v1.begin(),v1.end());
		reverse(v2.begin(),v2.end());
		int ans = find_ans(v1,v2);
		cout <<"Case #" << i + 1 <<": "<< ans <<'\n';
	}
	return 0;
}
