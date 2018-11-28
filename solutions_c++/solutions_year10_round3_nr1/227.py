#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <stdlib.h>
#include <ctime>
#include <fstream>

using namespace std;

int n;
int a[1001],b[1001];
int main() {
	//freopen("f:\\a-small.in","r",stdin); freopen("f:\\a-small.out","w",stdout);
	freopen("f:\\a-large.in","r",stdin); freopen("f:\\a-large.out","w",stdout);
	int t,ans;
	cin>>t;
	for(int j=1;j<=t;j++){
		cout<<"Case #"<<j<<": ";
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>a[i]>>b[i];
		}
		ans =0;
		for(int i=0;i<n-1;i++){
			for(int k=i+1;k<n;k++){
				if(a[i]>a[k] && b[i]<b[k]) ans++;
				if(a[i]<a[k] && b[i]>b[k]) ans++;

			}
		}
		cout<<ans<<endl;
	}
}