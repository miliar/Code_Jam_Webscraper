#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int n;
int ap, al;
int bp, bl;

void process()
{
	cin >> n;
	ap = 1, al = 0;
	bp = 1, bl = 0;
	for(int i = 0; i < n; i++)
	{
		string t;
		int p;
		cin >> t >> p;
		if(t=="O")
		{
			int dif = abs(p-ap);
			al = max(al + dif + 1, bl + 1);
			ap = p;
		}
		else
		{
			int dif = abs(p-bp);
			bl = max(bl + dif + 1, al + 1);
			bp = p;
		}
	}
}

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++)
	{
		process();
		cout << "Case #" << i+1 << ": " << max(al, bl) << endl;
	}
}