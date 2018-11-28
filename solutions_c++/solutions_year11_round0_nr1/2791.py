#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream f;
	f.open("A-large.in");
	int n;
	f >> n;
	for(int i=0; i<n; i++)
	{
		int ot=0,bt=0,op=1,bp=1;
		string player;
		int p;
		int cs;
		f >> cs;
		for(int j=0; j<cs; j++)
		{
			f >> player >> p;
			if(player == "O")
			{
				ot+= max(abs(op-p)+1, bt-ot+1);
				op=p;
			}
			else // Blue
			{
				bt+= max(abs(bp-p)+1, ot-bt+1);
				bp=p;
			}
		}
		cout << "Case #" << i+1 << ": " << max(ot, bt) << endl;
	}
	return 0;
}
