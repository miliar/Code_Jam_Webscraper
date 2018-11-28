#include <iostream>
#include <string>
using namespace std;

int n;
string s[50];
int ans;

bool isok(int row, int testrow)
{
	bool good=true;
	for( int i=testrow+1; i<n; i++ ) {
		if( s[row][i]=='1' ) {
			good=false;
			break;
		}
	}
	return good;
}

void process()
{
	ans=0;

	for( int i=0; i<n; i++ ) {

		int target = i;
		for( int j=i; j<n; j++ ) {
			if( isok(j,i) == true ) {
				target=j;
				break;
			}
		}

		ans += (target-i);
		for( int j=target; j>i; j-- ) {
			string t;
			t = s[j]; s[j]= s[j-1]; s[j-1]=t;
		}
		
	}
}

int main()
{
	freopen("A-large.in","rt", stdin);
	freopen("a.out","wt", stdout);
	int t;
	cin>>t;
	for( int i=0; i<t; i++ ) 
	{
		cin>>n;
		for( int j=0; j<n; j++ ) 
		{
			cin>>s[j];
		}
		cout<<"Case #"<<i+1<<": ";
		process();
		cout<<ans<<endl;

	}
	return 0;
}