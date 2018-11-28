#include<ctime>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<queue>
#include<stack>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<locale>
using namespace std;
#define all(x) (x).begin(),(x).end()
#define sz(a) (int((a).size()))
typedef istringstream iss; typedef ostringstream oss; typedef long long lli;
const double TOLL=1e-9;

char arr[110][110]; int r,c;

int main()
{
    int t; cin>>t; int cn=0;
    while(t--)
    {
	cin>>r>>c;
	for(int i=0;i<r;i++) scanf("%s",arr[i]);
	for(int i=0;i<r-1;i++) for(int j=0;j<c-1;j++) if(arr[i][j]=='#' && arr[i][j+1]=='#' && arr[i+1][j]=='#' && arr[i+1][j+1]=='#')
	{
	    arr[i][j]='/' ; arr[i][j+1]='\\' ; arr[i+1][j]='\\' ; arr[i+1][j+1]='/';
	}
	bool ok=true;
	for(int i=0;i<r;i++) for(int j=0;j<c;j++) if(arr[i][j]=='#') ok=false;
	printf("Case #%d:\n",++cn);
	if(!ok) cout<<"Impossible"<<endl;
	for(int i=0;i<r && ok;i++)
	{
	    for(int j=0;j<c;j++) cout<<arr[i][j];
	    cout<<endl;
	}

    }

}
