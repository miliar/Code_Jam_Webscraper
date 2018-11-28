#include <fstream>

using namespace std;
ifstream fin("C-large.in");
ofstream fout("output.txt");
#define cin fin
#define cout fout

int a[100000];

int main()
{
	int n;
	cin>>n;
	for(int x=1;x<=n;x++){
		int m,mi=10000000,ans=0,sum=0;
		cin>>m;
		for(int i=0;i<m;i++){
			cin>>a[i];mi=min(mi,a[i]);ans^=a[i];sum+=a[i];
		}
		if(ans){
			cout<<"Case #"<<x<<": NO"<<endl;
		}else{
			cout<<"Case #"<<x<<": "<<sum-mi<<endl;
		}
	}
}