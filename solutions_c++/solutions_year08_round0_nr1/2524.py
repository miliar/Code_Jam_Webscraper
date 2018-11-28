#include <iostream>
#include <string>
#include <fstream>


using namespace std;

ofstream fout("Aout.txt");
#define cout fout

int main()
{
	int n,s,q, sw,cnt;
	string qu[1005],se[105];
	bool vis[105];
	cin>>n;
	for(int cse=1; cse<=n; cse++)
	{
		cin>>s; cin.ignore();
		for(int i=0; i<s; i++)
			getline(cin,se[i]);
		cin>>q; cin.ignore();
		for(int i=0; i<q; i++)
			getline(cin,qu[i]);

		sw=0;cnt=0;
		memset(vis, 0, sizeof vis);
		for(int i=0; i<q; i++)
		{
			for(int j=0; j<s; j++)
				if(qu[i]==se[j])
				{
					if(!vis[j])
					{
						vis[j]=true, cnt++;
						if(cnt >= s)
						{
							sw++;
							cnt = 1;
							memset(vis, 0, sizeof vis);
							vis[j] = true;
						}
						break;
					}
				}
		}
		cout<<"Case #"<<cse<<": "<<sw<<endl;
	}

	return 0;
}
