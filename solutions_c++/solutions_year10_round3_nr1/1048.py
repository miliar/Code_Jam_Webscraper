#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int SIZE = 1100;
class Point{
public:
	int ind,pos;
	Point(int i=0,int p=0):ind(i),pos(p){
	}
	bool operator < (const Point& oth)const{
		return ind<oth.ind;
	}
};
Point dat[SIZE];
int n;
void init();
long long work();
int main(){
	freopen("dat.in","r",stdin);
	freopen("dat.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	for (int i=0;i<cas;i++){
		init();
		long long  ans = work();
		printf("Case #%d:",i+1);
		cout<<" "<<ans<<endl;
	}
	return 0;
}
void init(){
	scanf("%d",&n);
	for (int i=0;i<n;i++){
		int ind,pos;
		scanf("%d%d",&ind,&pos);
		dat[i]=Point(ind,pos);
	}
	sort(dat,dat+n);
}
long long  work(){
	long long  sum=0;
	for (int i=0;i<n;i++){
		for (int j=0;j<i;j++){
			if (dat[j].pos>dat[i].pos){
				sum++;
			}
		}
	}
	return sum;
}