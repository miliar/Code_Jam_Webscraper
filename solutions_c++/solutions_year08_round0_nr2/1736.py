#include <cstdio>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

#define MAX_NA_NB 20

using namespace std;

struct Time
{
	int H;
	int M;

	bool operator<(const Time& other) const
	{
		return (H < other.H || (H == other.H && M < other.M));
	}

	bool operator<=(const Time& other) const
	{
		return (H < other.H || (H == other.H && M <= other.M));
	}

	Time AddMinutes(int addM) const
	{
		Time result;
		result.H = H;
		result.M = M;
		if(addM == 60)
			result.H += 1;
		else
		{
			result.M += addM;
			if(result.M >= 60)
			{
				result.H += 1;
				result.M -= 60;
			}
		}
		return result;
	}
};

// start, end time
struct SETime
{
	int index; // ���� SE �� �ε��� ( ���Ľ� �����ϱ� ���� )
	Time st; // depature
	Time et; // arival

	SETime() : index(-1) {}
};

bool et_less(const SETime& se1, const SETime& se2)
{
   return se1.et < se2.et;
}

void solve_case(int T, const vector<SETime>& timeAB, const vector<SETime>& timeBA)
{
	const int NA = timeAB.size();
	const int NB = timeBA.size();

	// ����
	vector<SETime> arrival_sorted_AB = timeAB; // AB �� �����ð����� sorting �� ��
	sort(arrival_sorted_AB.begin(), arrival_sorted_AB.end(), et_less);
	vector<SETime> arrival_sorted_BA = timeBA; // BA �� �����ð����� sorting �� ��
	sort(arrival_sorted_BA.begin(), arrival_sorted_BA.end(), et_less);

	int need_a = NA; // A ������ ���� need
	int need_b = NB; // B ������ ���� need

	bool check_a[MAX_NA_NB] = { false, };
	bool check_b[MAX_NA_NB] = { false, };

	// A ���� B �� ��츦 ���� ����.
	// timeAB �� �� �������� et + T �� timeBA �� st ���� �۴ٸ�, timeBA �� ������ �پ���.
	for(int ai=0; ai<NA; ++ai)
	{
		for(int bi=0; bi<NB; ++bi)
		{
			// AB �� �����ð�(+ ��ȯ�ð�)��, (���ĵ�) BA �� ��߽ð����� �����ٸ� �����ϳ��� ���� �� �ִ�.
			if(false == check_b[bi] && timeAB[ai].et.AddMinutes(T) <= arrival_sorted_BA[bi].st)
			{
				check_b[bi] = true;
				--need_b; // ���� �ϳ� ���̱�!
				break; // bi �� ������ �ϳ��� ���ϴ�.
			}
		}
	}

	// ���� Ŭ��
	for(int bi=0; bi<NB; ++bi)
	{
		for(int ai=0; ai<NA; ++ai)
		{
			if(false == check_a[ai] && timeBA[bi].et.AddMinutes(T) <= arrival_sorted_AB[ai].st)
			{
				check_a[ai] = true;
				--need_a; // ���� �ϳ� ���̱�!
				break; // bi �� ������ �ϳ��� ���ϴ�.
			}
		}
	}

	printf("%d %d\n", need_a, need_b);
}

int main(int argc, char* argv[])
{
	int N;  // 1 ~ 100 ( cases )
	int NA; // 0 ~ 20  ( A->B times )
	int NB; // 0 ~ 20  ( B->A times )
	int T;  // 0 ~ 60  ( turnaround time ; minutes )

	vector<SETime> timeAB;
	vector<SETime> timeBA;

	scanf("%d", &N);

	for(int ni=0; ni<N; ++ni)
	{
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);

		timeAB.resize(NA);
		timeBA.resize(NB);

		for(int i=0; i<NA; ++i)
		{
			scanf("%d:%d %d:%d", &timeAB[i].st.H, &timeAB[i].st.M, &timeAB[i].et.H, &timeAB[i].et.M); 
			timeAB[i].index = i;
		}

		for(int i=0; i<NB; ++i)
		{
			scanf("%d:%d %d:%d", &timeBA[i].st.H, &timeBA[i].st.M, &timeBA[i].et.H, &timeBA[i].et.M);
			timeBA[i].index = i;
		}

		printf("Case #%d: ", ni + 1);
		solve_case(T, timeAB, timeBA);
	}
}
