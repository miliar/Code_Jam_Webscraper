#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <stack>
#include <cmath>
#include <sstream>
using namespace std;

int main()
{
	freopen("1.in","r",stdin);
	//freopen("large.in","r",stdin);
	freopen("1.out","w",stdout);

	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		queue<int> blue,orange;

		int n,stando=1,standb=1;
		cin>>n;
		vector<pair<char,bool> > arr(n);
		for(int j=0;j<n;j++){
			char c;
			int x;
			cin>>c;
			cin>>x;
			if(c=='B'){
				blue.push(x);
				arr[j]=(make_pair('B',false));
			}
			else if(c=='O'){
				orange.push(x);
				arr[j]=(make_pair('O',false));
			}
		}
		int j=1,k=0,sz=orange.size();


		for(;;j++){
			if(blue.empty() && orange.empty())break;
			bool f=false;
			if(!blue.empty() && blue.front()==standb ){
				if(arr[k].first=='B'){
					k++;
					blue.pop();
					f=true;
				}
			}
			else if(blue.front()>standb ){
				standb++;
			}
			else if(blue.front()<standb ){
				standb--;
			}

			if(!orange.empty() && (orange.front()==stando) && f==false ){
				if(arr[k].first=='O' ){
					k++;
					orange.pop();
				}
			}
			else if(orange.front()>stando ){
				stando++;
			}
			else if(orange.front()<stando ){
				stando--;
			}
		}
		cout<<"Case #"<<i<<": "<<j-1<<endl;
	}

	return 0;
}
