
#include<iostream>
#include<cmath>
using namespace std;
const double eps=1e-8;
int dblcmp(double x,double y)
{
	if(fabs(x-y)<eps)
		return 0;
	if(x>y)
		return 1;
	return -1;	
}//�������
typedef struct 
{
	double x;
	double y;
}point;//��Ľṹ
typedef struct 
{
	point p1;
	point p2;
}seg;//�߶εĽṹ
double  length(double x,double y)
{
	return sqrt(x*x+y*y);
}//��������
double dotdet(double x1,double y1,double x2,double y2)
{
	return x1*x2+y1*y2;
}//���
double dot(point a,point b,point c)
{
	return dotdet(b.x-a.x,b.y-a.y,c.x-a.x,c.y-a.y);
}//�����ĵ��
double  dis(double x1,double y1,double x2,double y2)
{
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}//����
double det(double x1,double y1,double x2,double y2)
{
	return x1*y2-x2*y1;
}//���
double cross(point a,point b,point c)
{
	return det(b.x-a.x,b.y-a.y,c.x-a.x,c.y-a.y);
}//�������
int betweencmp(point a,point b,point c)
{
	return dblcmp(dot(a,b,c),0.0);
}//�жϵ�c�ǲ������߶�a,b�䣬<=0��֮��(0Ϊ��ֵ)

int dots_inline(point p1,point p2,point p3)
{
	return !dblcmp(cross(p1,p2,p3),0.0);
}//�����㹲��
int dots_inline(int x1,int y1,int x2,int y2,int x3,int y3)
{
	return !dblcmp(det(x3-x1,y3-y1,x3-x2,y3-y2),0.0);
}//�����㹲��

bool parallel(seg u,seg v)
{
	return (u.p1.x-u.p2.x)*(v.p1.y-v.p2.y)==(v.p1.x-v.p2.x)*(u.p1.y-u.p2.y);
}//����ֱ��ƽ��
bool parallel(point u1,point u2,point v1,point v2)
{
	return (u1.x-u2.x)*(v1.y-v2.y)==(v1.x-v2.x)*(u1.y-u2.y);
}//����ֱ��ƽ��
bool perpendicular(seg u,seg v)
{
	return (u.p1.x-u.p2.x)*(v.p1.x-v.p2.x)==-(u.p1.y-u.p2.y)*(v.p1.y-v.p2.y);
}//����ֱ�ߴ�ֱ
int perpendicular(point u1,point u2,point v1,point v2)
{
	return (u1.x-u2.x)*(v1.x-v2.x)==-(u1.y-u2.y)*(v1.y-v2.y);
}//����ֱ�ߴ�ֱ
int segcross(point a,point b,point c,point d,point &p)
{
	double s1,s2,s3,s4;
	int d1,d2,d3,d4;
	d1=dblcmp(s1=cross(a,b,c),0.0);
	d2=dblcmp(s2=cross(a,b,d),0.0);
	d3=dblcmp(s3=cross(c,d,a),0.0);
	d4=dblcmp(s4=cross(c,d,b),0.0);
	if((d1^d2)==-2&&(d3^d4)==-2)
	{
		p.x=(c.x*s2-d.x*s1)/(s2-s1);
		p.y=(c.y*s2-d.y*s1)/(s2-s1);
		return 1;
	}
	if(d1==0&&betweencmp(c,a,b)<=0||d2==0&&betweencmp(d,a,b)<=0||d3==0&&betweencmp(a,c,d)<=0||d4==0&&betweencmp(b,c,d)<=0)
		return 2;
	return 0;
}//0--���ཻ��1--�ཻ��һ�㣬2--һ��ֱ�ߵ�һ���˵�������һ����

int main(){
	freopen("G:\\A-large.in","r",stdin);
	freopen("G:\\A-large.out","w",stdout);
	point p[2000][3];
	int t ; 
	scanf("%d",&t);
	for(int cases = 1; cases<=t;++cases){
		int n ; 
		scanf("%d",&n);
		for(int i = 0 ; i<n ;++i ){
			int a , b ;
			scanf("%d%d",&a,&b);
			p[i][0].x = 0 , p[i][0].y = a ;
			p[i][1].x = 1000,p[i][1].y = b ;
		}
		int cnt = 0 ; 
		point tmp;
		for(int i = 0 ;i<n ;++i)
			for(int j = 0 ; j<i;++j)
				if(segcross(p[i][0],p[i][1],p[j][0],p[j][1] ,tmp )!=0 )
					cnt++;
		printf("Case #%d: %d\n",cases,cnt);
	}
	return 0 ;

}