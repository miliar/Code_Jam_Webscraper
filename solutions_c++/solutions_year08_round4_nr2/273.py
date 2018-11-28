
#include <iostream>
#include <vector>
typedef long long LL;
using namespace std;

void calc(LL w, LL h, LL A, vector<LL> &ans){
	/*
	for(LL t=1; t<=w; t++){
		if(A%t == 0 && A/t <= h){
			ans.push_back(0LL);
			ans.push_back(0LL);
			ans.push_back(t);
			ans.push_back(0LL);
			ans.push_back(0LL);
			ans.push_back(A/t);
			return;
		}
	}
	*/
	for(int x=0; x<=w; x++)
		for(int y=0; y<=h; y++)
			for(int x2=0; x2<=w; x2++)
				for(int y2=0; y2<=h; y2++)
					if(2*x2*y2 - x*y - x2*(y2-y) - y2*(x2-x) == A){
						ans.push_back(0LL);
						ans.push_back(y);
						ans.push_back(x);
						ans.push_back(0LL);
						ans.push_back(x2);
						ans.push_back(y2);
						return;
					}

}

int main(void){
	int cases;
	cin >> cases;
	for(int case_no=1; case_no<=cases; case_no++){
		LL w, h, A;
		cin >> w >> h >> A;
		vector<LL> ans;
		calc(w,h,A, ans);
		cout << "Case #"<<case_no<<":";
		if(ans.empty()){
			cout << " IMPOSSIBLE";
		}else{
			for(int i=0; i<6; i++)
				cout << " " << ans[i];
		}
		cout << endl;
	}
	return 0;
}
