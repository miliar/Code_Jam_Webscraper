#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<cmath>
#include<algorithm>

#define PI 3.14159265358979323

using namespace std;


long double integral(long double a,long double b,long double c)
{
  long double t1=asin(a/c);
  long double t2=asin(b/c);  
  return c*c*(t2-t1+(sin(2*t2)-sin(2*t1))/2.000)/2.000;
}

int main()
{
 int n;
 cin>>n;
 for(int i=0;i<n;i++)
 {
 
 cout<<"Case #"<<i+1<<": ";
 
 long double good=0.0;
 
 long double good2=0.0;
 
 long double f,R,t,r,g ;
 cin>>f>>R>>t>>r>>g;
 long double posx=r+g;
 long double posy=r+g;
 
 int nosquares=0;
 
 while(posx-g<=R-t)
 {
                
   posy=r+g; 
              
   while(posy-g<=R-t)
   {  
                  
     if((posx)*(posx)+(posy)*(posy)<=(R-t)*(R-t))          
         nosquares++;                    
     else if((posx-g+f)*(posx-g+f)+(posy-g+f)*(posy-g+f)<=(R-t-f)*(R-t-f))
     {
     
       //El punto de entrada es cuatro   
       if((R-t)*(R-t)-(posx-g)*(posx-g)<posy*posy)
       {
                                                  
      // cout<<"el punto de entrada es cuatro"<<endl;     
        //El punto de salida es 2
        if((R-t)*(R-t)-(posy-g)*(posy-g)<posx*posx)
        {
        //   cout<<"el punto de salida es dos"<<endl;
           long double x1=posx-g;
           long double x2=sqrt((R-t)*(R-t)-(posy-g)*(posy-g));
           long double y1=sqrt((R-t)*(R-t)-x1*x1);
           long double y2=posy-g;       
           
           
           long double y2p=y2+f;
           long double x2p=sqrt((R-t-f)*(R-t-f)-y2p*y2p);
           
           long double x1p=x1+f;
           long double y1p=sqrt((R-t-f)*(R-t-f)-x1p*x1p);
           
           if(x2p>=x1p 
             &&y1p>=y2p)
           {
              good2+=integral(x1p,x2p,(R-t-f))-(y2p)*(x2p-x1p);                         
           }                                    
        }
        //El punto de salida es 5
        else
        {
          // cout<<"el punto de salida es cinco"<<endl;
           long double x1p=posx-g+f;
           long double x2p=posx-f;

           
           long double y1p=sqrt((R-t-f)*(R-t-f)-x1p*x1p);
           long double y2p=sqrt((R-t-f)*(R-t-f)-x2p*x2p);
           
               
           if(y1p>=y2p&&y2p>=(posy-g)+f&&x2p-x1p>=0)
           {
              good2+=integral(x1p,x2p,(R-t-f))-(y2p)*(x2p-x1p);                         
           }
           else
           {
              long double x2p=sqrt((R-t-f)*(R-t-f)-(posy-g+f)*(posy-g+f));
              if(y1p>=(posy-g+f)&&x2p>=x1p)
               good2+=integral(x1p,x2p,(R-t-f))-((posy-g+f))*(x2p-x1p);                         
           }
           if(y2p>=(posy-g)+f&&x2p-x1p>=0)
           {
              good2+=(x2p-x1p)*(y2p-(posy-g)-f);                         
           }                     
        }
       }
       //El punto de entrada es tres
       else
       {
      //  cout<<"el punto de entrada es tres"<<endl;
        //El punto de salida es 2
        if((R-t)*(R-t)-(posy-g)*(posy-g)<posx*posx)
        {
           long double x1=sqrt((R-t)*(R-t)-posy*posy);
           long double x2=sqrt((R-t)*(R-t)-(posy-g)*(posy-g));
           long double y1=posy;
           long double y2=posy-g;  
           
           
           
           
           long double y2p=y2+f;
           long double x2p=sqrt((R-t-f)*(R-t-f)-y2p*y2p);
           
           
           long double y1p=y1-f;
           long double x1p=sqrt((R-t-f)*(R-t-f)-y1p*y1p);
                
           if(x2p>=x1p&&x1p>=posx-g+f&&y1-y2>=2*f)
           {

              good2+=integral(x1p,x2p,(R-t-f))-(y2+f)*(x2p-x1p);                         
           }
           else if(x2p>=posx-g+f&&y1-y2>=2*f)
           {
             y1p=sqrt((R-t-f)*(R-t-f)-(posx-g+f)*(posx-g+f));
             good2+=integral(posx-g+f,x2p,(R-t-f))-(y2+f)*(x2p-(posx-g+f));                            
           }
           
                     
           if(x1p-(posx-g)>=f&&y1-y2>=2*f)
           {
              good2+=(y1-y2-2*f)*(x1p-(posx-g)-f);                         
           }                                             
        }
        //El punto de salida es 5
        else
        {
       //    cout<<"el punto de salida es 5"<<endl;
           long double x1=sqrt((R-t)*(R-t)-posy*posy);
           long double x2=posx;
           long double y1=posy;
           long double y2=sqrt((R-t)*(R-t)-posx*posx);   
           
           long double y1p=posy-f;
           long double x1p=sqrt((R-t-f)*(R-t-f)-y1p*y1p);
           
           long double x2p=posx-f;
           long double y2p=sqrt((R-t-f)*(R-t-f)-x2p*x2p);
           
           
           
           
           
           if(x2p-x1p>=0&&x1p>=posx-g+f&&y1p>=y2p&&y2p>=posy-g+f)
           {
                                                                 
            //cout<<"Rara 1"<<endl;
              good2+=integral(x1p,x2p,(R-t-f))-(y2p)*(x2p-x1p);                         
               if(x1p-(posx-g)>=f&&y1p-y2p>=0)
                   {
                      good2+=(y1p-y2p)*(x1p-(posx-g)-f);                         
                   }                
        
                   if(x2p-x1p>=0&&y2p-(posy-g)>=f)
                   {
                      good2+=(y2p-(posy-g)-f)*(x2p-x1p);                         
                   }  
                                  
                   if(x1p-(posx-g)>=f&&y2p-(posy-g)>=f)
                   {
                      good2+=(y2p-(posy-g)-f)*(x1p-(posx-g)-f);                         
                   }                                            

           }
           else if(x1p<=posx-g+f&&y2p<=posy-g+f)
           {
            // cout<<"Rara 2"<<endl;
              x2p=sqrt((R-t-f)*(R-t-f)-(posy-g+f)*(posy-g+f));
              y1p=sqrt((R-t-f)*(R-t-f)-(posx-g+f)*(posx-g+f));
              if(x2p>=(posx-g+f)&&y2p>=(posy-g+f))   
                 good2+=integral(posx-g+f,x2p,(R-t-f))-(posy-g+f)*(x2p-(posx-g)-f);                                         
           }
           else if(x1p<=posx-g+f)
           {
            // cout<<"Rara 3"<<endl;                
              y1p=sqrt((R-t-f)*(R-t-f)-(posx-g+f)*(posx-g+f));   
              if(y1p>=y2p)
                good2+=integral(posx-g+f,x2p,(R-t-f))-(y2p)*(x2p-(posx-g)-f);
              good2+=(x2p-(posx-g)-f)*(y2p-(posy-g)-f);                                        
           }
           else if(y2p<=posy-g+f)
           {
             //cout<<"Rara 4"<<endl;                
              x2p=sqrt((R-t-f)*(R-t-f)-(posy-g+f)*(posy-g+f));
              if(x2p>=x1p)
                 good2+=integral(x1p,x2p,(R-t-f))-(posy-g+f)*(x2p-x1p); 
               good2+=(x1p-(posx-g)-f)*(y1p-(posy-g)-f);                                        
           }
           //Puede que al quitar r de radio, pasen a tener interseccion
           //con los otros lados, pero es a la vez
         }
       }     
     }
     else
        break;
     posy+=2*r+g;
   }
   posx+=2*r+g;
 }
 
 //cout<<"squaresizerelative "<<4.00000*max((g*g-4*f*g+4*f*f),(long double)0.00)/(PI*R*R)<<endl;
 //cout<<"nosquares: "<<nosquares<<endl;
 good=nosquares*max((g*g-4*f*g+4*f*f),(long double)0.00)+good2;
 
 
 cout.setf(ios::fixed);
 cout.precision(6);
 cout<< 1-(4.00000*good)/(PI*R*R)<<endl;
 
 
 }
}
