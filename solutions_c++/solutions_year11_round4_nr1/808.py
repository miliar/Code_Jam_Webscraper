#include<stdio.h>

int main() {
    double b1[3000],e1[3000],_pos,_rs,_t,_t0,_t1,_t1a,tt,w1[3000];
    int _cnt,_e,b[2000],cnt,e[2000],i,j,k,n,r,rs,s,t,t1,temp,w[2000],x;
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    scanf("%d",&t1);
    for(cnt=1;cnt<=t1;cnt++) {
        scanf("%d %d %d %d %d",&x,&s,&r,&t,&n);
        for(i=0;i<n;i++)scanf("%d %d %d",&b[i],&e[i],&w[i]);
        //sort by location
        for(i=0;i<n;i++) {
            for(j=n-1;j>i;j--) {
                if(b[j]<b[i]) {
                    temp=b[i];b[i]=b[j];b[j]=temp;
                    temp=e[i];e[i]=e[j];e[j]=temp;
                    temp=w[i];w[i]=w[j];w[j]=temp;
                }
            }
        }
        //get walkway parts
        _cnt=0;_e=0;b1[0]=0;
        for(i=0;i<n;i++) {
            if(b[i]>_e) {
                b1[_cnt]=_e;e1[_cnt]=b[i];w1[_cnt]=s;
                _cnt++;
            }
            b1[_cnt]=b[i];e1[_cnt]=e[i];w1[_cnt]=w[i]+s;
            _cnt++;
            _e=e[i];
        }
        if(_e<x) {
            b1[_cnt]=_e;e1[_cnt]=x;w1[_cnt]=s;
            _cnt++;
        }
        //sort by walking speed
        for(i=0;i<_cnt;i++) {
            for(j=_cnt-1;j>i;j--) {
                if(w1[j]<w1[i]) {
                    temp=b1[i];b1[i]=b1[j];b1[j]=temp;
                    temp=e1[i];e1[i]=e1[j];e1[j]=temp;
                    temp=w1[i];w1[i]=w1[j];w1[j]=temp;
                }
            }
        }
        //simulate
        rs=r-s;tt=0.0;_rs=rs;_t=t;
        for(i=0;i<_cnt;i++) {
            //time when not running
            _t0=(e1[i]-b1[i])/w1[i];
            //time when running
            if(tt>_t)_t1=_t0; //can no longer run
            else {
                _t1=(e1[i]-b1[i])/(w1[i]+_rs); //run
                if((tt+_t1)>_t) { //exhausted, partial run
                    _t1a=_t-tt;
                    _pos=b1[i]+(_t1a*(w1[i]+_rs));
                    _t1=_t1a+((e1[i]-_pos)/w1[i]);
                }
            }
            tt+=_t1;
        }
        printf("Case #%d: %.9f\n",cnt,tt);
    }
    return 0;
}
