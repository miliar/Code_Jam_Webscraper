#include <string>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n;
	cin >>n;
	for (int i=0; i<n; ++i){
		cout <<"Case #" <<i+1 <<": ";
		int a,b;
		cin >>a >>b;
		int count=0;
		for (int j=a; j<=b; ++j){
			int t=10,c=1;
			while (j>=t)
			{
				t*=10;
				++c;
			}
			int cur=j;
			set<int> s;
			for (int k=1; k<c; ++k){
				int ost=cur%10;
				cur=(cur/10)+ost*(t/10);
				if (cur>=t/10 && cur<j && cur>=a && cur<=b && s.find(cur)==s.end()){
					++count;
					s.insert(cur);
				}
			}
		}
		cout <<count <<endl;
	}
	return 0;
}