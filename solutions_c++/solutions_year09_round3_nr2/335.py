#include<iostream>
#include<conio.h>
#include<vector>
#include<map>
#include<algorithm>
#include<string>
#include<math.h>
#define max 1000

using namespace std;

int n;
int x[max],y[max],z[max];
int vx[max],vy[max],vz[max];
double tx,ty,tz,tvx,tvy,tvz;

int main(void){

	
	freopen("c.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int cases,c;

	cin>>cases;

	for(c=0;c<cases;c++){
		int i,j;

		cin>>n;
		//cout<<n<<endl;

		tx=0,ty=0,tz=0,tvx=0,tvy=0,tvz=0;
		for(i=0;i<n;i++){
			cin>>x[i];
			cin>>y[i];
			cin>>z[i];
			cin>>vx[i];
			cin>>vy[i];
			cin>>vz[i];
		}
		for(i=0;i<n;i++){
			tx+=x[i];
			ty+=y[i];
			tz+=z[i];
			tvx+=vx[i];
			tvy+=vy[i];
			tvz+=vz[i];
		}
		tx/=n;
		ty/=n;
		tz/=n;
	    tvx/=n;
		tvy/=n;
		tvz/=n;

		double t;
		if((tvx*tvx + tvy*tvy+ tvz*tvz)==0)
			t=0;
		else
		 t=-(tx*tvx+ ty*tvy + tz*tvz)/(tvx*tvx + tvy*tvy+ tvz*tvz);
		
		if(t<=0)
			t=0;
		double ans=sqrt( (tx+tvx*t)*(tx+tvx*t)+(ty+tvy*t)*(ty+tvy*t)+(tz+tvz*t)*(tz+tvz*t));


	cout<<"Case #"<<c+1<<": ";
	cout<<fixed;
		cout<<ans<<" "<<t<<endl;
	}
	getch();
	return 0;
}