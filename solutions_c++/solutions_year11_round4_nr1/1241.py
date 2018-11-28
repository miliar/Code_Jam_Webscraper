#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int MAX = 4000;
const double eps = 1e-8;
int n, x;
double rt, s, r;
double ans;

struct Node {
	int b, e, w;
	Node(){}
	Node(int _b, int _e, int _w):
		b(_b), e(_e), w(_w){}
	bool operator < (const Node &p) const {
		 return w < p.w;	 
    }	
}nn[MAX];

struct Node2 {
	int b, e;
	Node2(){}
	Node2(int _b, int _e):
		b(_b), e(_e){}
	bool operator < (const Node2 &p) const {
		 return b < p.b;	 
    }	
}nn2[MAX];


int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int i, j, icas, cas;
	scanf("%d", &cas);
	for (icas = 1; icas <= cas; ++icas) {
		scanf("%d%lf%lf%lf%d", &x, &s, &r, &rt, &n);
		j = 0;
		memset(nn2, 0, sizeof(nn2));
		for (i = 0; i < n; ++i) {
			scanf("%d%d%d", &nn[i].b, &nn[i].e, &nn[i].w);
			nn2[i].b = nn[i].b;
			nn2[i].e = nn[i].e;
		}
		int tn  = n;
		sort(nn2, nn2 + n);
		nn[n++] = Node(0, nn2[0].b, 0);
		for (i = 1; i < tn; ++i) {
			nn[n++] = Node(nn2[i - 1].e, nn2[i].b, 0);
		}
		if (tn >= 1)
		   nn[n++] = Node(nn2[tn - 1].e, x, 0);
		else
			nn[n++] = Node(0, x, 0);
	//	printf("$$$$$$$$$$\n");
		sort(nn, nn + n);
	//	for (i = 0; i < n; ++i)
	//		printf("%d %d %d\n", nn[i].b, nn[i].e, nn[i].w);
	//	printf("\n");
		
		ans = 0.0;
		
		for (i = 0; i < n; ++i) {
			if (nn[i].e == nn[i].b) continue;
			if (rt > eps) {
   			   double tmp = (nn[i].e - nn[i].b) / (nn[i].w + r);
   		//	   printf("tt %lf %lf\n", rt,tmp);
   			   if (tmp <= rt) {
			   	  ans += tmp;
				  rt -= tmp;	  	   
               }
               else {
      		      double d = (nn[i].w + r) * rt;
      		      ans += rt + (nn[i].e - nn[i].b - d) / (nn[i].w + s);
      		      i++;
      		      break;
			   }	  
	        }
	        else
	        	break;
		}
		for (; i < n; ++i) {
			if (nn[i].e == nn[i].b) continue;
			ans += (nn[i].e - nn[i].b) / (nn[i].w + s);
		//	printf("t2 %lf\n",ans);
			
		}
		printf("Case #%d: %.8lf\n", icas, ans);
	}
	
	
//	system("pause");	
}