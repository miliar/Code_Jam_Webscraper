
#include <iostream>
#include <fstream>
#include <vector>
#include <exception>

#define ASSERT(x, s) if (!(x)) throw (std::exception(s))


using namespace std;


class UF {
public:
	UF(int size):mSize(size)
	{
		if (size==0)size=1;
		st = new int[size];
		sz = new int[size];
		for (int i=0;i<size;++i)
		{
			st[i]=i;
			sz[i]=1;
		} 
	}
	~UF()
	{
		if (st) delete []st;
		if (sz) delete[] sz;
	}
	bool Find(int i, int j)
	{
		return Find(i)==Find(j);
	}

	void Unite(int i, int j)
	{
		i=Find(i); j=Find(j);
		if (i==j)return;
		if (sz[i]>sz[j])
		{
			st[j]=i;
			sz[i]+=sz[j];
		}
		else
		{
			sz[j]+=sz[i];
			st[i]=j;
		}
	}



	int Find(int i)
	{
		ASSERT(0<=i && i<mSize, "Index out of range!");
		int j;
		for (j=i; st[j]!=j; st[j]=st[st[j]], j=st[j]);
		return j;
	}
protected:
	int mSize;
	int* st;
	int* sz; 
};

const int MAXW = 100;
const int MAXH = 100;
int h, w;
int  sinkPoint[MAXH*MAXW];
int  height[MAXH*MAXW];
int numbPoints;
ofstream Log("log.txt");

int GetFlowTo( int j )
{
	int x = j % w;
	int y = j / w;
	int nb = -1;
	int lowestHeight = height[j];
	//North, West, East, South.
	if (y > 0 && lowestHeight > height[j-w]) { lowestHeight = height[j-w]; nb = j - w; }
	if (x > 0 && lowestHeight > height[j-1]) { lowestHeight = height[j-1]; nb = j - 1; }
	if (x < w -1 && height[j+1] < lowestHeight) { lowestHeight = height[j+1]; nb = j+1; }
	if (y < h-1 && lowestHeight > height[j+w]) { nb = j+w; }
	
	Log << " (" <<y << "," << x <<'"' << ") flow to (" <<  nb / w << "," << nb % w  << ")\n";
	return nb;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int T;
	cin >> T;
	for (int i=1; i<=T; ++i)
	{
		cin >> h >> w;
		numbPoints = h * w;
		for (int j=0; j<numbPoints; ++j)
			cin >> height[j];
		UF uf(numbPoints);
		for (int j=0; j<numbPoints; ++j)
		{
			int nb = -1;
			if ( (nb = GetFlowTo(j)) > -1 )
			{
				uf.Unite(nb, j);
			}
		}
		int a = uf.Find(0);
		
		int numLetters = 1;
		int  rootNum[26];  
		rootNum[0] = uf.Find(0);

		Log << "Case #" << i << ":\n";
		cout << "Case #" << i << ":\n";
		for (int j=0; j<numbPoints; ++j)
		{
			int rt = uf.Find(j);
			char letter = 'a';
			bool found = false;
			for (int k=0; k<numLetters; ++k)
				if (rootNum[k] == rt)
				{
					letter += k;
					found = true;
					break;
				}
			if (!found)
			{
				letter += numLetters;
				rootNum[numLetters++] = rt;
			}
			cout << letter;				
			if (j % w == w - 1) cout << '\n';
			else cout << ' ';
		}

	}
	return 0;
}
