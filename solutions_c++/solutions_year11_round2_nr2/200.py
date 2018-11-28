#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int C, D;
vector<int> p;

bool dasie(long long czas){
	long long byl = -1000123000123000123LL;
	for(int i = 0; i < p.size(); i++){
		if(p[i]+czas<byl+D)
			return false;
		else
			byl = max(byl+D, p[i]-czas);
	}
	return true;
}

int main(){
	int testy;
	scanf("%d", &testy);
	for(int t = 1; t <= testy; t++){
		p.clear();
		scanf("%d %d", &C, &D);
		D *= 2;
		int P, V;
		for(int i = 0; i < C; i++){
			scanf("%d %d", &P, &V);
			P *= 2;
			while(V--)
				p.push_back(P);
		}
		long long pocz = 0, kon = 1000123000123000123LL, srodek;
		while(kon-pocz>3){
			srodek = (pocz+kon)/2;
			if(dasie(srodek))
				kon = srodek;
			else
				pocz = srodek;
		}
		while(!dasie(pocz))
			pocz++;
		printf("Case #%d: %lld.%lld\n", t, pocz/2, (pocz%2)*5);
	}
	return 0;
}
