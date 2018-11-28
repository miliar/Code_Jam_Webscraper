#include <fstream>
#include <iostream>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int a[100000];

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		int ans,m;
		cin>>m;ans=m;
		for(int i=0;i<m;i++){
			cin>>a[i];if(a[i]==(i+1)) ans--;
		}
		cout<<"Case #"<<x<<": "<<ans<<".000000"<<endl;
	}
}