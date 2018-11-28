#include <iostream>
#include <fstream>

using namespace std;

int main()
{

	//freopen("data.txt", "r", stdin);
	//freopen("data.txt", "r", stdin);
	freopen("A-small-attempt4.in.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, k, t;
	int bulb[31];
	int flag = 0;

	//ifstream fin( "A-small-attempt1.in.txt" );
	//ofstream fout( "output",ios::trunc );

	scanf("%d",&t);
	//cin >> t;
	int i = 1;
	while(i <= t)
	{
		scanf("%d%d",&n,&k);
		//cin >> n >> k;
		//bulb = new int[n];
		for(int j = 0; j<n;j++)
		{
			bulb[j] = 1;
		}
		for(int z = 0; z<k;z++)
		{
			int r = 0;
			int temp = bulb[r];
			if(bulb[r] == 0) bulb[r] = 1;
			else if(bulb[r] == 1) bulb[r] = 0;
			while(temp == 0 && r < n)
			{
				r++;
				temp = bulb[r];
				if(bulb[r] == 0) bulb[r] = 1;
		    	else if(bulb[r] == 1) bulb[r] = 0;
			}
		}
		flag = 1;//open
		for(int x = 0; x < n; x++)
		{
			if(bulb[x] == 1)
			{
				flag = 0;
				break;
			}
		}
		if(flag == 0)
			printf("Case #%d: OFF\n",i);
			//cout << "Case #" << i << ": OFF" << endl;
		else if(flag == 1)
			printf("Case #%d: ON\n",i);
			//cout << "Case #" << i << ": ON" << endl;
		i++;
	//	delete[] bulb;
	}

	//fin.close();
	//fout.close();
	return 0;

}