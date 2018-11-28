#include <iostream>
#include <vector>
#include <cassert>
#include <map>
#include <string>
#include <queue>
#define D 0
using namespace std;
typedef map<string,int> MSI;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef priority_queue<PII> PQPII;
typedef pair<int,PII> PIPII;
typedef priority_queue<PIPII , vector<PIPII>, greater<PIPII> > PQPIPII;
typedef vector<PII> VPII;
typedef vector<VI> VVI;

class Tripple{
public:
	int start(){
		return a;
	}
	int end(){
		return b;
	}
	int direction(){
		return dir;
	}
	int duration(){
		return b-a;
	}
	Tripple(int aa,int bb,int ddir):a(aa),b(bb),dir(ddir){
		assert(bb>aa);
		assert(ddir==0 || ddir==1);
		a=aa;
		b=bb;
		dir=ddir;
	}
	~Tripple(){}
private:
	int a,b,dir;
};

int main(){
	int N;
	cin >> N;
	for(int ii=1;ii<=N;ii++){
		int ab,ba,n,A=0,B=0;
		cin >> n>>ab>>ba;
		VPII vab,vba,abfahrten,ankuenfte,vabr,vbar;
		VVI alle_fahrten;
		for(int i=0;i<ab;i++){
			int a,b,c,d;
			assert(4==scanf("%d:%d %d:%d",&a,&b,&c,&d));
			VI v(4);
			v[1]=-(a*60+b);
			v[0]=-(c*60+d+n);
			v[2]=0;
			PII p(a*60+b,c*60+d+n);
			PII q(c*60+d+n,a*60+b);
			vab.push_back(p);
			abfahrten.push_back(p);
			ankuenfte.push_back(q);
			vabr.push_back(q);
			alle_fahrten.push_back(v);
		}
		for(int i=0;i<ba;i++){
			int a,b,c,d;
			assert(4==scanf("%d:%d %d:%d",&a,&b,&c,&d));
			VI v(4);
			v[1]=-(a*60+b);
			v[0]=-(c*60+d+n);
			v[2]=1;
			PII p(a*60+b,c*60+d+n);
			PII q(c*60+d+n,a*60+b);
			vba.push_back(p);
			abfahrten.push_back(p);
			ankuenfte.push_back(q);
			vba.push_back(q);
			alle_fahrten.push_back(v);
		}
		sort(vab.begin(),vab.end());
		sort(vba.begin(),vba.end());
		sort(vabr.begin(),vabr.end());
		sort(vbar.begin(),vbar.end());
		reverse(vabr.begin(),vabr.end());
		reverse(vbar.begin(),vbar.end());
		VI usedab(vab.size()),usedba( vba.size() );

		sort(alle_fahrten.begin(),alle_fahrten.end());
		
		for(int i=0;i<(int)alle_fahrten.size();i++){
			alle_fahrten[i][0]=-alle_fahrten[i][0];
			alle_fahrten[i][1]=-alle_fahrten[i][1];
		}
		for(int i=0;i<(int)alle_fahrten.size();i++){
if(D)			fprintf(stderr,"%d -> %d # %d %d\n",alle_fahrten[i][2],
					!alle_fahrten[i][2],alle_fahrten[i][1],
					alle_fahrten[i][0]);
		}
		
		int nn=ab+ba;
		while(nn){
			//for(int i=(int)alle_fahrten.size()-1;i>=0;i--){
			for(int i=0;i<(int)alle_fahrten.size();i++){
				if(!alle_fahrten[i][3]){
					int start=alle_fahrten[i][1],stopp=alle_fahrten[i][0];
					alle_fahrten[i][3]=1; // used!!
					nn--;
					int ca=alle_fahrten[i][2];
if(D)	fprintf(stderr,"ausgewaehtl: %d->%d # %d-%d\n",ca,!ca,start,stopp);
//					for(int j=(int)alle_fahrten.size()-1;j>=0;j--){
					for(int j=0;j<(int)alle_fahrten.size();j++){
						if(!ca==alle_fahrten[j][2]){
if(D)							fprintf(stderr,"ca: %d:%d\n",ca,j);
							if( !alle_fahrten[j][3]){
if(D)								fprintf(stderr,"ok: %d\n",j);
								if( alle_fahrten[j][0]<=start ){
									start=alle_fahrten[j][1];
									stopp=alle_fahrten[j][0];
									ca=!ca;
									alle_fahrten[j][3]=1; // used!!
									nn--;
								}
							}
						}	
					}
					if(ca) B++;
					else A++;
//					break; // ??
				}

			}
		}
		printf("Case #%d: %d %d\n",ii,A,B);
	}
	return 0;
}
