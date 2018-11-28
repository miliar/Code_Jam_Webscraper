#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

char sch[110][110];
long double WP[110][110],OWP[110],OOWP[110],RPI[110];

int main(){
   int t,n;
   cin>>t;
   for (int z=0; z<t; z++){
       cin>>n;
       for (int y=0; y<n;y++)
           for (int x=0; x<n;x++)
               cin>>sch[y][x];
       for (int y=0; y<n;y++){
           long double wp=0,c=0;
           for (int x=0; x<n;x++){
               if (sch[y][x]=='1')
                   wp++;
               if (sch[y][x]=='1' || sch[y][x]=='0')
                   c++;
           }
           for (int i=0; i<n;i++){
               if (sch[y][i]=='1'){
                   wp--;
                   c--;
                   WP[y][i]=wp/c;
                   wp++;
                   c++;
               }
               else if (sch[y][i]=='0'){
                   c--; 
                   WP[y][i]=wp/c;
                   c++;
               }
               else
                   WP[y][i]=wp/c;
           }
       }
       for (int y=0; y<n;y++){
           long double owp=0,c=0;
           for (int x=0; x<n;x++){
               if (sch[y][x]!='.' && x!=y){
                   owp+=WP[x][y];
                   c++;
               }
           }
           if (c>0)
               OWP[y]=owp/c;
           else
               OWP[y]=0;
       }
       //cout<<"1";
       for (int y=0; y<n;y++){
           long double oowp=0,c=0;
           for (int x=0; x<n;x++){
               if (sch[y][x]!='.'){
                   oowp+=OWP[x];
                   c++;
               }
           }
           if (c>0)
               OOWP[y]=oowp/c;
           else
               OOWP[y]=0;
       }
       for (int y=0; y<n;y++)
           RPI[y] = WP[y][y]/4.0 +  OWP[y]/2.0 + OOWP[y]/4.0;
       printf("Case #%d:\n",z+1);
       /*for (int y=0; y<n;y++)
       for (int x=0; x<n;x++)
         cout<<WP[y][x]<<" "<<OWP[y]<<" "<<OOWP[y]/4.0<<endl;*/
       for (int y=0; y<n;y++)
          cout<<setprecision(12)<<RPI[y]<<endl;
       }
}
       
