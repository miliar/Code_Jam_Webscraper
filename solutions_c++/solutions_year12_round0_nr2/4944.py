#include <iostream>

using namespace std;
int t,n,s,p,z,il,limit, mlimit, tab[10000000],x;
int main()
{
	cin >> t;
	while(t--)
	{
		z++;
		cin >> n >> s >> p;
		limit=3*p-4;
		mlimit=3*p-2;
		for(int i=0; i<n; i++)
			cin >> tab[i];
			
		for(int i=0; i<n; i++)
		{
			if(tab[i]>=mlimit)
			{
				il++;
			}
			else
			{
				if(tab[i]>=limit && tab[i]<mlimit && s!=0 && limit>=0)
				{
					s--;
					il++;
				}
			}
		}
		cout << "Case #" << z <<": " << il << endl;
		il=0;
	}
}
