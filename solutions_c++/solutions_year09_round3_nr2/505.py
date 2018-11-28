#include <iostream>
#include <cmath>

using namespace std;

int n,t;
int flies[510][6];
double mint, maxt,curt,lt,rt,x,y,z,vx,vy,vz;
int X,Y,Z,VX,VY,VZ;


double sqr(double a) {
    return a * a;
}

double dist(double t) {
    return sqr(x + vx * t) + sqr(y + vy * t) + sqr(z + vz * t);
}

double tS(double levo, double desno){
    double lt,dt;
    if (desno-levo < 0.0000001) return (levo+desno)/2;
    lt = (levo*2+desno)/3;
    dt = (levo+desno*2)/3;
//     cout << levo << " " << desno << endl;
//     cout << 0 << lt << " " << dt << endl;
    if (dist(lt) > dist(dt))
        return tS(lt, desno);
    else
        return tS(levo, dt);
}




int main(){
  
 scanf("%d", &t);
 
 for(int zz = 0;zz<t;zz++){
   
   scanf("%d", &n);
   
   x = y = z = vx = vy = vz = 0;
   
   for(int zu=0;zu<n;zu++){
     scanf("%d %d %d %d %d %d", &X, &Y, &Z, &VX, &VY, &VZ);
     x += (double)X;
     y += (double)Y;
     z += (double)Z;
     vx += (double)VX;
     vy += (double)VY;
     vz += (double)VZ;
   }
   x /= n;
   y /= n;
   z /= n;
   vx /= n;
   vy /= n;
   vz /= n;
   
  

   //find max
   mint = 0.0;
   maxt = 1.0;
   curt = maxt*2;
   while(true){
      if(dist(curt*2) < dist(curt)){
	maxt = curt;
	curt *= 2;
      } else {
	maxt = curt*2;
	break;
      }
   }
   
  curt = tS(mint,maxt);
  

   
   
   printf("Case #%d: %0.7lf %0.7lf\n", zz+1, sqrt(dist(curt)), curt);
  // cout << dist(6) << endl;
   
   
 }
  
 return 0;
}