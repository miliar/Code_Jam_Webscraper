#include <iostream>
#include <ctime>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int X[2000],Y[2000];
struct PP{
	int i;
	int r;
	PP(){}
	PP(int _i,int _r):i(_i),r(_r){}
};
vector<PP> v;
bool cmp(PP a, PP b){
	return a.r>b.r;
}
int main(){
	freopen("B-small-attempt5.in","r",stdin);
	freopen("B-small-attempt5.out","w",stdout);
	int cn;
	srand(time(0));
	cin>>cn;
	for (int cs=1;cs<=cn;cs++){
		int W,H;

		cin>>N>>W>>H;

		v.clear();
		for (int i=0;i<N;i++){
			int tmp;
			cin>>tmp;
			v.push_back(PP(i,tmp));
		}
		sort(v.begin(),v.end(),cmp);
		int cH=0,cW=v[0].r,ccH=v[0].r;
		X[v[0].i]=Y[v[0].i]=0;
		for (int i=1;i<N;i++){
			if (cW+v[i].r>W)
			{
				cH+=ccH;
				ccH=0;
				cW=-v[i].r;
			}
			int index=v[i].i;
			X[index]=cW+v[i].r;
			if (cH==0)Y[index]=0;
			else
			Y[index]=cH+v[i].r;
			//cout<<cW<<" "<<cH<<endl;

			cW+=2*v[i].r;
			ccH=max(ccH,v[i].r*2);
		}
		printf("Case #%d: ",cs);
		for (int j=0;j<N;j++)
			printf("%d %d ",X[j],Y[j]);
		printf("\n");
	}
	return 0;
}