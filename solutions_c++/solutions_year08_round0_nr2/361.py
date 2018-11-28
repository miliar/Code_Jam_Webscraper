#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

typedef struct
{
	float start;
	float end;
	bool atob;
}path;

void generatePath(char *times, long turnaround, bool atob, path& apath)
{
	float h1 = 0, m1 = 0, h2 = 0, m2 = 0;

	sscanf(times, "%f:%f %f:%f", &h1, &m1, &h2, &m2);
	m2 += turnaround;
	apath.start = h1 + (m1 / 60);
	apath.end = h2 + (m2 / 60);
	apath.atob = atob;
}

int comparepaths(const void *ppath1, const void *ppath2)
{
	path& path1 = *(path*)ppath1;
	path& path2 = *(path*)ppath2;

	if(path1.start < path2.start)
		return -1;
	if(path1.start > path2.start)
		return 1;
	if(path1.end < path2.end)
		return -1;
	if(path1.end > path2.end)
		return 1;
	return 0;
}

bool searchTrain(vector<float>& waiters, float time)
{
	long i, m = waiters.size(), mini = -1;
	float min = time;

	for(i = 0;i < m;++i)
	{
		if(waiters[i] <= min)
		{
			min = waiters[i];
			mini = i;
		}
	}
	if(mini == -1)
		return false;
	waiters.erase(waiters.begin() + mini);
	return true;
}

void solve(long index, istream& is, ostream& os)
{
	long i, j;
	long turnaround = 0, na, nb;
	char buffer[100];
	path *paths = NULL;
	vector<float> a, b;
	long counta = 0, countb = 0;

	is >> turnaround >> na >> nb;
	paths = new path[na + nb];
	for(i = 0;i < na;++i)
	{
		is.getline(buffer, 100);
		if(strlen(buffer) == 0)
			--i;
		else
			generatePath(buffer, turnaround, true, paths[i]);
	}
	for(j = 0;j < nb;++j)
	{
		is.getline(buffer, 100);
		if(strlen(buffer) == 0)
			--j;
		else
			generatePath(buffer, turnaround, false, paths[na + j]);
	}
	qsort(paths, na + nb, sizeof(path), &comparepaths);
	for(i = 0;i < (na + nb);++i)
	{
		path& apath = paths[i];

		if(apath.atob)
		{
			if(!searchTrain(a, apath.start))
				++counta;
			b.push_back(apath.end);
		}
		else
		{
			if(!searchTrain(b, apath.start))
				++countb;
			a.push_back(apath.end);
		}
	}
	delete [] paths;
	os << "Case #" << index << ": " << counta << " " << countb << endl;
}

int main(int argc, char* argv[])
{
	if(argc < 3)
	{
		cerr << "Usage: " << argv[0] << " inputfile outputfile" << endl;
		return 0;
	}

	filebuf ib, ob;

	if(ib.open(argv[1], ios::in) && ob.open(argv[2], ios::out))
	{
		long i, count = 0;
		istream is(&ib);
		ostream os(&ob);

		is >> count;
		for(i = 0;i < count;++i)
			solve(i + 1, is, os);
	}
	return 0;
}
