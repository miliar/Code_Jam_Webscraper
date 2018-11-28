#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
#include <string>
using namespace std;

int main (){
	int i,j,t=0,T,N,S,p,res=0,rem,temp1,SI; // SI = Starting Index for performing surprises on total score
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	cin >> T;
	while (t<T){
		res=0;
		cin >> N;
		cin >> S;
		cin >> p;
		vector <int> temp;
		for (i=0;i<N;i++){
			cin >> temp1;
			temp.push_back(temp1);
		}
		if (S==0) {SI=0; goto proceed;}

		sort(temp.begin(), temp.end());
		
		for (i=0;i<N;i++){
			rem=temp[i]%3;
			switch (rem){
			case 0: if ((temp[i]/3+1)>=p && temp[i]>=2) {SI=i;goto proceed;} break;
			case 1: if ((temp[i]/3+1)>=p && temp[i]>=2) {SI=i;goto proceed;} break;
			case 2: if ((temp[i]/3+2)>=p && temp[i]>=2) {SI=i;goto proceed;} break;
			}
		}
		SI=N;
proceed:

		if ((SI+S)>N) j=N; else j=SI+S;

		for (i=SI;i<j;i++){
			rem=temp[i]%3;
			switch (rem){
			case 0: if ((temp[i]/3+1)>=p) res++;break;
			case 1: if ((temp[i]/3+1)>=p) res++;break;
			case 2: if ((temp[i]/3+2)>=p) res++;break;
			}
			if (temp[i]==0&&p==0) res++;
		}
		for (i=0;i<SI;i++){
			rem=temp[i]%3;
			switch (rem){
			case 0: if ((temp[i]/3)>=p && temp[i]>0) res++;break;
			case 1: if ((temp[i]/3+1)>=p && temp[i]>0) res++;break;
			case 2: if ((temp[i]/3+1)>=p && temp[i]>0) res++;break;
			}
			if (temp[i]==0&&p==0) res++;
		}

		for (i=j;i<N;i++){
			rem=temp[i]%3;
			switch (rem){
			case 0: if ((temp[i]/3)>=p && temp[i]>0) res++;break;
			case 1: if ((temp[i]/3+1)>=p && temp[i]>0) res++;break;
			case 2: if ((temp[i]/3+1)>=p && temp[i]>0) res++;break;
			}
			if (temp[i]==0&&p==0) res++;
		}
		cout << "Case #" << ++t << ": " << res << endl;
	}
	 return 0;
}
