#include <stdio.h>
#include <algorithm>

using namespace std;

struct Ladder{
	int start;
	int end;
	int speed;
	bool operator<(const Ladder &o)const{
		return start<o.start;
	}
};

int l,w,r,n;
double allTime;
double t;
Ladder ladders[1005];

bool sortbySpeed(Ladder a,Ladder b){
    return a.speed<b.speed;
}

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j;
    int xx,zz;
    scanf("%d",&zz);
    for(xx=1;xx<=zz;xx++){
        allTime=0;
    	printf("Case #%d: ",xx);
    	scanf("%d%d%d%lf%d",&l,&w,&r,&t,&n);
    	for(i=1;i<=n;i++){
            scanf("%d%d%d",&ladders[i].start,&ladders[i].end,&ladders[i].speed);
    	}
    	sort(ladders+1,ladders+n+1);
    	int now=0;
    	double len,time;
    	int walkTime=0;
    	for(i=1;i<=n;i++){
    		if(now<ladders[i].start){
    			walkTime+=ladders[i].start-now;
    		}
    		now=ladders[i].end;
    	}
    	if(now<l){
    		walkTime+=l-now;
    	}
    	now=0;
    	len=(double)walkTime;
        if(t>0){
            time=(double)len/r;
            if(t>=time){
                t-=time;
                allTime+=time;
            }else{
                allTime+=t;
                len-=r*t;
                allTime+=len/w;
                t=0;
            }
        }else{
            allTime+=len/w;
        }
        sort(ladders+1,ladders+n+1,sortbySpeed);

    	for(i=1;i<=n;i++){
    		len=ladders[i].end-ladders[i].start;
            if(t>0){
                time=(double)len/(r+ladders[i].speed);
                if(t>=time){
                    t-=time;
                    allTime+=time;
                }else{
                    allTime+=t;
                    len-=(r+ladders[i].speed)*t;
                    allTime+=len/(w+ladders[i].speed);
                    t=0;
                }
            }else{
                allTime+=len/(w+ladders[i].speed);
            }
    	}
    	printf("%.20lf\n",allTime);
    }
	return 0;
}
/*
3
10 1 4 1 2
4 6 1
6 9 2
12 1 2 4 1
6 12 1
20 1 3 20 5
0 4 5
4 8 4
8 12 3
12 16 2
16 20 1
*/
