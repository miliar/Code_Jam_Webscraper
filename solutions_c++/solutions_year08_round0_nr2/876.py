#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

struct Trip {
	int from;
	int dm, am;
};

int TT;
vector<Trip> trips;

bool TCMP(Trip& ta, Trip& tb)
{
	return (ta.dm < tb.dm);
}

void solve(int id)
{
	int AA, AB;
	vector<int> SA, SB;
	sort(trips.begin(), trips.end(), TCMP);
	AA = AB = 0;
	bool bFind;
	for (size_t i = 0;i < trips.size();++i)
	{
		if (!trips[i].from)	// from A
		{
			bFind = false;
			for (size_t j = 0;j < SA.size();++j)
				if (SA[j] <= trips[i].dm)
				{
					bFind = true;
					SA.erase(SA.begin() + j);
					SB.push_back(trips[i].am + TT);
					break;
				}
			if (!bFind)
			{
				AA++;
				SB.push_back(trips[i].am + TT);
			}
		}
		else // from B
		{
			bFind = false;
			for (size_t j = 0;j < SB.size();++j)
				if (SB[j] <= trips[i].dm)
				{
					bFind = true;
					SB.erase(SB.begin() + j);
					SA.push_back(trips[i].am + TT);
					break;
				}
			if (!bFind)
			{
				AB++;
				SA.push_back(trips[i].am + TT);
			}
		}
	}
	printf("Case #%d: %d %d\n", id, AA, AB);
}

int main()
{
	//freopen("B-small.in", "r", stdin);
	////freopen("in.txt", "r", stdin);
	//freopen("B-small.txt", "w", stdout);

	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.txt", "w", stdout);

	Trip trip;
	int N, NA, NB, hd, md, ha, ma;
	scanf("%d", &N);
	for (int i = 0;i < N;++i)
	{
		trips.clear();
		scanf("%d", &TT);
		scanf("%d %d", &NA, &NB);
		trip.from = 0;
		for (int j = 0;j < NA;++j)
		{
			scanf("%d:%d %d:%d", &hd ,&md ,&ha ,&ma);
			trip.dm = hd * 60 + md;
			trip.am = ha * 60 + ma;
			trips.push_back(trip);
		}
		trip.from = 1;
		for (int j = 0;j < NB;++j)
		{
			scanf("%d:%d %d:%d", &hd ,&md ,&ha ,&ma);
			trip.dm = hd * 60 + md;
			trip.am = ha * 60 + ma;
			trips.push_back(trip);
		}
		solve(i + 1);
	}
	return 0;
}
