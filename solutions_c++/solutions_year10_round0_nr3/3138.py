#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>

#include <assert.h>
#include <stdlib.h>
#include <time.h>

using namespace std;

namespace
{
	const bool TEST_MODE = false;

	//const string IN_FILE_NAME("C-small-attempt0.in");
	//const string OUT_FILE_NAME("C-small-attempt.out");
	const string IN_FILE_NAME("C-large.in");
	const string OUT_FILE_NAME("C-large.out");
}

struct Group;
typedef vector<Group> Groups;

void solve_theme_park(ifstream &in, ofstream &out);
long long solve_theme_park(long long tryNum, long long maxNum, Groups &groups);
void make_test_case(ofstream &out);

struct Group
{
	Group()
		:
		m_num(0), m_index(0), m_index_in_max(0), m_euro_in_max(0), m_already(false),
		m_euro_in_loop(0), m_try_in_loop(0), m_fixed_loop_info(false)
	{}

	long long		m_num;
	int		m_index;
	int		m_index_in_max;
	long long		m_euro_in_max;
	bool	m_already;	// ループ検知用
	long long		m_euro_in_loop;
	long long		m_try_in_loop;
	bool	m_fixed_loop_info;
};

void
solve_theme_park(ifstream &in, ofstream &out)
{
	if(!in.is_open() || !out.is_open())
		return;

	int		caseNum;
	in	>>	caseNum;

	for(int i=1; i<=caseNum; ++i)
	{
		long long		tryNum;
		in	>>	tryNum;

		long long		maxNum;
		in	>>	maxNum;

		int		groupsNum;
		in	>>	groupsNum;

		vector<Group>	groups;
		groups.reserve(groupsNum);

		for(int j=0; j<groupsNum; ++j)
		{
			Group group;
			in	>>	group.m_num;
			group.m_index = j;
			groups.push_back(group);
		}

		long long total = 0;
		for(int j=0; j<groupsNum; ++j)
		{
			total += groups[j].m_num;
		}

		// maxNum以下のindex付け
		for(int j=0; j<groupsNum; ++j)
		{
			long long num = groups[j].m_num;
			int k = j+1;
			k %= groupsNum;
			while(true)
			{
				num += groups[k].m_num;

				// max超えたら終わり
				if (num > maxNum)
				{
					groups[j].m_index_in_max	= (k-1+groupsNum)%groupsNum;
					groups[j].m_euro_in_max		= num-groups[k].m_num;
					break;
				}

				// 一周したら終わり
				if (k == j)
				{
					groups[j].m_index_in_max	= (k-1+groupsNum)%groupsNum;
					groups[j].m_euro_in_max		= total;
					break;
				}

				++k;
				k %= groupsNum;
			}
		}

		long long euros = solve_theme_park(tryNum, maxNum, groups);

		// 出力
		out << "Case #"<< i << ": " << euros << endl;
	}
}

long long
solve_theme_park(long long tryNum, long long maxNum, Groups &groups)
{
	int index = 0;
	long long euros = 0;

	while(0<tryNum)
	{
		if (groups[index].m_already)
		{
			if (!groups[index].m_fixed_loop_info)
			{
				groups[index].m_fixed_loop_info = true;
				groups[index].m_euro_in_loop = euros-groups[index].m_euro_in_loop;
				groups[index].m_try_in_loop -= tryNum;
			}

			// ループ処理できそうだったらする
			if (tryNum>=groups[index].m_try_in_loop)
			{
				long long loopNum = tryNum/groups[index].m_try_in_loop;
				euros += loopNum*groups[index].m_euro_in_loop;
				tryNum %= groups[index].m_try_in_loop;
			}
			else
			{
				//// 全部ループフラグ消したらどうなる??
				//for(int i=0; i<groups.size(); ++i)
				//{
				//	groups[i].m_already = false;
				//}

				euros	+=	groups[index].m_euro_in_max;
				index	=	(groups[index].m_index_in_max+1)%groups.size();
				--tryNum;
			}
		}
		else
		{
			groups[index].m_already = true;
			groups[index].m_euro_in_loop	= euros;
			groups[index].m_try_in_loop		= tryNum;
			euros	+=	groups[index].m_euro_in_max;
			index	=	(groups[index].m_index_in_max+1)%groups.size();
			--tryNum;
		}
	}

	return euros;
}

int random(const int max, const int min=1)
{
	assert(max>min);
	float r = static_cast<float>(rand())/static_cast<float>(RAND_MAX)*static_cast<float>(max-min);
	int result = static_cast<int>(r)+min;
	assert(min<=result && max>=result);
	return result;
}

void
make_test_case(ofstream &out)
{
	if (!out.is_open())
		return;

	int caseNum = 50;
	out << caseNum << endl;

	srand(static_cast<unsigned int>(time(NULL)));
	for(int i=0; i<caseNum; ++i)
	{
		int tryMax = 100000000;
		int tryNum = random(tryMax);

		int numMax = 1000000000;
		int numNum = random(numMax);

		int groupsMax = 1000;
		int groupsNum = random(groupsMax);

		out << tryNum << " " << numNum << " " << groupsNum << endl;

		for(int j=0; j<groupsNum; ++j)
		{
			int groupMax = 10000000;
			int groupNum = random(groupMax);

			out << groupNum << " ";
		}

		out << endl;
	}
}


int main()
{
	if (TEST_MODE)
	{
		make_test_case(ofstream(IN_FILE_NAME.c_str()));
	}

	solve_theme_park(ifstream(IN_FILE_NAME.c_str()), ofstream(OUT_FILE_NAME.c_str()));

	return 0;
}