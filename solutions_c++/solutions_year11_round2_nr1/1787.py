#include <vector>
#include <set>
#include <deque>
#include <string>

using namespace std;

int ni() {
    int foo;
    scanf("%d", &foo);
    return foo;
}

char teamscores[128][128];

int main() {
   int c = ni();

   for(int i=0;i<c;i++) {
    
     double twp[128];
     int teamwins[128];
     int teamlosses[128];
     double owp[128];
     double oowp[128];
     
     printf("Case #%d: \n", i+1);

     int teams;
     scanf("%d", &teams);
     for(int j=0;j<teams;j++) {
       scanf("%s", teamscores[j]);
       int wins =0;
       int losses=0;
       teamwins[j] = 0;
       teamlosses[j] = 0;
       for(int k=0;k<teams;k++) {
         switch(teamscores[j][k]) {
         case '.':
           break;
         case '0':
           losses++;
           teamlosses[j]++;
           break;
         case '1':
           wins++;
           teamwins[j]++;
           break;
         default:
           break;
         }
        
       }
       twp[j] = wins / (wins + (double)losses);
       //printf("twp for team %d is %f\n", j, twp[j]);
     }
     
     for(int j=0;j<teams;j++){
  
       double sum = 0.0;
       int count = 0;
       
       for(int k=0;k<teams;k++) {
         if(j==k) continue;
         switch(teamscores[j][k]) {
         case '.':
           break;
         case '0':
           count++;
           sum += (teamwins[k] - 1) / (double)(teamlosses[k] + (teamwins[k] -1));
           //printf("Team %d had %d wins and %d losses exempting team %d\n", k,  teamwins[k] - 1, teamlosses[k], j);
           break;
         case '1':
           count++;
           sum += teamwins[k] / (double)((teamlosses[k] - 1) + teamwins[k]);
           //printf("Team %d had %d wins and %d losses exempting team %d\n", k,  teamwins[k], teamlosses[k]-1, j);
           break;
         default:
           break;
         }
       }
       owp[j] = sum / count;
       //printf("owp for team %d is %f with sum %f and count %d\n", j, owp[j], sum, count);
     }
       

     for(int j=0;j<teams;j++) {
       double sum = 0.0;
       int count = 0;
       
       for(int k=0;k<teams;k++) {
         switch(teamscores[j][k]) {
         case '.':
           break;
         case '0':
         case '1':
           count++;
           sum += owp[k];
           break;
         default:
           break;
         }
       }
       oowp[j] = sum / count;
       //printf("oowp for team %d is %f\n", j, oowp[j]);
     }
 
     for(int j=0;j<teams;j++) {
       printf("%.8f\n", 0.25 * twp[j] + 0.50 * owp[j] + 0.25 * oowp[j]);
     }
   
   }
}

