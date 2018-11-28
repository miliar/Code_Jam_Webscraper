#define wru 0
#include <cstdio> 
#include <cstdlib> 
#include <cstring> 
#include <cassert> 
#include <cmath> 
#include <vector> 
#include <string>
#include <fstream>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <iostream>

using namespace std; 

typedef double LD;
typedef long long LL;
typedef  vector<int> VI;
typedef  vector<string> VS;
ifstream inf ;
ofstream outf ;

/*template  */

#define FOR(i,a,b) for( int i=(a),_b=(b); i<=(_b); i++) 
#define FORD(i,a,b) for( int i=(a),_b=(b); i>=(_b); i--) 
#define FORIT(i,a,type) for(type::iterator i=((a).begin()); i<((a).end()); i++) 
#define bend(x) x.begin(),x.end()
#define SORT(x) sort(bend(x))
#define pf(a) outf<< #a <<" = " <<a <<endl;
#define clr(t) memset((t),0,sizeof(t))
#define mnn 71234
#define pi 3.141592653589793

int anw2;
vector <pair <int ,int> > w;
#define bad {printf("NO\n");return 0;}


			string ss[1200];
			int lenn[1200];
			int delta=3000;
			int minn[7000];
			int maxx[7000];
			int minn1[7000];
			int maxx1[7000];
			int imp=90000000;
			int mp=6500;
				int dx[100];
				int dy[100];
			void add(int x,int y){
				//cout<<x<<endl;
				//w.push_back()
				x=x+delta;
				if(minn[x]==imp) minn[x]=y;
				if(maxx[x]==imp) maxx[x]=y;
				if(minn[x]>y) minn[x]=y;
				if(maxx[x]<y) maxx[x]=y;
				return;
			}
			void add1(int x,int y){
				//cout<<x<<endl;
				x=x+delta;
				if(minn1[x]==imp) minn1[x]=y;
				if(maxx1[x]==imp) maxx1[x]=y;
				if(minn1[x]>y) minn1[x]=y;
				if(maxx1[x]<y) maxx1[x]=y;
				return;
			}
			void addd(int x1,int x2,int y){
				 anw2=anw2+(x2-x1)*y;
				return;
			}
			int iss(int x,int y){
				return  
					((minn[x+delta]<=y) &&(maxx[x+delta]>=y)) ||
					((minn1[y+delta]<=x) &&(maxx1[y+delta]>=x)) ;
			}
int main()
{

	ifstream inf("input.txt");
	ofstream outf("output.txt");
	int test;
	
	inf >>test;




	
	FOR(ii,1,test){
			int l;
				int anw=0;
			inf >>l;
			w.clear();
			FOR(i,1,l) inf >>ss[i]>>lenn[i];
			//FOR(i,1,l) outf<< ss[i]<<lenn[i]<<endl;
			FOR(i,0,mp) minn[i]=maxx[i]=imp;
			FOR(i,0,mp) minn1[i]=maxx1[i]=imp;
			int cx=0;int cy=0;

			add(cx,cy);
			
			int dire=0;//0-left 1-up
			dx[0]=1;dy[0]=0;
			dx[1]=0;dy[1]=1;
			dx[2]=-1;dy[2]=0;
			dx[3]=0;dy[3]=-1;
			int direback= dire;
			anw2=0;
			FOR(i,1,l)
				FOR(j,1,lenn[i]){
					string s=ss[i];
					FOR(ch,0,s.length()-1){
						char c=s[ch];
						if(c=='L') dire=dire+1;
						if(c=='R') dire=dire-1;

						dire=(dire+4)%4;
						if(c=='F') {
							cx=cx+dx[dire];
							cy=cy+dy[dire];
							if(dx[dire]!=0) {addd(cx-dx[dire],cx,cy);}

						}
						//outf<<"ADD"<<cx<<" "<<cy<<endl;
						add(cx,cy);
						add1(cy,cx);
					}
			}
			//qq
			anw=0;
			/*
			FOR(x,0,mp-10){
				if ((minn[x]!=imp) &&(minn[x+1]!=imp)) {
					outf<<x<<endl;
					outf<<maxx[x]<<endl;
					outf<<minn[x]<<endl;
					anw=anw+maxx[x]-minn[x];

				}
			}*/

			/*
			FOR(x,-3000,3000) {
				if(minn[x+delta]==imp) continue;
					int l=minn[x+delta];
					int r=maxx[x+delta];

					//l=-3000;r=3000;

				FOR(y,l,r-1){
				if (iss(x+1,y) &&iss(x,y+1) &&iss(x,y) && iss(x+1,y+1)) {anw++;
				//outf<<x<<" "<<y<<endl;
				}
			}}
			*/
			
			
					FOR(x,-3000,3000) FOR(y,-3000,3000){
				if (iss(x+1,y) &&iss(x,y+1) &&iss(x,y) && iss(x+1,y+1)) {anw++;
				//outf<<x<<" "<<y<<endl;
				}
			}
			


			

	



			anw2=abs(anw2);
			anw=abs(anw);
			outf << "Case #"<<ii<<": "<<abs(anw-anw2)<<endl;
			//outf << "Case #"<<ii<<": "<<anw<<endl;
	
		//outf <<endl;
		//printf("Case #%d: \n",ii);

	}


	outf.close();  
   return 0;
}