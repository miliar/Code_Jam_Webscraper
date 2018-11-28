#include<iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>
using namespace std;

int n, p, k, l;
ifstream fin("A-large.in");
ofstream fout("C.out");
struct Letter
{
	int index, freq;
};
Letter text[1000];

bool f(Letter a, Letter b)
{
	return a.freq > b.freq;
}

int main()
{
	fin>>n;
	int i = 0, j;
	double ans;
	while(i < n){
		i++;
		fin>>p>>k>>l;
		for(j = 0; j < l; ++ j){
			text[j].index = j;
			fin>>text[j].freq;
		}
		sort(text, text+l, f);

		ans = 0;
//		cout<<"--------------------------"<<endl;
		for(j = 0; j < l; ++ j){
//			cout<<text[j].freq<<endl;
			if(text[j].freq == 0) break;
			ans += text[j].freq*(j/k+1);
		}
		fout<<"Case #"<<i<<": ";
		fout<<fixed<<setprecision(0)<<ans<<endl;
	}
	return 0;
}
