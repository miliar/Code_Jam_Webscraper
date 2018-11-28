#include <stdio.h>
#include <cmath> 
#include <set>
#include <vector>
#include <iostream>

using namespace std;

const double ss = 0;
const double ee = 100;

#define INF  1e200
#define EP  1e-10
#define MAXV  300
#define PI  3.14159265

/* �������νṹ */ 
struct POINT { 
    double x; 
    double y; POINT(double a=0, double b=0) { x=a; y=b;} //constructor 
}; 
bool operator < (const POINT &x, const POINT &y) {
	if (x.x != y.x) {
		return x.x < y.x;
	} else {
		return x.y < y.y;
	}
}
struct LINESEG { 
    POINT s; 
    POINT e;
    LINESEG(POINT a, POINT b) { s=a; e=b;} 
    LINESEG() { } 
}; 
struct LINE {// ֱ�ߵĽ������� a*x+b*y+c=0 Ϊͳһ��ʾ��Լ�� a >= 0 
    double a; 
    double b; 
    double c;
    LINE(double d1=1, double d2=-1, double d3=0) {a=d1; b=d2; c=d3;} 
}; 

double max(double a,double b) {
    if (a>b) return a;
    return b;
}
double min(double a,double b) {
    if (a>b) return b;
    return a;
}    
/********************\ 
* * 
* ��Ļ������� * 
* * 
\********************/ 

double dist(POINT p1,POINT p2) {// ��������֮��ŷ�Ͼ��� 
    return( sqrt( (p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y) ) ); 
} 
bool equal_point(POINT p1,POINT p2) {// �ж��������Ƿ��غ� 
     return ( (fabs(p1.x-p2.x)<EP)&&(fabs(p1.y-p2.y)<EP) ); 
} 

/****************************************************************************** 
r=multiply(sp,ep,op),�õ�(sp-op)*(ep-op)�Ĳ�� 
r>0:ep��ʸ��opsp����ʱ�뷽�� 
r=0��opspep���㹲�ߣ� 
r<0:ep��ʸ��opsp��˳ʱ�뷽�� 
*******************************************************************************/ 

double multiply(POINT sp,POINT ep,POINT op) { 
    return((sp.x-op.x)*(ep.y-op.y)-(ep.x-op.x)*(sp.y-op.y)); 
} 

/******************************************************************************* 
r=dotmultiply(p1,p2,op),�õ�ʸ��(p1-op)��(p2-op)�ĵ�����������ʸ��������ʸ�� 
r<0:��ʸ���н�Ϊ��ǣ�r=0����ʸ���н�Ϊֱ�ǣ�r>0:��ʸ���н�Ϊ�۽� 
*******************************************************************************/ 
double dotmultiply(POINT p1,POINT p2,POINT p0) { 
    return ((p1.x-p0.x)*(p2.x-p0.x)+(p1.y-p0.y)*(p2.y-p0.y)); 
} 

/* �жϵ�p�Ƿ����߶�l�ϣ�������(p���߶�l���ڵ�ֱ����)&& (��p�����߶�lΪ�Խ��ߵľ�����) */ 
bool online(LINESEG l,POINT p) { 
	return p.x > ss && p.x < ee;
    return((multiply(l.e,p,l.s)==0) &&( ( (p.x-l.s.x)*(p.x-l.e.x)<=0 )&&( (p.y-l.s.y)*(p.y-l.e.y)<=0 ) ) ); 
} 

// ���ص�p�Ե�oΪԲ����ʱ����תalpha(��λ������)�����ڵ�λ�� 
POINT rotate(POINT o,double alpha,POINT p) { 
    POINT tp; 
    p.x-=o.x; 
    p.y-=o.y; 
    tp.x=p.x*cos(alpha)-p.y*sin(alpha)+o.x; 
    tp.y=p.y*cos(alpha)+p.x*sin(alpha)+o.y; 
    return tp; 
} 

/* ���ض�����o�㣬��ʼ��Ϊos����ֹ��Ϊoe�ļн�(��λ������) 
�Ƕ�С��pi��������ֵ 
�Ƕȴ���pi�����ظ�ֵ 
�����������߶�֮��ļн� 
*/ 
double angle(POINT o,POINT s,POINT e) { 
    double cosfi,fi,norm; 
    double dsx = s.x - o.x; 
    double dsy = s.y - o.y; 
    double dex = e.x - o.x; 
    double dey = e.y - o.y; 

    cosfi=dsx*dex+dsy*dey; 
    norm=(dsx*dsx+dey*dey)*(dex*dex+dey*dey); 
    cosfi /= sqrt( norm ); 

    if (cosfi >= 1.0 ) return 0; 
    if (cosfi <= -1.0 ) return -3.1415926; 

    fi=acos(cosfi); 
    if (dsx*dey-dsy*dex>0) return fi; // ˵��ʸ��os ��ʸ�� oe��˳ʱ�뷽�� 
    return -fi; 
} 

 

