#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int i,t,r,k,n;
    cin >> t;
    for(i=1;i<=t;i++)
    {
	vector<int> riders;
	long long rides=0;
	int next=0;
	cin >> r >> k >> n;
	int g[n];
	for(int j=0;j<n;j++) cin >> g[j];
	int l;
	for(l=0;l<r;l++)
	{
	    int curriders=0;
	    int start=next;
	    while(g[next]+curriders<=k && (start != next || curriders == 0))
	    {
		curriders+=g[next];
		next=(next+1)%n;
	    }
	    rides+=curriders;
	    riders.push_back(curriders);
	    if(next==0) // Found a pattern!
	    {
		l++;
		break;
	    }
	}
	rides*=(r/l); // Repeat the pattern
	for(int j=0;j<r%l;j++) // Fill in the rest
	{
	    rides+=riders[j];
	}
	cout << "Case #" << i << ": " << rides << endl;
    }
    return 0;
}
