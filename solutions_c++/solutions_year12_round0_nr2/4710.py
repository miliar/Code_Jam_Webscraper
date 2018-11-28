# include <iostream>
# include <stdio.h>
# include <string.h>
# include <algorithm>
# include <vector>
using namespace std;

struct data
    {
        int index,max;
        data()
            {
                index=0;
                max=0;
            }
        void init()
        {
            index=0;
            max=0;

        }
    }v_norm[105],v_surp[105];
bool comp(struct data a1,struct data a2)
    {
        if(a1.max<=a2.max)
            return 0;
        else
            return 1;
    }
int main()
{
    int s=0,p=0,t=0,n=0,i=0,j=0,a[105],l=0,k=0,norm[105][3],surp[105][3];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
        {
            scanf("%d %d %d",&n,&s,&p);
            for(j=1;j<=n;j++)
                {
                    scanf("%d",&a[j]);
                    if(a[j]%3==0)
                        {
                    if(a[j]==0)
                       {
                        norm[j][0]=0;
                         norm[j][1]=0;
                        norm[j][2]=0;
                         surp[j][0]=0;
                         surp[j][1]=0;
                      surp[j][2]=0;
                            } else {
                           		 norm[j][0]=a[j]/3;
                          		  norm[j][1]=a[j]/3;
                          		  norm[j][2]=a[j]/3;
                           		 surp[j][0]=a[j]/3;
                          		 surp[j][1]=a[j]/3 - 1;
                           		 surp[j][2]=a[j]/3 + 1;}
                         		   v_norm[j].index=j;
                         		   v_surp[j].index=j;
                          		  int max=-1;
                        		    for(k=0;k<3;k++)
                                		{
                                	    if(norm[j][k]>max)
                               		         max=norm[j][k];
                           			     }
                            v_norm[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surp[j][k]>max)
                                        max=surp[j][k];
                                }

                            v_surp[j].max=max;

                        }
                    else
                        if(a[j]%3==1)
                        {
                            if(a[j]==1)
                            {norm[j][0]=1;
                            norm[j][1]=0;
                            norm[j][2]=0;
                            surp[j][0]=1;
                            surp[j][1]=0;
                            surp[j][2]=0;}
                            else {
                            norm[j][0]=a[j]/3+1;
                            norm[j][1]=a[j]/3;
                            norm[j][2]=a[j]/3;
                            surp[j][0]=a[j]/3+1;
                            surp[j][1]=a[j]/3-1;
                            surp[j][2]=a[j]/3+1;}
                            v_norm[j].index=j;
                            v_surp[j].index=j;
                            int max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(norm[j][k]>max)
                                        max=norm[j][k];
                                }
                            v_norm[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surp[j][k]>max)
                                        max=surp[j][k];
                                }

                            v_surp[j].max=max;

                        }
                        else
                        if(a[j]%3==2)
                        {
                            norm[j][0]=a[j]/3;
                            norm[j][1]=a[j]/3+1;
                            norm[j][2]=a[j]/3+1;
                            surp[j][0]=a[j]/3;
                            surp[j][1]=a[j]/3;
                            surp[j][2]=a[j]/3+2;
                            v_norm[j].index=j;
                            v_surp[j].index=j;
                                    int max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(norm[j][k]>max)
                                        max=norm[j][k];
                                }
                            v_norm[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surp[j][k]>max)
                                        max=surp[j][k];
                                }

                            v_surp[j].max=max;

                        }

                }

            int sum=0,h=0,mn=0;
            vector <int> taken(105,0);
            for(l=1;l<=n;l++)
                {
                    if(mn>=s)
                            break;
                    if(v_surp[l].max >=p && v_norm[l].max<p)
                        {sum+=1;taken[l]=1;mn++;

                        }
                }

            for(l=1;l<=n;l++)
                {

                    if(taken[l]!=1)
                        {

                            if(mn>=s)
                                    break;
                            if(v_surp[l].max >=p)
                            {sum+=1;taken[l]=1;mn++;

                            }
                        }
                }
            for(l=1;l<=n;l++)
                {
                    if(taken[l]!=1)
                        {

                            if(v_norm[l].max>=p)
                            {
                                taken[l]=1;sum+=1;
//                                if(mn==s)
//                                    break;
                            }
                        }
                }
            printf("Case #%d: %d\n",i,sum);
            for(h=0;h<=n;h++)
                {
                    v_norm[h].init();
                    v_surp[h].init();
                }
            sum=0;
        }

    return 0;
}
