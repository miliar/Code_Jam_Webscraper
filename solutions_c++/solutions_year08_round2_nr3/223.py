#include <iostream>
#include <vector>
#include <map>
using namespace std;

typedef long long LL;
typedef long double LD;

typedef vector<int> VI;

map<int,vector<int> > mm;

map<int,int> build(int K){
	vector<int> v(K);
	
	for(int i=0;i<K;i++)
		v[i]=i+1;
	
	int N=v.size();

	map<int,int> ans;

	int nexK=1;
	int p=0;
	
	fprintf(stderr, "go for %d\n",K);
	
	while(N){
		int np=nexK+p-1;
		np%=N;
		ans[ v[np] ]=nexK;

		//fprintf(stderr, "%d\n",v[np]);

		v.erase(v.begin()+np);
		p=np;
		nexK++;
		N--;
	}
	fprintf(stderr, "done for %d\n",K);
	return ans;
}



int main()
{
	int ttt;
	cin >> ttt;
	for(int cutest=1;cutest<=ttt;cutest++){

		int K,n;
		cin >> K >> n;

		printf("Case #%d: ",cutest);

		map<int,int> v=build(K);

		for(int i=0;i<n;i++){
			int dx;
			cin >> dx;
			printf("%d",v[dx]);
			if(i!=n-1)
				printf(" ");
		}
		printf("\n");
	}

}