/*****************************\ 
* * 
* �߶μ�ֱ�ߵĻ������� * 
* * 
\*****************************/ 

/* �жϵ����߶εĹ�ϵ,��;�ܹ㷺 
�������Ǹ�������Ĺ�ʽд�ģ�P�ǵ�C���߶�AB����ֱ�ߵĴ��� 

AC dot AB 
r = --------- 
||AB||^2 
(Cx-Ax)(Bx-Ax) + (Cy-Ay)(By-Ay) 
= ------------------------------- 
L^2 

r has the following meaning: 

r=0 P = A 
r=1 P = B 
r<0 P is on the backward extension of AB 
r>1 P is on the forward extension of AB 
0<r<1 P is interior to AB 
*/ 
double relation(POINT p,LINESEG l) { 
    LINESEG tl; 
    tl.s=l.s; 
    tl.e=p; 
    return dotmultiply(tl.e,l.e,l.s)/(dist(l.s,l.e)*dist(l.s,l.e)); 
} 

// ���C���߶�AB����ֱ�ߵĴ��� P 
POINT perpendicular(POINT p,LINESEG l) { 
    double r=relation(p,l); 
    POINT tp; 
    tp.x=l.s.x+r*(l.e.x-l.s.x); 
    tp.y=l.s.y+r*(l.e.y-l.s.y); 
    return tp; 
} 
/* ���p���߶�l����̾���,�������߶��Ͼ�õ�����ĵ�np 
ע�⣺np���߶�l�ϵ���p����ĵ㣬��һ���Ǵ��� */ 
double ptolinesegdist(POINT p,LINESEG l,POINT &np) { 
    double r=relation(p,l); 
    if (r<0) { 
        np=l.s; 
        return dist(p,l.s); 
    } 
    if(r>1) { 
        np=l.e; 
        return dist(p,l.e); 
    } 
    np=perpendicular(p,l); 
    return dist(p,np); 
} 

// ���p���߶�l����ֱ�ߵľ���,��ע�Ȿ�������ϸ����������� 
double ptoldist(POINT p,LINESEG l) { 
    return abs(multiply(p,l.e,l.s))/dist(l.s,l.e); 
} 

/* ����㵽���߼����������,�����������. 
ע�⣺���õ���ptolineseg()���� */ 
double ptopointset(int vcount,POINT pointset[],POINT p,POINT &q) { 
    int i; 
    double cd,td; cd=INF;
    LINESEG l; 
    POINT tq,cq; 

    for (i=0;i<vcount-1;i++) { 
        l.s=pointset[ i ]; 
        l.e=pointset[i+1]; 
        td=ptolinesegdist(p,l,tq);
        if (td<cd) {
            cd=td;
            cq=tq;
        }
    }
    q=cq; 
    return cd; 
} 
/* �ж�Բ�Ƿ��ڶ������.ptolineseg()������Ӧ��2 */ 
bool CircleInsidePolygon(int vcount,POINT center,double radius,POINT polygon[]) { 
    POINT q; 
    double d; 
    q.x=0; 
    q.y=0; 
    d=ptopointset(vcount,polygon,center,q); 
    if (d<radius||fabs(d-radius)<EP) return true; 
    else return false; 
} 

/* ��������ʸ��l1��l2�ļнǵ�����(-1 --- 1)ע�⣺������������нǵĻ���ע�ⷴ���Һ����Ķ������Ǵ� 0��pi */ 
double cosine(LINESEG l1,LINESEG l2) { 
    return (((l1.e.x-l1.s.x)*(l2.e.x-l2.s.x) + (l1.e.y-l1.s.y)*(l2.e.y-l2.s.y))/(dist(l1.e,l1.s)*dist(l2.e,l2.s))) ; 
} 
// �����߶�l1��l2֮��ļн� ��λ������ ��Χ(-pi��pi) 
double lsangle(LINESEG l1,LINESEG l2) { 
    POINT o,s,e; 
    o.x=o.y=0; 
    s.x=l1.e.x-l1.s.x; 
    s.y=l1.e.y-l1.s.y; 
    e.x=l2.e.x-l2.s.x; 
    e.y=l2.e.y-l2.s.y; 
    return angle(o,s,e); 
} 
// ����߶�u��v�ཻ(�����ཻ�ڶ˵㴦)ʱ������true 
bool intersect(LINESEG u,LINESEG v) { 
    return ( (max(u.s.x,u.e.x)>=min(v.s.x,v.e.x))&& //�ų�ʵ�� 
        (max(v.s.x,v.e.x)>=min(u.s.x,u.e.x))&& 
        (max(u.s.y,u.e.y)>=min(v.s.y,v.e.y))&& 
        (max(v.s.y,v.e.y)>=min(u.s.y,u.e.y))&& 
        (multiply(v.s,u.e,u.s)*multiply(u.e,v.e,u.s)>=0)&& //����ʵ�� 
        (multiply(u.s,v.e,v.s)*multiply(v.e,u.e,v.s)>=0)); 
} 


