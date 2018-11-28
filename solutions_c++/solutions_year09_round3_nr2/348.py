#include<iostream>
#include<cmath>
#include<string>
using namespace std;


int x,y,z,vx,vy,vz,n,t;
double a,b,c,va,vb,vc,mini;
long long p,q,r,vp,vq,vr;

int main() {
    cin >> t;
    for (int i=0;i<t;i++) {
        cin >> n;
        a=0;
        b=0;
        c=0;
        va=0;
        vb=0;
        vc=0;
        p=0;
        q=0;
        r=0;
        vp=0;
        vq=0;
        vr=0;
        for (int j=0;j<n;j++) {
            cin >> x >> y >> z >> vx >> vy >> vz;
            a+=x;
            b+=y;
            c+=z;
            va+=vx;
            vb+=vy;
            vc+=vz;
            p+=(long long)x;
            q+=(long long)y;
            r+=(long long)z;
            vp+=(long long)vx;
            vq+=(long long)vy;
            vr+=(long long)vz;            
        }
        long long tempa,tempb;
        tempa=p*vp+q*vq+r*vr;
        tempb=vp*vp+vq*vq+vr*vr;
        a=a/double(n);
        b=b/double(n);
        c=c/double(n);
        va=va/double(n);
        vb=vb/double(n);
        vc=vc/double(n);
        double time;
        /*mini=a*a+b*b+c*c;
        long time=0;
        bool flag=false;
        do {
            a+=va;
            b+=vb;
            c+=vc;   
            double temp;
            temp=a*a+b*b+c*c;
            if (temp<mini) {mini=temp;time++;}
            else {flag=true;};
        } while (!flag);*/
        if ((tempa==0) || (tempb==0)) {time=0;}
        else if ((tempa>0) && (tempb>0)) {time=0;}
        else if ((tempa<0) && (tempb<0)) {time=0;}
        else {time=-(a*va+b*vb+c*vc)/(va*va+vb*vb+vc*vc);};
        //cout << tempa << " " << tempb << " " << a*va+b*vb+c*vc << " " << va*va+vb*vb+vc*vc << " ";
        a+=time*va;
        b+=time*vb;
        c+=time*vc;
        mini=a*a+b*b+c*c;
        printf("Case #%ld: %.8lf %.8lf\n",i+1,sqrt(mini),time);
    }
    return 0;
}
