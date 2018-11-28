# include <iostream>
# include <stdio.h>
# include <string.h>
# include <algorithm>
# include <vector>
using namespace std;

struct df
    {
        int index,max;
        df()
            {
                index=0;
                max=0;
            }
        void init()
        {
            index=0;
            max=0;

        }
    }v_normal[105],v_surprising[105];
bool comp(struct df a1,struct df a2)
    {
        if(a1.max<=a2.max)
            return 0;
        else
            return 1;
    }
int main()
{
    //vector <struct df> v_normal(105,0),v_surprising(105,0);
    int s=0,p=0,t=0,n=0,i=0,j=0,a[105],l=0,k=0,normal[105][3],surprising[105][3];
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
                                normal[j][0]=0;
                            normal[j][1]=0;
                            normal[j][2]=0;
                            surprising[j][0]=0;
                            surprising[j][1]=0;
                            surprising[j][2]=0;
                            }
                            else {
                            normal[j][0]=a[j]/3;
                            normal[j][1]=a[j]/3;
                            normal[j][2]=a[j]/3;
                            surprising[j][0]=a[j]/3;
                            surprising[j][1]=a[j]/3 - 1;
                            surprising[j][2]=a[j]/3 + 1;}
                            v_normal[j].index=j;
                            v_surprising[j].index=j;
                            int max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(normal[j][k]>max)
                                        max=normal[j][k];
                                }
                            v_normal[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surprising[j][k]>max)
                                        max=surprising[j][k];
                                }

                            v_surprising[j].max=max;

                        }
                    else
                        if(a[j]%3==1)
                        {
                            if(a[j]==1)
                            {normal[j][0]=1;
                            normal[j][1]=0;
                            normal[j][2]=0;
                            surprising[j][0]=1;
                            surprising[j][1]=0;
                            surprising[j][2]=0;}
                            else {
                            normal[j][0]=a[j]/3+1;
                            normal[j][1]=a[j]/3;
                            normal[j][2]=a[j]/3;
                            surprising[j][0]=a[j]/3+1;
                            surprising[j][1]=a[j]/3-1;
                            surprising[j][2]=a[j]/3+1;}
                            v_normal[j].index=j;
                            v_surprising[j].index=j;
                            int max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(normal[j][k]>max)
                                        max=normal[j][k];
                                }
                            v_normal[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surprising[j][k]>max)
                                        max=surprising[j][k];
                                }

                            v_surprising[j].max=max;

                        }
                        else
                        if(a[j]%3==2)
                        {
                            normal[j][0]=a[j]/3;
                            normal[j][1]=a[j]/3+1;
                            normal[j][2]=a[j]/3+1;
                            surprising[j][0]=a[j]/3;
                            surprising[j][1]=a[j]/3;
                            surprising[j][2]=a[j]/3+2;
                            v_normal[j].index=j;
                            v_surprising[j].index=j;
                                    int max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(normal[j][k]>max)
                                        max=normal[j][k];
                                }
                            v_normal[j].max=max;
                            max=-1;
                            for(k=0;k<3;k++)
                                {
                                    if(surprising[j][k]>max)
                                        max=surprising[j][k];
                                }

                            v_surprising[j].max=max;

                        }

                }
//            cout<<"\nNormal\n";
//            for(int o=0;o<=n;o++)
//                {
//                    printf("%d:%d\n",o,v_normal[o].max);
//                }
//            cout<<"\nSurprising";
//            for(int o=0;o<=n;o++)
//                {
//                    printf("%d:%d\n",o,v_surprising[o].max);
//                }
////            sort(v_normal+1,v_normal+n-1,comp);
//            sort(v_normal+1,v_normal+n-1,comp);

            //sort(v_surprising.begin()+1,v_surprising.begin()+n-1,comp);
            //sort(v_surprising.begin()+1,v_surprising.begin()+n-1,comp);
            int sum=0,h=0,mn=0;
            vector <int> taken(105,0);
            for(l=1;l<=n;l++)
                {
                    if(mn>=s)
                            break;
                    if(v_surprising[l].max >=p && v_normal[l].max<p)
                        {sum+=1;taken[l]=1;mn++;

                        }
                }

            for(l=1;l<=n;l++)
                {

                    if(taken[l]!=1)
                        {

                            if(mn>=s)
                                    break;
                            if(v_surprising[l].max >=p)
                            {sum+=1;taken[l]=1;mn++;

                            }
                        }
                }
            for(l=1;l<=n;l++)
                {
                    if(taken[l]!=1)
                        {

                            if(v_normal[l].max>=p)
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
                    v_normal[h].init();
                    v_surprising[h].init();
                }
            sum=0;
        }

    return 0;
}
