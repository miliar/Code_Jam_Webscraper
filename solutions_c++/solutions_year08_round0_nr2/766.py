#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<algorithm>
using namespace std;

class Node
{
public:
	int start;
	int end;
	Node(int s, int e)
	{
		start = s;
		end = e;
	}
};

bool cmp(Node n1, Node n2)
{
	if(n1.start < n2.start) return true;
	else return false;
}

int main()
{
	fstream f;
	f.open("out.out");
	int N, case_count = 0;
	scanf("%d", &N);
	for(; N>0 ; N--)
	{
		case_count++;
		int T, NA, NB;
		string blank_tmp;
		scanf("%d%d%d", &T, &NA, &NB);
		getline(cin,blank_tmp); 
		vector<Node> m_atob_start, m_atob_end, m_btoa_start, m_btoa_end;
		for(int i = 0; i < NA; i++)
		{
			string char_tmp;
			int sum1, sum2;
			getline(cin, char_tmp);
			sum1 = char_tmp[0]*600 + char_tmp[1]*60 + char_tmp[3]*10 + char_tmp[4];
			sum2 = char_tmp[6]*600 + char_tmp[7]*60 + char_tmp[9]*10 + char_tmp[10];
			Node tmp1(sum1, sum2), tmp2(sum2+T, sum1);
			m_atob_start.push_back(tmp1);
			m_atob_end.push_back(tmp2);;
		}
		for(int i = 0; i < NB; i++)
		{
			string char_tmp;
			int sum1, sum2;
			getline(cin, char_tmp);
			sum1 = char_tmp[0]*600 + char_tmp[1]*60 + char_tmp[3]*10 + char_tmp[4];
			sum2 = char_tmp[6]*600 + char_tmp[7]*60 + char_tmp[9]*10 + char_tmp[10];
			Node tmp1(sum1, sum2), tmp2(sum2+T, sum1);
			m_btoa_start.push_back(tmp1);
			m_btoa_end.push_back(tmp2);
		}

		sort(m_atob_start.begin(), m_atob_start.end(), cmp);
		sort(m_btoa_start.begin(), m_btoa_start.end(), cmp);
		sort(m_atob_end.begin(), m_atob_end.end(), cmp);
		sort(m_btoa_end.begin(), m_btoa_end.end(), cmp);

		int count_a = 0, count_b = 0;
		while(m_atob_start.size() != 0 && m_btoa_end.size() != 0)
		{
			if(m_atob_start.begin()->start < m_btoa_end.begin()->start)
			{
				count_a++;				
			}
			else
			{
				m_btoa_end.erase(m_btoa_end.begin());
			}
			m_atob_start.erase(m_atob_start.begin());
		}
		count_a += m_atob_start.size();

		while(m_btoa_start.size() != 0 && m_atob_end.size() != 0)
		{
			if(m_btoa_start.begin()->start < m_atob_end.begin()->start)
			{
				count_b++;				
			}
			else
			{
				m_atob_end.erase(m_atob_end.begin());
			}
			m_btoa_start.erase(m_btoa_start.begin());
		}
		count_b += m_btoa_start.size();

		printf("Case #%d: %d %d\n", case_count, count_a, count_b);
		f << "Case #" << case_count << ": " << count_a << " "<< count_b <<endl;
	}
	f.close();
	return 0;
}