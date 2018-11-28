#include<vector>
#include<iostream>
using namespace std;
int mc[3][3];
struct mcr{
	int xr, yr, cnt;
};
int main(){
	int N;
	cin>>N;
	for(int test=1; test<=N; test++){
		long long X,Y,n,A,B,C,D,x0,y0,M;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		vector<long long> x,y;
		x.push_back(x0);
		y.push_back(y0);
		X=x0;Y=y0;
		memset(mc, 0, sizeof(mc));
		mc[x.back()%3][y.back()%3]++;
		for(int i=1; i<n; i++){
			x.push_back(X=(A*X+B)%M);
			y.push_back(Y=(C*Y+D)%M);
			mc[x.back()%3][y.back()%3]++;
		}
		vector<mcr> V;
		for(int i=0; i<3; i++)
			for(int j=0; j<3; j++)
				if(mc[i][j]!=0)
					V.push_back((mcr){i,j,mc[i][j]});

		long long sum=0;
		for(int i=0; i<V.size(); i++)
			for(int j=i; j<V.size(); j++)
				for(int z=j; z<V.size(); z++)
					if((V[i].xr+V[j].xr+V[z].xr)%3==0 && (V[i].yr+V[j].yr+V[z].yr)%3==0){
						if(i==j && j==z)
							sum+=((long long)V[i].cnt*(V[i].cnt-1)*(V[i].cnt-2)/6);

#define numUn(a,b,c)    if(a==b && c!=a) \
							sum+=((long long)V[a].cnt*(V[a].cnt-1)/2)*V[c].cnt;
						numUn(i,j,z);
						numUn(i,z,j);
						numUn(j,z,i);

						if(i!=j && z!=i && z!=j)
							sum+=(long long)V[i].cnt*V[j].cnt*V[z].cnt;
					}
		cout<<"Case #"<<test;
		cout<<": "<<sum<<'\n';
	}
	return 0;
}
