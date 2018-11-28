#include<cstdio>
#include<iostream>
#include<vector>
using namespace std;
     struct tt
       {
                int time;
                bool avail;
       };
bool cmp(struct tt a,struct tt b)
     {
                return a.time<b.time;
     }
                   
int main()
 {
          
          int N,T,NA,NB;
          scanf("%d",&N);
          int Case=1;
          while(N--)
           {
                    
                    vector<struct tt> Va1,Va2,Vb1,Vb2;
                    scanf("%d",&T);
                    scanf("%d%d",&NA,&NB);
                    int t1,t2,s1,s2;
                    struct tt t;
                    for(int i=0;i<NA;i++)
                      {
                            scanf("%d:%d %d:%d",&t1,&s1,&t2,&s2);
                            t.time=60*t1+s1;
                            t.avail=1;
                            Va1.push_back(t);
                            t.time=60*t2+s2+T;
                            t.avail=1;
                            Va2.push_back(t);
                      }
                     
                    for(int i=0;i<NB;i++)
                       {
                            scanf("%d:%d %d:%d",&t1,&s1,&t2,&s2);
                            t.time=60*t1+s1;
                            t.avail=1;
                            Vb2.push_back(t);
                            t.time=60*t2+s2+T;
                            t.avail=1;
                            Vb1.push_back(t);
                       }
                    sort(Va1.begin(),Va1.end(),cmp);
                    sort(Vb1.begin(),Vb1.end(),cmp);
                    sort(Va2.begin(),Va2.end(),cmp);
                    sort(Vb2.begin(),Vb2.end(),cmp);
                    
                    /*for(int i=0;i<NA;i++)
                     cout<<Va1[i].time<<" "<<Va1[i].avail<<endl;
                    for(int i=0;i<NB;i++)
                     cout<<Vb1[i].time<<" "<<Vb1[i].avail<<endl;*/
                   
                   int counta=0,countb=0;
                   int f;
                   for(int i=0;i<NA;i++)
                     {
                           f=1;
                           for(int j=0;j<NB;j++)
                            {
                                   if(Va1[i].time<Vb1[j].time)
                                    {
                                       counta++;
                                       f=0; 
                                       break;
                                    }
                                   else
                                   {
                                       if(Vb1[j].avail==true)
                                          {
                                              Vb1[j].avail=0;
                                              f=0;
                                              break;
                                          }
                                   }
                                 
                            }
                            if(f)
                            counta++;
                   }        
                      
                      
                  for(int i=0;i<NB;i++)
                     {
                           f=1;
                           for(int j=0;j<NA;j++)
                            {
                                   if(Vb2[i].time<Va2[j].time)
                                    {
                                       countb++;
                                       f=0; 
                                       break;
                                    }
                                   else
                                   {
                                       if(Va2[j].avail==true)
                                          {
                                              Va2[j].avail=0;
                                              f=0;
                                              break;
                                          }
                                   }
                                 
                            }
                            if(f)
                            countb++;
                   }                             
                  printf("Case #%d: %d %d\n",Case++,counta,countb);
           }
           
    }    
                                                 
