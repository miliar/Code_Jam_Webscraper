#include<cstdio>
#include<cmath>
struct point{
	double X, Y;
}LP[1001], UP[1001];
int T, L, U, G;
double W, area;
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		area = 0.0;
		printf("Case #%d:\n", t);
		scanf("%lf%d%d%d", &W, &L, &U, &G);
		for(int i = 0; i < L; i++)
			scanf("%lf%lf", &LP[i].X, &LP[i].Y);
		for(int i = 0; i < U; i++)
			scanf("%lf%lf", &UP[i].X, &UP[i].Y);
		for(int i = 0; i + 1 < L; i++)
			area += LP[i].X * LP[i + 1].Y - LP[i].Y * LP[i + 1].X;
		area += LP[L - 1].X * UP[U - 1]. Y - LP[L - 1].Y * UP[U - 1].X;
		for(int i = U - 1; i > 0; i--)
			area += UP[i].X * UP[i - 1].Y - UP[i].Y * UP[i - 1].X;
		area += UP[0].X * LP[0].Y - UP[0].Y * LP[0].X;
		if(area < 0.0)area = -area;
		area /= 2.0;
		area /= double(G);
		//printf("%lf\n", area);
		double now_len = UP[0].Y - LP[0].Y, lst = 0.0, now_area = 0.0;
		for(int i = 1, j = 1, c = 0; i < L && j < U && c < G - 1; ){
			double tmp_len, dX;
			//puts("JIZZ");
			if(LP[i].X < UP[j].X){
				double dY = UP[j - 1].Y + (UP[j].Y - UP[j - 1].Y) * (LP[i].X - UP[j - 1].X) / (UP[j].X - UP[j - 1].X); 
				tmp_len = dY - LP[i].Y;
				dX = LP[i].X - lst;
				double t_area = (tmp_len + now_len) * dX / 2.0;
				//printf("t_area = %lf %lf %lf %lf %lf\n", t_area, tmp_len, now_len, dX, dY);
				//a = now_len, b = tmp_len
				if(t_area + now_area > area){
					double left = area - now_area;
					double root = 
						dX / (tmp_len - now_len) * (sqrt(now_len * now_len + 2.0 * left * (tmp_len - now_len) / dX) - now_len);
					if(tmp_len - now_len > -1e-6 && tmp_len - now_len < 1e-6)root = left / now_len;
					//printf("root = %lf\n", root);
					printf("%lf\n", lst + root);
					c++;
					lst += root;
					now_area = 0.0;
					now_len += (tmp_len - now_len) * (root / dX);
				}else{
					now_area += t_area;
					now_len = tmp_len;
					lst = LP[i].X;
					i++;
					//puts("1");
				}
			}else{
				double dY = LP[i - 1].Y + (LP[i].Y - LP[i - 1].Y) * (UP[j].X - LP[i- 1].X) / (LP[i].X - LP[i - 1].X); 
				tmp_len = UP[j].Y - dY;
				dX = UP[j].X - lst;
				double t_area = (tmp_len + now_len) * dX / 2.0;
				//a = now_len, b = tmp_len
				//printf("t_area = %lf %lf %lf\n", t_area, tmp_len, now_len, dX);
				if(t_area + now_area > area){
					double left = area - now_area;
					double root = 
						dX / (tmp_len - now_len) * (sqrt(now_len * now_len + 2.0 * left * (tmp_len - now_len) / dX) - now_len);
					if(tmp_len - now_len > -1e-6 && tmp_len - now_len < 1e-6)root = left / now_len;
					//printf("root = %lf\n", root);
					printf("%lf\n", lst + root);
					c++;
					lst += root;
					now_area = 0.0;
					now_len += (tmp_len - now_len) * (root / dX);
				}else{
					now_area += t_area;
					now_len = tmp_len;
					lst = UP[j].X;
					j++;
					//puts("2");
				}
			}
			//printf("%lf %d %d %d %lf\n", now_area, c, i, j, lst);
		}
	}
}
