//CODEJAM C

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	//vars
	ifstream cin ("C-large.in");
	ofstream cout ("C-large.out");
	int n,l,a,b,x;
	char s[600];
	char k[20]={'w','e','l','c','o','m','e',' ','t','o',' ','c','o','d','e',' ','j','a','m','?'};
	static int dyn[600][20];
	//testcase loop
	cin >> n;
	cin.ignore();
		for (x=1; x<=n; x++)
		{
			//input
			cin.getline(s,600,'\n');
			l=strlen(s);
			//dynamic
			memset(dyn,0,sizeof(dyn));
			dyn[0][0]=1;
				for (a=0; a<l; a++)
					for (b=0; b<20; b++)
						if (dyn[a][b])
						{
							dyn[a+1][b]=(dyn[a+1][b]+dyn[a][b])%10000;
								if (s[a]==k[b])
									dyn[a+1][b+1]=(dyn[a+1][b+1]+dyn[a][b])%10000;
						}
			//output
			cout << "Case #" << x << ": ";
				if (dyn[l][19]<10)
					cout << 0;
				if (dyn[l][19]<100)
					cout << 0;
				if (dyn[l][19]<1000)
					cout << 0;
			cout << dyn[l][19] << endl;
		}
	return(0);
}