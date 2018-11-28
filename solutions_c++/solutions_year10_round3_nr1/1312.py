#include <vector>
#include <stdio.h>
 



using namespace std;




class point{
public:
	int x;
	int y;
};



bool ccw(point A,point B, point C){
	return ((C.y-A.y)*(B.x-A.x)) > ((B.y-A.y)*(C.x-A.x));
}


bool intersec(point A, point B, point C, point D){
	//printf("Ay:%d By:%d Cy:%d Dy:%d SI:%d\n", A.y,B.y,C.y,D.y, ((ccw(A,C,D) != ccw(B,C,D)) && (ccw(A,B,C) != ccw(A,B,D))));
	return ((ccw(A,C,D) != ccw(B,C,D)) && (ccw(A,B,C) != ccw(A,B,D)));
}



int main(){

	freopen("A-small.in","r",stdin);
	freopen("A-small.out","w",stdout);
	
	vector<point> A;
	vector<point> B;
	int cases,a,b,points,cont;
	scanf("%d\n",&cases);

	point p,p2;
	for(int i=0;i<cases;i++){
		scanf("%d\n",&points);
		for(int j=0;j<points;j++){

			scanf("%d %d\n",&a,&b);
			p.x=0;
			p.y=a;
			p2.x=10;
			p2.y=b;

			A.push_back(p);
			B.push_back(p2);
			
		}

		cont=0;
		for(int z=0;z<A.size()-1;++z){


			for(int w=z+1;w<A.size();++w){

				if(intersec(A[z],B[z],A[w],B[w]))cont++;

			}

		}
		A.clear();
		B.clear();
		printf("Case #%d: %d\n",i+1,cont);
	


	}

	return 0;

}
