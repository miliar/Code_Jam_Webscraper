#include<stdio.h>
#include<math.h>

double Pi=3.14159265358979323846f;
double f,R,t,r,g,area;

double integral(double a, double b, double dolz) {
  // dolz represents the radius
  // we integrate from a to b
  double pom;
  pom=0.5*b*sqrt(dolz*dolz-b*b)-0.5*a*sqrt(dolz*dolz-a*a);  
  pom=pom+0.5*dolz*dolz*atan2(sqrt(1/(dolz*dolz-b*b))*b,1); 
  pom=pom-0.5*dolz*dolz*atan2(sqrt(1/(dolz*dolz-a*a))*a,1);
  
  return pom;
}

double rast(double a, double b, double c, double d) {
  double pom;
  
  pom=sqrt((c-a)*(c-a)+(d-b)*(d-b));
  return pom;
}

double min(double a, double b) {
  if (a<b) {
    return a;
  } else {
    return b;
  }
}

double max(double a, double b) {
  if (a>b) {
    return a;
  } else {
    return b;
  }
}

int main() {
    
  int i,j,k,total;
  // coordinates of the vertex
  double ax,ay,maxi,mini,pom,sarea;
  double pa,pb,pc,ia,ib,prob,dia,nr,ng;
  
  FILE *fi,*fo;
  fi=fopen("input3.txt","r+");
  fo=fopen("output3.txt","w+");
  
  fscanf(fi,"%d",&total);
  
  for (k=0;k<total;k++) {
    // reading part
      
    fscanf(fi,"%lf%lf%lf%lf%lf",&f,&R,&t,&r,&g);
    area=0;
    
    // first some conditions need to be true
    if (g>2*f) {
      // we do this to eliminate working with
      
      nr=r+f; 
      ng=g-2*f;
      sarea=ng*ng;      
      
      ax=0-g-2*r;
      while (ax<R) {
        ax=ax+g+2*r;
        ay=0;
        
        ay=0-g-2*r;
        while (ay<R) {
          ay=ay+g+2*r;
          // check here
          ////////////////////
      
          mini=rast(ax+nr,ay+nr,0,0);
          maxi=rast(ax+nr+ng,ay+nr+ng,0,0);
      
          if ((R-t)>=maxi) {
            // this means that the square is fully inside
            area=area+sarea;
         
          } else {
            if ((R-t)<=mini) {
              // this means that the square is fully ouside
             
            } else {
              // dia is a var name for the "imagined" radius       
              dia=R-t-f;
          
              // this means that the sphere cuts the square
              if (dia<=rast(ax+nr,ay+nr,0,0)) {
                // this means that nothing should be added
                
              } else {
                     
                // this means that there should be made some
                // complex maths calculations
                
                // let's find A first
                pa=rast(ax+nr,ay+nr,0,0);
                pb=rast(ax+nr,ay+nr+ng,0,0);
            
                
            
                if ((dia>=pa)&&(dia<=pb)) {
                  ia=ax+nr;
               
                } else {
                  // this is not checked whether it's correct
                  ia=sqrt(dia*dia-(ay+nr+ng)*(ay+nr+ng));
                  area=area+(ia-(ax+nr))*ng;
                  
                }
            
                // now let's find B similary
                pa=rast(ax+nr+ng,ay+nr,0,0);
                pb=rast(ax+nr+ng,ay+nr+ng,0,0);
            
                if ((dia>=pa)&&(dia<=pb)) {
                  ib=ax+nr+ng;
                } else {
                  ib=sqrt(dia*dia-(ay+nr)*(ay+nr));
                  
                }
                area=area+integral(ia,ib,dia)-(ay+nr)*(ib-ia);  
                
                
              }
          
            }
          }
          ////////////////////
        }
      }
    }
    
    prob=1-area/((Pi*R*R)/4);
    fprintf(fo,"Case #%d: %f\n",k+1,prob);
    
  }
  
  fclose(fi);
  fclose(fo);
  scanf("%d",&i);
  return 0;
}
