#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#define MAXN 1050

using namespace std;

int a,b,c,d,e;
int ansx,ansy,ansz;
double minx,miny,minz;
double sx,sy,sz;
double bawahx,bawahy,bawahz;
double atasx,atasy,atasz;
double best;
int jmlcase;
int x[MAXN];
int y[MAXN];
int z[MAXN];
int n;
int p[MAXN];


int power[MAXN];
double cx,cy,cz,cp,ccc;
double count(void) {
	//printf("%.7lf %.7lf %.7lf\n",sx,sy,sz);
	//printf("%.3lf %.3lf %.3lf\n",sx,sy,sz);
	int aa;
	double maxi = 0;
	//printf("%d\n",n);
	for (aa = 0;aa < n;aa++) {
		cp = p[aa];
		cx = fabs(sx - (double)x[aa]);
		cy = fabs(sy - (double)y[aa]);
		cz = fabs(sz - (double)z[aa]);
		ccc = ((cx + cy + cz)) / cp;
		//printf("%lf\n",ccc);
		maxi = fmax(maxi,ccc);
		}
	return maxi;
	}
		

double shit(void) {
	double best = 99999999;
	atasz = 0;
				bawahz = 1000000;
				while ((bawahz - atasz >= 0.0000001)) {
					//printf("%.7lf %.7lf\n",bawahz,atasz);
					sz = (bawahz + atasz) / 2.0;
					
					double temp = count();
				
					best = fmin(best,temp);
				
					sz -= 0.0000001;
				
					double kiri = count();
					sz += 0.0000002;
					double kanan = count();
				
					//if (temp <= kiri && temp <= kanan) break;
					if (temp >= kiri) {
		
						sz -= 0.0000001;
				
						bawahz = sz;
						continue;
						}
					atasz = sz - 0.0000001;
					}
				return best;
				}

double crazy(void) {
	double best = 99999999;
	atasy = 0;
				bawahy = 1000000;
				while ((bawahy - atasy >= 0.0000001)) {
					
					sy = (bawahy + atasy) / 2.0;
					double temp = shit();
		
					best = fmin(best,temp);
					sy -= 0.0000001;
					double kiri = shit();
					sy += 0.0000002;
					double kanan = shit();
					//if (temp <= kiri && temp <= kanan) break;
					if (temp >= kiri) {
						bawahy = sy - 0.0000001;
						continue;
						}
					atasy = sy- 0.0000001;
					}
				return best;
				}

double love(void) {
	double best = 99999999;
	atasx = 0;
				bawahx = 1000000;
				while ((bawahx - atasx >= 0.0000001)) {
					
					sx = (bawahx + atasx) / 2.0;
					double temp = crazy();
		
					best = fmin(best,temp);
					sx -= 0.0000001;
					double kiri = crazy();
					sx += 0.0000002;
					double kanan = crazy();
					//if (temp <= kiri && temp <= kanan) break;
					if (temp >= kiri) {
						bawahx = sx - 0.0000001;
						continue;
						}
					atasx = sx- 0.0000001;
					}
				return best;
				}

int main() {
	
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d",&n);
		printf("Case #%d: ",e + 1);
		for (a = 0;a < n;a++) {
			scanf("%d%d%d%d",&x[a],&y[a],&z[a],&p[a]);
			}
		atasx = 0;
		bawahx = 1000000;
		double answer = 999999999;
	
		double jawab = love();
	
		printf("%.6lf\n",jawab);
	
	
	}
	return 0;
	}

