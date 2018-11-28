#include<stdio.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{

    FILE *fp=fopen("B-small-attempt2.in", "r"), *ofp=fopen("B-small-attempt2.op.txt", "w");
     int T,i,S ,N, p,r,max,count,temp;




       fscanf(fp, "%d", &T);



       for(int tc=1;tc<=T;tc++)
       {
           count=0;
               fscanf(fp,"%d%d%d",&N,&S,&p );

                cout<<"N"<<N<<endl;
                cout<<"P"<<p<<endl;
                cout<<"S"<<S<<endl;
                vector<int> g;
               for(i=0;i<N;i++)
               {
                   fscanf(fp,"%d",&temp);
                   g.push_back(temp);
                   cout<<g[i];
               }
               cout<<endl;
                sort(g.begin(),g.end());
                for(i=N-1;i>=0;i--)
                {
                    max=g[i]/3; r=g[i]%3;
                    if(max-p>=0)
                    {
                        count++;
                    }
                    else
                    {


                   switch(r)
                   {
                       case 1:{
                                if(abs(max-p)<=1&&g[i]!=1)
                                {cout<<"Case 1"<<count<<endl;
                                count++;
                                }
                                break;
                                }
                       case 2:{
                                    if(abs(max-p)<=1&&g[i]!=2)
                                {
                                     cout<<"Case 2"<<count<<endl;
                                    count++;

                                }
                                else if(g[i]!=2)
                                {
                                    if(abs(max-p)<=2)
                                    {
                                        if(S>0)
                                        {
                                            cout<<"Case 2.2"<<count<<endl;
                                            count++;
                                            S--;
                                        }
                                    }
                                }
                                break;
                                }

                       case 0:{
                            if(abs(max-p)<=1&&g[i]!=0)
                                {
                                    if(S>0)
                                    {

                                    cout<<"Case 0.1"<<count<<endl;
                                    count++;
                                    S--;
                                    }


                                }
                               break;
                                }
                   };

                }
                }

    cout<<"S"<<S<<endl;
               // print cases

               fprintf(ofp, "Case #%d: %d\n", tc, count);

       }
       return 0;
}
