#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
bool shu[2000000];
vector<int> sushu;
void pre(){
	for(int i =2 ; i<2000000; i++)shu[i] = true;
	for(int i =2 ; i<2000000; i++){
		if(shu[i]){
			sushu.push_back(i);
			for(int j = 2*i; j < 2000000;j+=i)shu[j] = false;
		}
	}
}
void work(int x)
{
	long long ans =1;
	printf("Case #%d: ",x);
	int N;
	cin >> N;
	for(long long i = 0; i <sushu.size() && sushu[i] *sushu[i]<=N ; i++){
		for(long long j = sushu[i]* sushu[i]; j <=N; j*=sushu[i])ans++;
	}
	if(N != 1)cout << ans << endl;
	else cout << "0" << endl;
}
int main()
{
	int t;
	pre();
	scanf("%d",&t);
	for(int i = 1; i <= t; i++)work(i);
}
