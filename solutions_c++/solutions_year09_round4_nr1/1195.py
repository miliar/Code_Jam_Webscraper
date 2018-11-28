#include <iostream>
#include <algorithm>
using namespace std;

int N;
int cnt[10], p[10], num[10], kk;

int getNum(string str, int idx){
	int tmp = 0;
	int res = 0;
	for(int i = 0; i < str.length(); i++){
		if(str[i] == '1') ++tmp;
		res = res*2+(str[i]-'0');
	}
	num[idx] = res;
	return tmp;
}



int isSatisfy(int pp[], int num2[]){
	for(int i = 0; i < N; i++){
		//cout << ((1<<(N-i-1))-1) << endl;
		if(( num2[i]& ((1<<(N-i-1))-1)) ) return 0;
	}
	return 1;
}

int getAns(){
	int pp[10], num2[10];
	for(int i = 0; i < N; i++){
		pp[i] = cnt[p[i]];
		num2[i] = num[p[i]];
	}
	//cout << "num2= ";
	//for(int i = 0; i < N; i++) cout << num2[i] << " "; cout << endl;
	if(!isSatisfy(pp,num2)) return 1000000;
	//cout << "yes" << endl;
	//cout << "the " << kk++ << ": ";
	//for(int i = 0; i < N; i++)
	//	cout << pp[i] << " "; cout << endl;
	int ans = 0;
	int i, j, k;
	int now[10];
	for(i = 0; i < N; i++) now[i] = num[i];
	for(i = 0; i < N; i++){ //p
		//cout << "cnt= ";
		//for(int s = 0; s < N; s++) cout << cnt[s] << " "; cout << endl;
		//for(int s = 0; s < N; s++) cout << pp[s] << " "; cout << endl;
		//cout << "ans= " << ans << endl;
		for(j = i; j < N; j++)
			if(now[j] == num2[i]) break;
		if(j == i) continue;
		for(k = j-1; k >= i; k--)
			{ now[k+1] = now[k]; ++ans; }
		now[k] = num2[i];
	}
	return ans;
}

int min(int a, int b) {return a>b?b:a;}

int main()
{
	int KASE;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out.txt", "w", stdout);
	string str;
	cin >> KASE;
	for(int kase = 1; kase <= KASE; kase++){
		cin >> N;
		for(int j = 0; j < N; j++){
			cin >> str;
			cnt[j] = getNum(str,j);
		}
		//cout << "num= ";
		//for(int j = 0; j < N; j++) cout << num[j] << " ";cout << endl;
		for(int i = 0; i < N; i++) p[i] = i;
		int res = 1000000;
		kk = 0;
		do{
			res = min( getAns(), res);
		}while(next_permutation(p,p+N));
		cout << "Case #" << kase << ": " << res << endl;
	}
	return 0;
}
