#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cmath>

using namespace std;

int cases;

long double ballRadius,outerRadius,innerRadius,thickness,g,chordThick;
const long double PI=3.14159265359,err=1e-7;

long double two=2;
long double half=0.5;
long double one=1;
long double zero=0;
long double sqr(long double x) {return x*x;}
long double add;

bool inCircle(long double x,long double y) {return (sqr(x)+sqr(y)<=sqr(innerRadius));}

long double nInt(long double lowerLimit,long double intStart,long double intEnd)  {
	long double ca=innerRadius-ballRadius;
	return sqr(ca)*half*(asin(intEnd/ca)-asin(intStart/ca))+half*(intEnd*sqrt(sqr(ca)-sqr(intEnd))-intStart*sqrt(sqr(ca)-sqr(intStart)))+(intStart-intEnd)*(lowerLimit+ballRadius);
}

long double solve() {
	long double ret=0;
	for(long double x=chordThick;x<innerRadius;x+=(long double)(g+two*chordThick)) {
		for(long double y=chordThick;y<innerRadius;y+=(long double)(g+two*chordThick)) {
			long double x2=x+g;
			long double y2=y+g;
			if (inCircle(x2,y2)) {
				ret+=add;
			}
			else {
				if (inCircle(x2,y)) {
					if (inCircle(x,y2)) {
						long double xone=sqrt(sqr(innerRadius-ballRadius)-sqr(y2-ballRadius));
						long double newx=x;
							if (xone>x+ballRadius) {
								ret+=(g-two*ballRadius)*(xone-x-ballRadius);
								newx=xone-ballRadius;
							}
							
							if (newx+two*ballRadius<x2) {
								if (sqr(innerRadius-ballRadius)-sqr(newx+ballRadius)>sqr(y+ballRadius)) {
									long double lo=newx+ballRadius;
									long double hi=x2-ballRadius;
									
									while (hi>lo+err) {
										long double mid=(hi+lo)*half;
										if (sqr(innerRadius-ballRadius)-sqr(mid)>sqr(y+ballRadius)) {lo=mid;}
										else {hi=mid;}
									}
									ret+=nInt(y,newx+ballRadius,lo);
								}								
							}
					}
					else {
						if (sqr(innerRadius-ballRadius)-sqr(x+ballRadius)>sqr(y+ballRadius)) {
							long double lo=x+ballRadius;
							long double hi=x2-ballRadius;
							
							while (hi>lo+err) {
								long double mid=(hi+lo)*half;
								if (sqr(innerRadius-ballRadius)-sqr(mid)>sqr(y+ballRadius)) {lo=mid;}
								else {hi=mid;}
							}
							ret+=nInt(y,x+ballRadius,lo);
						}
					}
				}
				else {
					if (inCircle(x,y2)) {
						if (sqr(innerRadius-ballRadius)-sqr(y+ballRadius)>sqr(x+ballRadius)) {
							long double lo=y+ballRadius;
							long double hi=y2-ballRadius;
							
							while (hi>lo+err) {
								long double mid=(hi+lo)*half;
								if (sqr(innerRadius-ballRadius)-sqr(mid)>sqr(x+ballRadius)) {lo=mid;}
								else {hi=mid;}
							}
							ret+=nInt(x,y+ballRadius,lo);
						}
					}
					else {
						long double xtwo=sqrt(sqr(innerRadius-ballRadius)-sqr(y+ballRadius));
						if (x+ballRadius<xtwo) {
							if (sqr(innerRadius-ballRadius)-sqr(x+ballRadius)>sqr(y+ballRadius)) {
								long double lo=x+ballRadius;
								long double hi=xtwo;
								
								while (hi>lo+err) {
									long double mid=(hi+lo)*half;
									if (sqr(innerRadius-ballRadius)-sqr(mid)>sqr(y+ballRadius)) {lo=mid;}
									else {hi=mid;}
								}
								ret+=nInt(y,x+ballRadius,lo);
							}							
						}
					}
				}
			}
		}
	}
	
	ret/=((long double)(sqr(outerRadius)*PI));
	ret*=two;
	ret*=two;
	ret=one-ret;
	return ret;
}

int main() {
	FILE * fin=fopen("C-small.in","r");
	FILE * fout=fopen("C-small.out","w");
	
	fscanf(fin,"%d ",&cases);
	for(int i=0;i<cases;i++) {
		fprintf(fout,"Case #%d: ",i+1);
		fscanf(fin,"%Lf %Lf %Lf %Lf %Lf ",&ballRadius,&outerRadius,&thickness,&chordThick,&g);
		innerRadius=outerRadius-thickness;
		add=sqr(g-two*ballRadius);
		if (g<two*ballRadius || innerRadius<ballRadius) {
			fprintf(fout,"%Lf\n",one);
		}
		else {
			fprintf(fout,"%Lf\n",solve());
		}
	}	
	return 0;
}
