#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t,c,d,i,j;
    freopen("GBL.in","r",stdin);
    freopen("GBL.out","w",stdout);
    scanf("%d",&t);
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d%d",&c,&d);
        vector<pair<int,int> >v;
        v.clear();
        for(i=0;i<c;i++)
        {
            int a,b;
            scanf("%d%d",&a,&b);
            v.push_back(make_pair(a,b));
            //printf("%d %d\n",v[i].first,v[i].second);
        }
        sort(v.begin(),v.end());
        vector<double>l,r,lm,rm;
        for(i=0;i<c;i++)
        {
            double p=v[i].first,n=v[i].second;
            //printf("%f,%f\n",p,n);
            l.push_back(p-(n-1)*d/2.0);
            lm.push_back((n-1)*d/2.0);
            r.push_back(p+(n-1)*d/2.0);
            rm.push_back((n-1)*d/2.0);
            //printf("%f,%f,%f,%f\n",l[i],r[i],lm[i],rm[i]);
        }
        while(1)
        {
            bool ok=1;
            int n=l.size();
            for(i=0;i<n-1;i++)
            {
                if(l[i+1]-r[i]<d)
                {
                    ok=0;
                    double tl,tr,tlm,trm;
                    if(lm[i]>=lm[i+1]&&rm[i]>=rm[i+1])
                    {
                        tr=r[i+1]+r[i]+d-l[i+1];
                        trm=rm[i+1]+r[i]+d-l[i+1];
                        tl=l[i];
                        tlm=lm[i];
                        if(trm>rm[i])
                        {
                            double tem=(trm+tlm)/2;
                            tl-=tem-tlm;
                            tr-=trm-tem;
                            tlm=trm=tem;
                        }
                        else
                        {
                            trm=rm[i];
                        }
                    }
                    else
                    {
                        tr=r[i+1];
                        trm=rm[i+1];
                        tl=l[i]+l[i+1]-r[i]-d;
                        tlm=lm[i]+r[i]+d-l[i+1];
                        if(tlm>lm[i+1])
                        {
                            double tem=(trm+tlm)/2;
                            tl+=tlm-tem;
                            tr+=tem-trm;
                            tlm=trm=tem;
                        }
                        else
                        {
                            tlm=lm[i+1];
                        }
                    }
                    l[i]=tl;r[i]=tr;lm[i]=tlm;rm[i]=trm;
                    //printf("%f %f %f %f\n",tl,tr,tlm,trm);
                    l.erase(l.begin()+i+1);r.erase(r.begin()+i+1);lm.erase(lm.begin()+i+1);rm.erase(rm.begin()+i+1);
                    n--;
                }
            }
            if(ok)break;
        }
        double flm=0,frm=0;
        for(i=0;i<l.size();i++)
        {
            //printf("%f,%f\n",l[i],r[i]);
            flm=max(flm,lm[i]);
            frm=max(frm,rm[i]);
        }
        printf("Case #%d: %f\n",cn,(flm+frm)/2);
    }
    return 0;
}
