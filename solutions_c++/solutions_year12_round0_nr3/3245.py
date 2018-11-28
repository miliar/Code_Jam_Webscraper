#include<iostream>
#include<vector>
#include<map>
using namespace std;
typedef long long LL;
int main(){
	int T;
	cin>>T;
	int caseNum=1;
	while(T--){
		int A,B;
		cin>>A>>B;
		int ans = 0;
		map<pair<int,int>,bool> picked;
		for(int n=A;n<=B;n++){
			int shift = 1;
			int temp = n;
			int prod = 1;
			while(temp!=0){
				shift*=10;
				temp/=10;
			}
			while(shift != 1){
				shift/=10;
				prod*=10;
				int m = (n%shift)*prod + n/shift;
				//cout<<m<<" ";
				if(n<m && m<=B){
				       //cout<<n<<" "<<m<<endl;
				       if(!picked[pair<int,int>(n,m)]){
					       ans++;
					       picked[pair<int,int>(n,m)] = true;
				       }
				}
			}
		}
		cout<<"Case #"<<caseNum++<<": "<<ans<<endl;
	}
	return 0;
}
