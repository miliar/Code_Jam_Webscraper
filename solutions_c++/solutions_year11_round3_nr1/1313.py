/*#include <iostream>

using namespace std;

string A[50];

int main()
{
    int n = 0;
    int a = 0;
    int b = 0;
    cin >> n;
    for(int i = 0; i < n; i++)
    {
        bool flag = true;
        cin >> a >> b;
        for(int j = 0; j < a; j++)
        {
            cin >> A[j];
        }
        for(int j = 0; j < a; j++)
        {
            for(int k = 0; k < b; k++)
            {
                if(A[j][k] == '#')
                {
                    if(j == a || k == b)
                    flag = false;
                    if(A[j][k] == '#' && A[j+1][k+1] == '#' && A[j+1][k] == '#' && A[j][k+1] == '#')
                }
            }
        }
    }
    return 0;
}
*/

#include <iostream>
#include <fstream>
using namespace std;

char input[50][50];

int main()
{
    istream cin("A-small-attempt0.in");
    ostream cout("output.txt");
	int T;
	cin >> T;
	for(int i=1;i<=T;i++)
	{
		int R,C;
		cin >> R >> C;
		for(int j=0;j<R;j++)
			for(int k=0;k<C;k++)
				cin >> input[j][k];
		bool flag = true;
		for(int j=0;flag&&j<R;j++)
			for(int k=0;flag&&k<C;k++)
			{
				if(input[j][k]!='#') continue;
				if(j+1<R && k+1<C && input[j+1][k]=='#' && input[j][k+1]=='#' && input[j+1][k+1]=='#')
				{
					input[j][k] = input[j+1][k+1] = '/';
					input[j+1][k] = input[j][k+1] = '\\';
				}
				else
					flag = false;
			}
		cout << "Case #" << i << ":" << endl;
		if(!flag) cout << "Impossible" << endl;
		else
		{
			for(int j=0;j<R;j++)
			{
				for(int k=0;k<C;k++)
				{
					cout << input[j][k];
				}
				cout << endl;
			}
		}
	}
}
