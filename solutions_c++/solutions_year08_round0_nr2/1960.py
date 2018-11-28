#include <iostream>

using namespace std;

pair<int, int> TA[100], TB[100];
int MA[24*60], MB[24*60];

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int n;
	cin>>n;
	for (int test=0; test<n; ++test){
		int t, na, nb;
		cin>>t>>na>>nb;
		for (int i=0; i<na; ++i){
			int hh, mm;
			scanf("%d:%d ", &hh, &mm);
			TA[i].first = hh*60 + mm;
			scanf("%d:%d", &hh, &mm);
			TA[i].second = hh*60 + mm + t;
		}
		for (int i=0; i<nb; ++i){
			int hh, mm;
			scanf("%d:%d ", &hh, &mm);
			TB[i].first = hh*60 + mm;
			scanf("%d:%d ", &hh, &mm);
			TB[i].second = hh*60 + mm + t;
		}
		
		/*for (int i=0; i<na; ++i)
			cout<<TA[i].first<<" "<<TA[i].second<<endl;

		for (int i=0; i<nb; ++i)
			cout<<TB[i].first<<" "<<TB[i].second<<endl;
		cout<<endl;*/

		for (int i=0; i<24*60; ++i)
			MA[i]=MB[i]=0;

		for (int i=0; i<na; ++i){
			MA[TA[i].first]--;
			MB[TA[i].second]++;
		}
		for (int i=0; i<nb; ++i){
			MB[TB[i].first]--;
			MA[TB[i].second]++;
		}
		int resA=0, resB=0, sumA=0, sumB=0;
		for (int i=0; i<24*60; ++i){
			sumA+=MA[i];
			sumB+=MB[i];
			resA = min(resA, sumA);
			resB = min(resB, sumB);
		}
		resA = -resA;
		resB = -resB;
		cout<<"Case #"<<test+1<<": "<<resA<<" "<<resB;
		if (test!=n-1)
			cout<<endl;
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}