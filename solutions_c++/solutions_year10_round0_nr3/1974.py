#include <iostream>
#include <fstream>
#define forn(i,n) for(int i=0; i<(int)(n); i++)
typedef long long tint;
using namespace std;

tint cp[2048];
tint ppg[1024];
tint proxg[1024];
tint us[1024];
tint res[1024];

int main(){
	ifstream in("gcjs.in");
	ofstream out("gcjsv2.out");
	
	tint T, n, k, r;
	in>>T;
	tint tc=1;
	
	while(tc<=T){
		in>>r>>k>>n;
		forn(i,n){in>>cp[i]; cp[i+n]=cp[i];}
		fill (us, us+n, 0);
		fill (res, res+n, 0);
		forn(i,n){
			tint count=0;
			tint j;
			for(j=i; j<i+n && count+cp[j]<=k; j++){
				count+=cp[j];
				}
			ppg[i]=count;
			proxg[i]=j%n;
			}
		/*
		forn(i,n)out<<ppg[i];
		out<<endl;
		forn(i,n)out<<proxg[i];
		out<<endl;
		*/
		tint pos=0;
		tint cnt=0;
		tint totp=0;
		res[0]=0;
		while(us[pos]==0){
			cnt++;
			us[pos]=cnt;
			totp+=ppg[pos];
			res[cnt]=totp;
			//posant=pos;
			pos=proxg[pos];
			}
		tint comciclo=pos;
		tint p1=0, p2=0, p3=0, r1=0, r2=0, r3=0;
		
		
		pos=0;
		while(pos!=comciclo){
			r1++;
			p1+=ppg[pos];
			pos=proxg[pos];			
			}
			//out<<p1<<" ";
			//out<<r1<<" ";

		pos=comciclo;
		while(proxg[pos]!=comciclo){
			r2++;
			p2+=ppg[pos];
			pos=proxg[pos];			
			}
			r2++;
			p2+=ppg[pos];
	//		out<<p2<<" ";
		//	out<<r2<<" ";

		r3=(r-r1)%r2;
		pos=comciclo;
		while(r3>0){
			p3+=ppg[pos];
			pos=proxg[pos];
			r3--;
			}
//			out<<p3<<" ";
//out<<r3<<" ";

			
			
		tint rr;
		
		rr=p1;
		 rr+=(p2*((r-r1)/r2));
		 rr+=p3;
		out<<"Case #"<<tc<<": ";
		out<<rr<<endl;
		tc++;
		}
	
	}	