// (�߶�u��v�ཻ)&&(���㲻��˫���Ķ˵�) ʱ����true 
bool intersect_A(LINESEG u,LINESEG v) { 
    return ((intersect(u,v))&& 
        (!online(u,v.s))&& 
        (!online(u,v.e))&& 
        (!online(v,u.e))&& 
        (!online(v,u.s))); 
} 


// �߶�v����ֱ�����߶�u�ཻʱ����true���������ж��߶�u�Ƿ�����߶�v 
bool intersect_l(LINESEG u,LINESEG v) { 
    return multiply(u.s,v.e,v.s)*multiply(v.e,u.e,v.s)>=0; 
} 


// ������֪�������꣬����������ֱ�߽������̣� a*x+b*y+c = 0 (a >= 0) 
LINE makeline(POINT p1,POINT p2) { 
    LINE tl; 
    int sign = 1; 
    tl.a=p2.y-p1.y; 
    if (tl.a<0) { 
        sign = -1; 
        tl.a=sign*tl.a; 
    } 
    tl.b=sign*(p1.x-p2.x); 
    tl.c=sign*(p1.y*p2.x-p1.x*p2.y); 
    return tl; 
} 

// ����ֱ�߽������̷���ֱ�ߵ�б��k,ˮƽ�߷��� 0,��ֱ�߷��� 1e200 
double slope(LINE l) { 
    if (abs(l.a) < 1e-20) return 0; 
    if (abs(l.b) < 1e-20) return INF;
    return -(l.a/l.b); 
} 

// ����ֱ�ߵ���б��alpha ( 0 - pi) 
double alpha(LINE l) { 
    if (abs(l.a)< EP) return 0; 
    if (abs(l.b)< EP) return PI/2; 
    double k=slope(l); 
    if (k>0) return atan(k);
    else return PI+atan(k); 
} 

// ���p����ֱ��l�ĶԳƵ� 
POINT symmetry(LINE l,POINT p) { 
    POINT tp; 
    tp.x=((l.b*l.b-l.a*l.a)*p.x-2*l.a*l.b*p.y-2*l.a*l.c)/(l.a*l.a+l.b*l.b); 
    tp.y=((l.a*l.a-l.b*l.b)*p.y-2*l.a*l.b*p.x-2*l.b*l.c)/(l.a*l.a+l.b*l.b); 
    return tp; 
} 

// �������ֱ�� l1(a1*x+b1*y+c1 = 0), l2(a2*x+b2*y+c2 = 0)�ཻ������true���ҷ��ؽ���p 
bool lineintersect(LINE l1,LINE l2,POINT &p) {// �� L1��L2 
    double d=l1.a*l2.b-l2.a*l1.b; 
    if (abs(d)<EP) return false;// ���ཻ 
    p.x = (l2.c*l1.b-l1.c*l2.b)/d; 
    p.y = (l2.a*l1.c-l1.a*l2.c)/d; 
    return true; 
} 

// ����߶�l1��l2�ཻ������true�ҽ�����(inter)���أ����򷵻�false 
bool intersection(LINESEG l1,LINESEG l2,POINT &inter) { 
    LINE ll1,ll2; 
    ll1=makeline(l1.s,l1.e); 
    ll2=makeline(l2.s,l2.e); 
    if (lineintersect(ll1,ll2,inter)) return online(l1,inter) && online(l2,inter); 
    else return false; 
}

set<POINT> a;
vector<LINESEG> b;
int n;

void Input() {
	POINT t1,t2;
	t1.x = ss;	
	t2.x = ee;

	cin >> n;

	a.clear();
	b.clear();
	for (int i = 0; i < n; ++i) {
		cin >> t1.y >> t2.y;
		LINESEG tmp(t1,t2);
		b.push_back(tmp);
	}
}

long long Solve() {
	long long res = 0;
	for (int i = 0; i < b.size(); ++i) {
		for (int j = i + 1; j < b.size(); ++j) {
			POINT tmp;
			if (b[i].s.y == b[j].s.y || b[i].e.y == b[j].e.y)
				continue;
			if (intersection(b[i], b[j], tmp) == true) {
				if (a.find(tmp) == a.end()) {
					++res;
					a.insert(tmp);
				}
			}
		}
	}
	return res;
}

int Easy() {
	cin >> n;
	int tmp[4];
	for (int i = 0; i < n; ++i) {
		cin >> tmp[i * 2] >> tmp[i * 2 + 1];
	}
	if (n == 1)
		return 0;
	if (tmp[0] < tmp[2]) {
		if (tmp[1] > tmp[3])
			return 1;
	} else if (tmp[0] > tmp[2]) {
		if (tmp[1] < tmp[3])
			return 1;
	}
	return 0;
}

int main() {
	// freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out_large.txt","w",stdout);
	int ncase;
	cin >> ncase;
	for (int i = 0; i < ncase; ++i) {
		Input();
		long long ans = Solve();
		// long long ans = Easy();
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}
	return 0;
}