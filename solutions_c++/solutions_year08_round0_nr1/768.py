#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<fstream>
using namespace std;


int main()
{
	fstream f;
	f.open("out.out");
	int N;
	scanf("%d", &N);
	int case_count = 0;
	for(; N>0; N--)
	{
		case_count++;
		int S;
		scanf("%d", &S);
		string blank_tmp;
		getline(cin, blank_tmp);
		map<string, int> m;
		for(; S>0; S--)
		{
			string str;
			getline(cin, str);
			m[str] = (int)2000;
			continue;
		}
		int Q;
		scanf("%d", &Q);
		getline(cin, blank_tmp);
		vector<string> v;
		int i = 0;
		for(i = 0; i < Q; i++)
		{
			string str;
			getline(cin, str);
			v.push_back(str);
			if(m[str] == 2000) m[str] = i;
		}
		map<string,int>::iterator ptr = m.begin();
		map<string,int>::iterator min = ptr, max = ptr;
		bool zero_times_flag = false;//即有些情况下有个搜索引擎没有用到，这样中心直接设为这个搜索引擎即可
		for(ptr = m.begin(); ptr != m.end(); ptr++)
		{
			if(ptr->second == 2000)
			{
				printf("Case #%d: 0\n", case_count);
				f << "Case #" << case_count <<": 0\n";
				zero_times_flag = true;
				break;
			}
			if(ptr->second > max->second) max = ptr;
			if(ptr->second < min->second) min = ptr;
		}
		if(zero_times_flag == true) continue;//再往下就是需要计算的了

		string cur_center = max->first;

		int current = 0;
		string cur_str;
		int count = 0;
		string toSwitch = "00000000";
		while(true)
		{
			cur_str = v[current];
			if(cur_str == cur_center)
			{
				if(toSwitch != "00000000")
				{
					count++;
					break;
				}
				min = m.begin(), max = m.begin();
				for(ptr = m.begin(); ptr != m.end(); ptr++)
				{
					if(ptr->second > max->second) max = ptr;
					if(ptr->second < min->second) min = ptr;
				}
				cur_center = max->first;
				if(current != 0) count++;
			}
			current++;
			for(i = current; i < Q; i++)
			{
				if(v[i] == cur_str)
				{
					m[cur_str] = i;
					break;
				}
			}
			if(i == Q) toSwitch = cur_str;//
		}
		printf("Case #%d: %d\n", case_count, count);
		f << "Case #" << case_count <<": " << count << "\n";
	}
	f.close();
	return 0;
}