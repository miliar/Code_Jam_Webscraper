#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solve(){
	int N, S, p, tmp, ok=0;
	vector < int > scores;
	scores.reserve(150);
	cin >> N >> S >> p;
	for (int k=0;k<N;++k){
		cin >> tmp;
		scores.push_back(tmp);
	}
	if (p==0) return N;
	if (p==1) {
		tmp=0;
		for (int k=0;k<scores.size();++k)
			if (scores[k]!=0) tmp++;
		return tmp;
	}
	for (int k=0;k<scores.size();++k){
		if ( p+(p-1)+(p-1)<=scores[k])
			ok++;	
		else if (p+(p-2)+(p-2)<=scores[k] && S>0){
			ok++;
			S--;
		}
	
	}
	return ok;
}

int main(void){
	int n;
	cin >> n;
	for (int k=1;k<=n;++k){
		cout << "Case #"<<k<<": "<<solve()<<endl;
	}
	return 0;

}