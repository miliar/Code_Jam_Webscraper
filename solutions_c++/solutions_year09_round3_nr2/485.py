#include <cstdio>
#include <cmath>

int main()
{
     int t, i;
     scanf("%d", &t);

     for (i = 1; i <= t; ++i) {
	  double dmin, tmin, proj, vm, dist;
	  int n, j;
	  int coor[500][3], velo[500][3];
	  double m[3] = {0}, v[3] = {0};
	  scanf("%d", &n);
	  for (j = 0; j < n; ++j) {
	       scanf("%d %d %d %d %d %d", &(coor[j][0]), &(coor[j][1]),
		     &(coor[j][2]), &(velo[j][0]),
		     &(velo[j][1]), &(velo[j][2]));
	       m[0] += coor[j][0];
	       m[1] += coor[j][1];
	       m[2] += coor[j][2];
	       v[0] += velo[j][0];
	       v[1] += velo[j][1];
	       v[2] += velo[j][2];
	  }
	  m[0] /= (double)n;
	  m[1] /= (double)n;
	  m[2] /= (double)n;

	  v[0] /= (double)n;
	  v[1] /= (double)n;
	  v[2] /= (double)n;

// 	  v[0] -= m[0];
// 	  v[1] -= m[1];
// 	  v[2] -= m[2];

	  proj = m[0] * v[0] + m[1] * v[1] + m[2] * v[2];
	  if (proj >= 0) {
	       dmin = sqrt(fabs(m[0] * m[0] + m[1] * m[1] + m[2] * m[2]));
	       tmin = 0;
	  } else {
	       vm = sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2]);
	       proj = -proj / vm;
	       tmin = proj / vm;
	       dmin = m[0] * m[0] + m[1] * m[1] + m[2] * m[2] - proj * proj;
	       if (dmin < 1e-11)
		    dmin = 0;
	       else
		    dmin = sqrt(dmin);
	  }
	  
	  
	  printf("Case #%d: %.8lf %.8lf\n", i, dmin, tmin);
     }
     
     return 0;
}
