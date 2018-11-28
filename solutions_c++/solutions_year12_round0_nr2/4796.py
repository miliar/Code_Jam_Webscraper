#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int dance(vector<int> score, int min, int max, int suc , bool s, bool p, int sum, int pp);

int main(void){
	int t,n,s,p;
	int googler;

	ofstream fw;
	fw.open("out.txt");
	cin >> t;
	vector<int> vysledok(3,0);

	for(int i=0;i<t;i++){
		cin >> n >> s >> p;
		for(int j=0;j<n;j++){
			cin >> googler;
			int res2=-1;
			res2 = -2;
			vector<int> score(1);
			for(int k=0;k<=10;k++){
				score[0] = k;				
				int x;
				x=dance(score, k, k, k, false, false, googler, p);
				if(x > res2) res2 = x;
			}

			if(res2 == -1) vysledok[0]++;
			if(res2 == 1) vysledok[1]++;
			if(res2 == 2) vysledok[2]++;
				
		}
		fw << "Case #" << i+1 << ": " << min(vysledok[0],s)+vysledok[1]+vysledok[2] << endl;
				
		vysledok[0]=0;
		vysledok[1]=0;
		vysledok[2]=0;
	}


	return 0;
}

int dance(vector<int> score, int min, int max, int suc , bool s, bool p, int sum, int pp){
	for(int i=0;i<=10;i++){
		if(abs(min-i) > 2 || abs(max-i) > 2) continue;
		if(score.size() == 1 && suc + i > sum) break;
		if(score.size() == 2){
			if((suc + i == sum) && (min >= pp || max >= pp || i >= pp)){
				score.push_back(i);
				int old_min = min;
				int old_max = max;
				if(min > i) min = i;
				if(max < i) max = i;
				if((min + 2) == max){
					p = true;
				}else{
					s = true;
				}
				max = old_max;
				min = old_min;
				score.pop_back();
			}
		}else{
			int old_min = min;
			int old_max = max;
			if(min > i) min = i;
			if(max < i) max = i;

			score.push_back(i);
			int ret;
			ret = dance(score, min, max, suc+i, s, p, sum, pp);
			if(ret == 1) s = true;
			if(ret == 2){
				s = true;
				p=true;
			}
			if(ret == -1) p = true;
			score.pop_back();
			max = old_max;
			min = old_min;
		}
		
	}
	if(!p && s) return 1;
	if(p && !s) return -1;
	if(p && s) return 2;
	return -2;
}
