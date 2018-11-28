#include <iostream>
#include<fstream>
using namespace std;

int main()
{
	ofstream fout("ans1.txt");
	int testnum;
	cin>>testnum;
	for(int i=0;i<testnum;i++)
	{
		int N,S,P,t;
		int ans=0;
		cin>>N>>S>>P;
		while(N>0)
		{
			cin>>t;
			int u=t/3;
			int v=t%3;
			//cout<<u<<"    "<<P-u<<" "<<v<<endl;
			if(u>=P) ans++;
			else if((P-u)==1&&v==2) ans++;
			else if((P-u)==1&&v==1) ans++;
			else if((P-u)==2&&v==2&&S>0)
			{
				ans++;
				S--;
			}
			/*else if((P-u)==2&&v==1&&S>0)
			{
				ans++;
				S--;
			}*/
			else if((P-u)==1&&v==0&&S>0&&u>0)
			{
				ans++;
				S--;
			}
			N--;
		}
		fout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
}