#include<iostream>
#include<math.h>
#include<stdio.h>
#define E 0.00000000
using namespace std;

int x,n;
double f,R,t,r,g,i,j,k,l,p,q,rr,s,luastotal,luas,jaraktemp,sudut,keliling;
double simpen;
double coba;

double jarak(double ay, double ax, double by, double bx) {
	return double(sqrt((by-ay)*(by-ay)+(bx-ax)*(bx-ax)));
}

int main() {
	freopen("raket.out","w",stdout);
	cin>>n;
	coba=0.000;
	for(x=1;x<=n;x++) {
		cout<<"Case #"<<x<<": ";
		cin>>f>>R>>t>>r>>g;
		luastotal=2*acos(0.000)*(R)*(R);
		t+=f;
		r+=f;
		g-=2*f;
		R-=t;
		luas=0.000;
		j=r;
		for(i=r;;i+=(g+2.000*r)) {
			//cout<<"i: "<<i<<endl;
			//cout<<"i,j,R: "<<i<<" "<<j<<" "<<R<<endl;
			if(i*i+r*r>=R*R) break;
			//if(i+g+2.000*r>=R) break;
			for(j=r;i*i+j*j<R*R;j+=(g+2.000*r)) {
				if(i*i+j*j>=R*R) continue;
				k=i+g;
				l=j+g;
				p=k;
				q=l;
				if((i*i+l*l<=R*R)&&(k*k+j*j<=R*R)&&(p*p+q*q<=R*R)) {
					if(g<0) continue;
					simpen=(g*g);
					if(simpen+E>0) luas+=(g*g);
				}
				else {
					p=k;
					q=l;
					if((i*i+l*l>=R*R)&&(k*k+j*j>=R*R)&&(p*p+q*q>R*R)) {
						l=sqrt(R*R-i*i);
						k=sqrt(R*R-j*j);
						simpen=((k-i)*(l-j)/2.000);
						if(k-i<0) continue;
						if(l-j<0) continue;
						if(simpen+E>0) luas+=((k-i)*(l-j)/2.000);
						jaraktemp=jarak(i,l,k,j);
						keliling=jaraktemp+2*R;
						keliling/=2.000;
						sudut=asin(jaraktemp/(2.000*R));
						sudut*=2.000;
						simpen=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));						
						if(simpen+E>0) luas+=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
					}
					else if((i*i+l*l>=R*R)&&(p*p+q*q>R*R)&&(k*k+j*j<R*R)) {
						l=sqrt(R*R-i*i);
						q=sqrt(R*R-p*p);
						simpen=((l-j)+(q-j))*(k-i)/2.000;
						//if(l-j<0) continue;
						//if(q-j<0) continue;
						//if(k-i<0) continue;
						/*if(simpen>0)*/ luas+=((l-j)+(q-j))*(k-i)/2.000;
						jaraktemp=jarak(i,l,p,q);
						keliling=jaraktemp+2.000*R;
						keliling/=2.000;
						sudut=asin(jaraktemp/(2.000*R));
						sudut*=2.000;
						simpen=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
						/*if(simpen>0)*/ luas+=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
					}
					else if((p*p+q*q>R*R)&&(k*k+j*j>=R*R)&&(i*i+l*l<R*R)) {
						p=sqrt(R*R-q*q);
						k=sqrt(R*R-j*j);
						simpen=((k-i)+(p-i))*(l-j)/2.000;
						//if(k-i<0) continue;
						//if(p-i<0) continue;
						//if(l-j<0) continue;
						/*if(simpen>0)*/ luas+=((k-i)+(p-i))*(l-j)/2.000;
						jaraktemp=jarak(k,j,p,q);
						keliling=jaraktemp+2.000*R;
						keliling/=2.000;
						sudut=asin(jaraktemp/(2.000*R));
						sudut*=2.000;
						simpen=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
						if(simpen+E>0) luas+=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
					}
					else if((p*p+q*q)>=R*R) {
						rr=k;
						s=l;
						p=sqrt(R*R-q*q);
						s=sqrt(R*R-rr*rr);
						simpen=((p-i)+(rr-i))*(l-s)/2.000;
						simpen+=(s-j)*(k-i);
						//if(simpen>0) {
							luas+=simpen;
						//}
						jaraktemp=jarak(rr,s,p,q);
						keliling=jaraktemp+2.000*R;
						keliling/=2.000;
						sudut=asin(jaraktemp/(2.000*R));
						sudut*=2.000;
						simpen=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
						if(simpen+E>0) luas+=(sudut*R*R/2.000)-(sqrt(keliling*(keliling-R)*(keliling-R)*(keliling-jaraktemp)));
					}
				}
			}
			//if(4*luas>luastotal) cout<<"gagal saat i: "<<i<<endl;
		}
		//cout<<"luastotal: "<<luastotal<<endl;
		//cout<<"luas slamet: "<<luas<<endl;
		printf("%.6llf\n",double(1.000-(4*luas/luastotal)));
		coba+=double(1.000-(4*luas/luastotal));
		//getchar();
	}
	//printf("%.6lf\n",coba);
	fclose(stdout);
	//printf("%.6lf\n",coba);
}
