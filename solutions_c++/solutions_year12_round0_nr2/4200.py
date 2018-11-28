#include <iostream>
#include <fstream>
#include <string.h>
#include <algorithm>
#define TI 100

using namespace std;

int main()
{
   fstream in,out;
   int t;

   in.open("dat.in",ios::in);
   out.open("out.in",ios::out);

   in>>t;cout<<"test cas "<<t<<"\n";

   for(int i=0; i<t ; i++)
   {
       int n,sur,p;
       int sum=0;
       in>>n;
       in>>sur;
       in>>p;

       int result = 0;
       int output=0;

       int best[100];
       int score[TI];
       int nscore[TI];
       int sscore[TI];
       memset(&score,'\0',TI);
       memset(&nscore,'\0',TI);
       memset(&sscore,'\0',TI);

       for(int j = 0;j<n;j++)
       {
            in>>score[j];
       }

       for(int s=0;s<n;s++)
       {
           int pos[10][3],poss[10][3];
           int y=0,z=0;
           int norm=0,surp=0;
           int ss[TI],ns[TI];
           memset(&ss,'\0',TI);
           memset(&ns,'\0',TI);
           int nsc=0,ssc=0;

           for(int a= 0; a <= 10 ; a++)
         {
           for(int b=0;b<=10;b++)
           {
               if(b>(a+2))
               continue;
               if(b<a-2)
               continue;
               for(int c=0;c<=10;c++)
               {
                   if(c>(b+2))
                   continue;
                   if(c>(a+2))
                   continue;
                   sum = a + b + c;
                   if((score[s]==sum)&&(c>=a))
                   {
                       int comp[] = {a,b,c};
                       int ma = *max_element(comp,comp+3);
                       int mi = *min_element(comp,comp+3);
                       if((ma-mi==0)||(ma-mi==1))
                       {
                           pos[z][0] = a;
                           pos[z][1] = b;
                           pos[z][2] = c;
                           int dum[3] = {a,b,c};
                           z++;
                           ns[nsc++] = *max_element(dum,dum+3);
                           cout<<"   possible norm "<<a<<" "<<b<<" "<<c<<"   "<<ns[nsc-1]<<"\n";
                       }
                       else if(ma-mi==2)
                       {
                           poss[y][0] = a;
                           poss[y][1] = b;
                           poss[y][2] = c;
                           int dum[3] = {a,b,c};
                           y++;
                           ss[ssc++] = *max_element(dum,dum+3);
                           cout<<"   possible surp "<<a<<" "<<b<<" "<<c<<"   "<<ss[ssc-1]<<"\n";
                       }
                       //cout<<"   possible "<<a<<" "<<b<<" "<<c<<"\n";
                   }

               }
           }
         }
            int count = (z>y)? z:y;
            for(int count2=0;count2<count;count2++)
            {
                if((pos[count][0]>=p)||(pos[count][1]>=p)||(pos[count][2]>=p))
                {
                    norm++;
                }
                if((poss[count][0]>=p)||(poss[count][1]>=p)||(poss[count][2]>=p))
                {
                    surp++;
                }
            }

            if(norm>0)
            result++;
            else if(sur>0)
            {
                if(surp>0)
                {
                    result++;cout<<"// "<<i<<"  "<<surp<<" "<<surp<<"\n";
                    surp--;
                }
            } cout<<"\n";

            nscore[s] = *max_element(ns,ns+nsc);
            sscore[s] = *max_element(ss,ss+ssc); cout<<" nscore "<<nscore[s]<<" sscore"<<sscore[s]<<"  s "<<s<<"\n";


       }

       if(sur>0)
       {
           for(int a=0;a<n;a++)
           {
               if(nscore[a]>=p)
               {
                   best[a]=nscore[a];
               }
               else if(nscore[a]>=sscore[a])
               {
                   best[a] = nscore[a];
               }
               else if((sur>0)&&(sscore[a]>=p))
               {
                   best[a] = sscore[a];
                   sur--;
               }
               else
               {
                   best[a] = nscore[a];
               }

               cout<<"                       best "<<best[a]<<"   nscore"<<nscore[a]<<"\n";
           }
       }
       else
       {
           for(int a=0;a<n;a++)
           {
               best[a] = nscore[a];
               cout<<"                       best "<<best[a]<<"\n";
           }
       }

       for(int a=0;a<n;a++)
       {
           if(best[a]>=p)
           output++;
       }



       cout<<"case :"<<i+1<<"  "<<output<<"\n";
       out<<"Case #"<<i+1<<": "<<output<<"\n";
   }
}
