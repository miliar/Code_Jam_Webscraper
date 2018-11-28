#include<stdio.h>
#include<math.h>
#include<vector>
#include<iostream>
using namespace std;

const double eps = 1e-8;

struct CPoint
{
	double x,y;
};

double sqr(double x) {return x*x;}

int CircleCrossCircle(CPoint p1, double r1, CPoint p2, double r2, CPoint& cp1, CPoint& cp2)
{
	double mx = p2.x - p1.x, sx = p2.x + p1.x, mx2 = mx * mx;
	double my = p2.y - p1.y, sy = p2.y + p1.y, my2 = my * my;
	double sq = mx2 + my2, d = - (sq - sqr(r1-r2)) * (sq - sqr(r1+r2));
	if(d+eps<0) return 0; if(d<eps) d = 0; else d = sqrt(d);
	double x = mx * ( (r1 + r2) * (r1 - r2) + mx * sx) + sx * my2;
	double y = my * ( (r1 + r2) * (r1 - r2) + my * sy) + sy * mx2;
	double dx = mx * d, dy = my * d; sq *= 2;
	cp1.x = (x - dy) / sq; cp1.y = (y + dx) / sq;
	cp2.x = (x + dy) / sq; cp2.y = (y - dx) / sq;
	if(d>eps) return 2;
	return 1;
}

vector<CPoint> v;
vector<double> R;

bool foo(CPoint p1, double r1, CPoint p2, double r2)
{
	if(r1<r2-eps) return false;
	double dx = p1.x - p2.x;
	double dy = p1.y - p2.y;
	double dist = sqrt(dx * dx + dy * dy);
	if(dist <= r1 - r2 + eps) return true;
	return false;
}

int main()
{
	int t,kase=0;
	scanf("%d",&t);
	while(t--)
	{
		int n;
		scanf("%d",&n);
		v.clear();
		R.clear();
		double x,y,r;
		for(int i=0;i<n;i++)
		{
			scanf("%lf %lf %lf",&x,&y,&r);
			CPoint p;
			p.x=x; p.y=y;
			v.push_back(p);
			R.push_back(r);
		}
		if(n==1)
		{
			printf("Case #%d: %.6lf\n",++kase,R[0]);
			continue;
		}
		double lo = 0, hi = 5000, mid;
		int step = 0;
		while(fabs(lo-hi)>1e-6&&step<100)
		{
			step++;
			mid = (lo + hi) / 2;
			//cout<<mid<<endl;
			bool ff=false;
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
					for(int k=0;k<n;k++)
						for(int l=0;l<n;l++)
						{
							vector<CPoint> v1,v2;
							CPoint ans1,ans2;
							v1.clear(); v2.clear();
							if(i==j) v1.push_back(v[i]);
							else
							{
								int ret1 = CircleCrossCircle(v[i],mid - R[i],v[j],mid - R[j],ans1,ans2);
								if(ret1>=1) v1.push_back(ans1);
								if(ret1==2) v1.push_back(ans2);
							}
							if(k==l) v2.push_back(v[k]);
							else
							{
								int ret2 = CircleCrossCircle(v[k],mid - R[k],v[l],mid - R[l],ans1,ans2);
								if(ret2>=1) v2.push_back(ans1);
								if(ret2==2) v2.push_back(ans2);
							}
							int sz1=(int)v1.size();
							int sz2=(int)v2.size();
							/*
							cout<<i<<" "<<j<<" "<<k<<" "<<l<<endl;
							cout<<v[i].x<<" "<<v[i].y<<" "<<mid-R[i]<<endl;
							cout<<v[j].x<<" "<<v[j].y<<" "<<mid-R[j]<<endl;
							cout<<v[k].x<<" "<<v[k].y<<" "<<mid-R[k]<<endl;
							cout<<v[l].x<<" "<<v[l].y<<" "<<mid-R[l]<<endl;
							cout<<sz1<<" "<<sz2<<endl;
							for(int ii=0;ii<sz1;ii++)
								cout<<v1[ii].x<<" "<<v1[ii].y<<endl;
							for(int ii=0;ii<sz2;ii++)
								cout<<v2[ii].x<<" "<<v2[ii].y<<endl;
							*/
							for(int ii=0;ii<sz1;ii++)
								for(int jj=0;jj<sz2;jj++)
								{
									bool hash[100];
									memset(hash,0,sizeof(hash));
									int cnt=0;
									for(int k=0;k<n;k++)
										if(foo(v1[ii],mid,v[k],R[k]))
											hash[k]=true;
									for(int k=0;k<n;k++)
										if(foo(v2[jj],mid,v[k],R[k]))
											hash[k]=true;
									for(int k=0;k<n;k++)
										if(hash[k])
											cnt++;
									if(cnt==n)
									{
										/*
										cout<<v1[ii].x<<" "<<v1[ii].y<<" "<<mid<<endl;
										cout<<v2[jj].x<<" "<<v1[jj].y<<" "<<mid<<endl;
										*/
										ff=true;
										break;
									}
								}
							if(ff) break;
						}
			if(ff) hi = mid;
			else lo = mid;
		}
		printf("Case #%d: %.6lf\n",++kase,mid);
	}
	return 0;
}