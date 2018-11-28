#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

#define eps 1e-9

#define sq(x) ((x)*(x))
#define PI 2.0*acos(0)

struct P { double x, y; P() {}; P( double q, double w ) : x( q ), y( w ) {} };

double findOther(double x, double r){
	return sqrt( sq(r) - sq(x) ); 
}

double dist(double x1, double y1, double x2, double y2){
	return sqrt( sq(x2-x1) + sq(y2-y1) );
}

double dist2( P p, P q )
{
    return sqrt( ( p.x - q.x ) * ( p.x - q.x ) + ( p.y - q.y ) * ( p.y - q.y ) );
}

bool in(double x, double y, double r){
	double d = dist(0, 0, x, y);
	//cout<<x<<" "<<y<<" "<<d<<" "<<r<<endl;
	if( d > r )return false;
	else return true;
}

double polygonArea(vector<P> &v){
	double ret = 0.;
	int len = v.size();



	for(int i = 0; i < len ; ++i){
		ret += (v[i].x * v[(i+1)%len].y) - (v[i].y * v[(i+1)%len].x);
	}
	ret = fabs(ret)/2.;

	return ret;
}

double chordArea(double len, double r){
	double ret;

	//cout<<len<< " == "<<r<<endl;
	double perp = sqrt( sq(r) - sq(len/2.) );
	ret = perp*len/2.;

	double angle = acos(perp/r)*2.;
	double cArea = ( angle / (PI * 2.0) ) * PI*r*r;
	ret = cArea - ret;
	//cout<<cArea<<" - "<<ret<<endl;
	return ret;
}

double Area(double r, double x, double y, double a){
	bool BottomLeft, BottomRight, TopRight, TopLeft;
	
	BottomLeft	= in(x,		y,		r);
	BottomRight = in(x+a,	y,		r);
	TopRight	= in(x+a,	y+a,	r);
	TopLeft		= in(x,		y+a,	r);

	//cout<<"----- "<<x<<" "<<y<<" "<<r<<" "<<a<<endl;
	//cout<<BottomLeft<<" "<<BottomRight<<" "<<TopLeft<<" "<<TopRight<<endl;

	if(BottomLeft == false)return 0.;
	if(TopRight == true) return a*a;

	double res = 0.;
	if(TopLeft && BottomRight){
		vector<P> v;
		v.clear();
		v.push_back(P(x, y+a)); //top left
		v.push_back(P(x,y)); //bottom left
		v.push_back(P(x+a, y)); //bottom right
		
		P A(x+a, findOther(x+a, r));
		P B(findOther(y+a, r), y+a);
		
		//cout<<"Points"<<endl;
		//cout<<A.x<<" "<<A.y<<endl;
		//cout<<B.x<<" "<<B.y<<endl;

		v.push_back(A);
		v.push_back(B);

		res += polygonArea(v);
		res += chordArea(dist2(A,B), r);
	}
	else if(TopLeft){
		vector<P> v;
		v.clear();
		v.push_back(P(x,y+a)); //top left
		v.push_back(P(x,y)); //bottom left
		
		P A(findOther(y, r), y);
		P B(findOther(y+a, r), y+a);
		
		v.push_back(A);
		v.push_back(B);

		res += polygonArea(v);
		res += chordArea(dist2(A,B), r);
	}
	else if(BottomRight){
		vector<P> v;
		v.clear();
		v.push_back(P(x,y)); //bottom left
		v.push_back(P(x+a, y)); //bottom right

		P A(x+a, findOther(x+a, r));
		P B(x, findOther(x, r));
		
		v.push_back(A);
		v.push_back(B);

		res += polygonArea(v);
		
		res +=chordArea(dist2(A,B), r);
	}
	else{
		vector<P> v;
		v.clear();
		v.push_back(P(x,y)); //bottom left

		P A(x, findOther(x, r));
		P B(findOther(y, r), y);

		v.push_back(A);
		v.push_back(B);
		
		res += polygonArea(v);
		
		//cout<<"="<<res<<endl;
		res += chordArea(dist2(A,B), r);
	}
	
	return res;
}

double solve(){
	double f, R, t, r, g;
	scanf("%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
	double ret=0;
	if( eps >= g - f*2 )return 1.;

	double totalArea = PI * R * R;
	double IR = R - t - f;

	double x = r + f;
	double y = r + f;

	double side = g - f*2.0;
	double area = 0.;

	double width = (r+f)*2.;
	double d = side + width;
	
	int i, j;

	for(i=0;i<=500;++i){
		for(j=0;j<=500;++j){
			//if(i==7 && j==5){
				//printf("%d %d %lf %lf %lf %lf %lf\n",i,j, x+d*i, y+d*j, side, IR, Area( IR, x+(d)*i, y+(d)*j, side ));
				//return area;
				area += Area( IR, x+(d)*i, y+(d)*j, side );
			//}
		}
	}

	//cout<<area<<" "<<totalArea<<endl;
	return ret = (totalArea - area*4.)/totalArea;
}

int main (void){
	int N;
	freopen("C-large.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&N);
	
	for(int t=1; t<=N; ++t){
		printf("Case #%d: %.6lf\n", t,  solve());
	}

	return 0;
}