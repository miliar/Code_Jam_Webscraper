#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long int64;

void fill(int x, int y, char c);

const int size = 102;
int hoogte, breedte;
int veld[size][size];

char out[size][size]; //antwoord
char richting[size][size]; //per veld in welke richting

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int n;
	
	cin >> n;
	
	for (int k=0; k<n; k++)
	{
		cin >> hoogte >> breedte;

		//inlezen + randen opvullen met 10K
		for (int i=0; i<=hoogte+1; i++)
		{
			veld[i][0]=10000;
			veld[i][breedte+1]=10000;
		}

		for (int i=0; i<=breedte+1; i++)
		{
			veld[0][i]=10000;
			veld[hoogte+1][i]=10000;
		}

		for (int h=1; h<=hoogte; h++)
		{
			for (int b=1; b<=breedte; b++)
			{
				cin >> veld[h][b];
			}
		}

		//-----------------------------

		for (int h=1; h<=hoogte; h++)
		{
			for (int b=1; b<=breedte; b++)
			{
				int cur=veld[h][b];

				char r='N';
				int max=cur-veld[h-1][b]; //noord
				
				if (cur-veld[h][b-1] > max) //west
				{
					max=cur-veld[h][b-1];
					r='W';
				}

				if (cur-veld[h][b+1] > max) //oost
				{
					max=cur-veld[h][b+1];
					r='O';
				}

				if (cur-veld[h+1][b] > max) //zuid
				{
					max=cur-veld[h+1][b];
					r='Z';
				}

				if (max > 0)
					richting[h][b]=r;
				else
					richting[h][b]='D'; //drain
			}
		}

		char c='A'; //vullen
		out[1][1]=c;

		for (int h=1; h<=hoogte; h++)
		{
			for (int b=1; b<=breedte; b++)
			{
				if (richting[h][b]=='D')
				{
					fill(h,b,c);
					c++;
				}
			}
		}

		//in 1 vector
		vector<char> ans(breedte*hoogte);
		int count=0;

		for (int h=1; h<=hoogte; h++)
		{
			for (int b=1; b<=breedte; b++)
			{
				ans[count]=out[h][b];
				count++;
			}
		}

		//sorteren
		char cur='a';
		for (int i=0; i<count; i++)
		{
			char change=ans[i];
			if(change<'a')
			{
				for (int j=0; j<count; j++)
				{
					if (ans[j]==change)
						ans[j]=cur;
				}
				cur++;
			}
		}


		//printen
		cout << "Case #" << k+1 << ":" << endl;
		for (int i=1; i<=count; i++)
		{
			cout << ans[i-1] << " ";

			if (i%breedte==0)
				cout << endl;
		}
	}
}

void fill(int x, int y, char c)
{
	out[x][y]=c;

	if (richting[x-1][y] == 'Z') //noord
		fill(x-1,y,c);

	if (richting[x][y-1] == 'O') //west
		fill(x,y-1,c);

	if (richting[x][y+1] == 'W') //oost
		fill(x,y+1,c);

	if (richting[x+1][y] == 'N') //zuid
		fill(x+1,y,c);

}