#define LARGE
#include <iostream>
#include <set>
using namespace std;

int SplitNumbers(int A, int *AA);
int GetNumOfRecycle(int A, int B)
{
	int XX[10];
	int num = 0;
	set<int> mySet;
	for(int X=A; X<B; X++ )
	{
		int size = SplitNumbers(X,XX);
		mySet.clear();
		for(int i = size-2; i >=0; i--)
		{
			if( XX[i] == 0 || XX[i] < XX[size-1])
				continue;

			int newX = 0;
			for(int k=i;k>=0;k--)
				newX = 10*newX + XX[k];
			for(int k=size-1; k >i ; k--)
				newX = 10*newX + XX[k];
			if(newX > X && newX <=B)
			{
				if(mySet.find(newX) == mySet.end())
				{
					mySet.insert(newX);
					num++;
				}
			}
		}
	}
	return num;
}


int SplitNumbers(int A, int *AA)
{
	int i = 0;
	while( A > 0 )
	{
		AA[i++] = A % 10;
		A = A / 10;
	}
	return i;
}

int main()
{  
#ifdef TEST
    freopen("A.txt","rt",stdin);
	freopen("A-out.txt","wt",stdout);
#endif

#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-out.txt","wt",stdout);
#endif

#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large-out.txt","wt",stdout);
#endif

    int num = 0;
    cin >> num;
	int A, B;

    for( int i=0; i<num; i++ )
    {
       cin >> A >> B;

	   cout << "Case #" << i+1 << ": " << GetNumOfRecycle(A, B) << endl;
    }
}