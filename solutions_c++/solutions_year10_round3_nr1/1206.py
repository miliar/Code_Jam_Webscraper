#include<iostream>
#include<algorithm>
#define OK(r,c) (r>=0&&c>=0&&r<row&&c<col)
using namespace std;
struct Point{
	int x,y;
	Point(){}
	Point(int a,int b):x(a),y(b){}
};
struct Line{
	Point p1,p2;
}all[1010];
Point operator-(Point p1, Point p2){ 
    return Point(p1.x - p2.x, p1.y - p2.y); 
} 
int operator*(Point p1, Point p2) {
    return (p1.x * p2.y - p2.x * p1.y); 
} 
inline bool LEQ(int x, int y){ 
    return ( x==y || (x < y) ); 
} 
inline bool GEQ(int x, int y){ 
    return ( x==y || (x > y) ); 
}

bool LineSegIntersect(Line L1, Line L2){
    return ( GEQ( max(L1.p1.x, L1.p2.x), min(L2.p1.x, L2.p2.x) ) && 
        GEQ( max(L2.p1.x, L2.p2.x), min(L1.p1.x, L1.p2.x) ) && 
        GEQ( max(L1.p1.y, L1.p2.y), min(L2.p1.y, L2.p2.y) ) && 
        GEQ( max(L2.p1.y, L2.p2.y), min(L1.p1.y, L1.p2.y) ) && 
        LEQ( ((L2.p1 - L1.p1) * (L1.p2 - L1.p1)) * ((L2.p2 -  L1.p1) * (L1.p2 - L1.p1)), 0 ) && 
        LEQ( ((L1.p1 - L2.p1) * (L2.p2 - L2.p1)) * ((L1.p2 -  L2.p1) * (L2.p2 - L2.p1)), 0 ) );              
} 

int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,i,n,j,cas=1;
	scanf("%d",&T);
	while(T--){
		scanf("%d",&n);
		for(i=0;i<n;i++){
			scanf("%d%d",&all[i].p1.y,&all[i].p2.y);
			all[i].p1.x=0;
			all[i].p2.x=1;
		}
		int ans=0;
		for(i=0;i<n;i++)
			for(j=i+1;j<n;j++)
				if(LineSegIntersect(all[i],all[j]))
					ans++;
		printf("Case #%d: %d\n",cas++,ans);
	}
}
